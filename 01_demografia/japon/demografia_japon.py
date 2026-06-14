#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proyecto: Análisis Demográfico y Proyección Poblacional de Japón
Curso:    Ciencias Actuariales — Demografía
Autores:  Eduardo Carrillo Reyna
Fecha:    2025

Descripción:
    1. Tasas demográficas básicas (TBN, TBM, TNC, TBF, TMI, Esperanza de vida)
    2. Ajuste del modelo de mortalidad de Gompertz
    3. Construcción de la Matriz de Leslie para proyección poblacional
    4. Proyección de la población a 5, 10 y 20 años

Bases de datos requeridas:
    - base_datos_japon.csv         : Población por grupos quinquenales, tasas de supervivencia,
                                     fecundidad y migración neta.
    - tabla_vida_japon_2023.csv    : Tabla de vida completa (qx, px, lx, dx, Lx, Tx, ex)
                                     por sexo, para año base 2023.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.optimize import curve_fit
from scipy.linalg import eig
import warnings
warnings.filterwarnings("ignore")

plt.rcParams.update({
    "figure.dpi": 120,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.family": "DejaVu Sans",
    "axes.titlesize": 13,
    "axes.labelsize": 11,
})

# ─────────────────────────────────────────────────────────────
# BLOQUE 1 — Datos nacionales y carga de bases de datos
# ─────────────────────────────────────────────────────────────
NACIMIENTOS      = 770_759
DEFUNCIONES      = 1_568_961
MIGRACION_NETA   = 79_730
POBLACION_MEDIA  = 124_947_000
MUJERES_15_49    = 24_180_000

BASE_DIR = "./"
df_base  = pd.read_csv(BASE_DIR + "base_datos_japon.csv")
df_vida  = pd.read_csv(BASE_DIR + "tabla_vida_japon_2023.csv")

print(f"Base cargada: {len(df_base)} grupos | Tabla de vida: {len(df_vida)} edades")

# ─────────────────────────────────────────────────────────────
# BLOQUE 2 — Tasas demográficas básicas
# ─────────────────────────────────────────────────────────────
TBN  = (NACIMIENTOS  / POBLACION_MEDIA) * 1000
TBM  = (DEFUNCIONES  / POBLACION_MEDIA) * 1000
TNC  = TBN - TBM
TBF  = (NACIMIENTOS  / MUJERES_15_49)  * 1000
TMI  = (df_base.loc[df_base["grupo_edad"]=="0-4","poblacion_total"].values[0] * 0.00179
        / NACIMIENTOS) * 1000
EV0H = df_vida.loc[df_vida["edad"]==0,"ex_hombres"].values[0]
EV0M = df_vida.loc[df_vida["edad"]==0,"ex_mujeres"].values[0]

print(f"TBN={TBN:.2f}‰  TBM={TBM:.2f}‰  TNC={TNC:.2f}‰  TBF={TBF:.2f}‰")
print(f"TMI={TMI:.2f}‰  E(0)H={EV0H}  E(0)M={EV0M}")

# ─────────────────────────────────────────────────────────────
# BLOQUE 3 — Modelo de Gompertz:  μ(x) = a · exp(b · x)
# ─────────────────────────────────────────────────────────────
def gompertz(x, a, b):
    return a * np.exp(b * x)

df_adultos = df_vida[df_vida["edad"].between(30, 85)].copy()

for sexo, col_qx in [("Hombres", "qx_hombres"), ("Mujeres", "qx_mujeres")]:
    x   = df_adultos["edad"].values
    mu  = -np.log(1 - df_adultos[col_qx].values)
    popt, _ = curve_fit(gompertz, x, mu, p0=[0.00005, 0.09], maxfev=10000)
    a_fit, b_fit = popt
    mu_fit = gompertz(x, a_fit, b_fit)
    r2 = 1 - np.sum((mu - mu_fit)**2) / np.sum((mu - np.mean(mu))**2)
    print(f"Gompertz {sexo}: a={a_fit:.6f}  b={b_fit:.6f}  R²={r2:.6f}")

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.semilogy(x, mu,     "o", color="#01696f", ms=5, label="Observado")
    ax.semilogy(x, mu_fit, "-", color="#e8891f", lw=2, label=f"Gompertz (a={a_fit:.5f}, b={b_fit:.5f})")
    ax.set_title(f"Ajuste Gompertz — {sexo} | Japón 2023")
    ax.set_xlabel("Edad (años)")
    ax.set_ylabel("μ(x) [escala log]")
    ax.legend()
    plt.tight_layout()
    plt.savefig(f"gompertz_{sexo.lower()}.png")
    plt.show()

# ─────────────────────────────────────────────────────────────
# BLOQUE 4 — Matriz de Leslie
# ─────────────────────────────────────────────────────────────
df_leslie = df_base[df_base["grupo_edad"] != "85+"].copy().reset_index(drop=True)
n_grupos  = len(df_leslie)
Sx_H = df_leslie["supervivencia_hombres"].values
Sx_M = df_leslie["supervivencia_mujeres"].values
asfr = df_leslie["asfr"].values
RAZON_MASC = 0.512
Fx_H = asfr * RAZON_MASC       * Sx_H[0]
Fx_M = asfr * (1 - RAZON_MASC) * Sx_M[0]

def construir_leslie(n, Fx, Sx):
    L = np.zeros((n, n))
    L[0, :]    = Fx
    L[1:, :-1] = np.diag(Sx[:-1])
    return L

L_H = construir_leslie(n_grupos, Fx_H, Sx_H)
L_M = construir_leslie(n_grupos, Fx_M, Sx_M)

eigenvalues_M, _ = eig(L_M)
lambda1  = float(np.max(np.abs(eigenvalues_M)))
r_intrin = np.log(lambda1) / 5
print(f"λ₁={lambda1:.6f}  r={r_intrin:.6f} anual")

# ─────────────────────────────────────────────────────────────
# BLOQUE 5 — Proyección (4 periodos quinquenales = 20 años)
# ─────────────────────────────────────────────────────────────
P0_H = df_leslie["poblacion_hombres"].values.astype(float)
P0_M = df_leslie["poblacion_mujeres"].values.astype(float)
mig_H = df_leslie["migracion_neta_hombres"].values.astype(float)
mig_M = df_leslie["migracion_neta_mujeres"].values.astype(float)

def proyectar(L, P0, pasos, migracion=None):
    serie = [P0.copy()]
    P = P0.copy()
    for _ in range(pasos):
        P = L @ P
        if migracion is not None:
            P = np.maximum(P + migracion, 0)
        serie.append(P.copy())
    return serie

serie_H = proyectar(L_H, P0_H, pasos=4, migracion=mig_H)
serie_M = proyectar(L_M, P0_M, pasos=4, migracion=mig_M)
anios   = [2020, 2025, 2030, 2040]
totales = [serie_H[i].sum() + serie_M[i].sum() for i in range(len(anios))]

for yr, tot in zip(anios, totales):
    print(f"  {yr}: {tot/1e6:.3f} millones")

# ─────────────────────────────────────────────────────────────
# BLOQUE 6 — Gráficas
# ─────────────────────────────────────────────────────────────
grupos_labels = df_leslie["grupo_edad"].tolist()
fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(grupos_labels,  P0_H / 1e6, color="#01696f", label="Hombres")
ax.barh(grupos_labels, -P0_M / 1e6, color="#d97706", label="Mujeres")
ax.set_xlabel("Población (millones)")
ax.set_title("Pirámide poblacional de Japón — 2020")
ax.legend()
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{abs(x):.1f}"))
plt.tight_layout()
plt.savefig("piramide_2020.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(anios, [t/1e6 for t in totales], "o-", color="#01696f", lw=2.5, ms=8)
ax.set_title("Proyección de la población total de Japón")
ax.set_xlabel("Año")
ax.set_ylabel("Millones de habitantes")
for yr, tot in zip(anios, totales):
    ax.annotate(f"{tot/1e6:.2f}M", (yr, tot/1e6), textcoords="offset points",
                xytext=(0,10), ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("proyeccion_poblacion.png")
plt.show()

print("\n✓ Proyecto de demografía completado.")
