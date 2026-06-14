# 📊 Análisis de Población y Proyección Demográfica — Japón 2024

**Asignatura:** Demografía  
**Proyecto final:** Análisis demográfico de la población y proyección a futuro (50 años)  
**Caso de estudio:** Japón 2024  
**Herramienta:** Python (Jupyter Notebook)

---

## 🎯 Objetivo

Realizar un análisis demográfico completo de Japón utilizando datos reales de 2023–2024, calculando indicadores de estructura poblacional, ajustando modelos de mortalidad y proyectando la población 50 años hacia el futuro (hasta 2074) con intervalos de incertidumbre.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|---|---|
| `ProyectoFinal.ipynb` | Notebook principal con todo el análisis paso a paso |
| `base_datos_japon.csv` | Población por grupo quinquenal, supervivencia, fecundidad y migración neta 2023 |
| `tabla_vida_japon_2023.csv` | Tabla de vida completa por edad simple (edades 0–105) para hombres y mujeres |

---

## 🗃️ Descripción de las bases de datos

### `base_datos_japon.csv`

Contiene 20 grupos quinquenales (0–4 hasta 95+):

| Columna | Descripción |
|---|---|
| `grupo_edad` | Grupo quinquenal de edad |
| `pob_H` | Población masculina observada en 2024 |
| `pob_M` | Población femenina observada en 2024 |
| `pob_total` | Población total por grupo |
| `s(x)_H` | Probabilidad de supervivencia quinquenal — hombres |
| `s(x)_M` | Probabilidad de supervivencia quinquenal — mujeres |
| `asfr_por_mujer` | Tasa específica de fecundidad por mujer (ASFR) |
| `mig_neta_2023` | Migración neta distribuida por grupo de edad (2023) |

### `tabla_vida_japon_2023.csv`

Tabla de vida completa con edades individuales de 0 a 105:

| Columna | Descripción |
|---|---|
| `edad` | Edad exacta en años |
| `qx_H` / `qx_M` | Probabilidad de morir a la edad x (hombres / mujeres) |
| `px_H` / `px_M` | Probabilidad de sobrevivir a la edad x (hombres / mujeres) |

---

## 🔬 Metodología y contenido del notebook

### Sección 1 — Librerías y carga de datos
Se importan `numpy`, `pandas`, `matplotlib` y `scipy`, y se cargan ambas bases de datos. Se verifican las estructuras y se muestran las primeras filas para validar la integridad de los datos antes de cualquier cálculo.

### Sección 2 — Notación, variables y cálculo de tasas básicas

| Indicador | Fórmula | Resultado Japón 2024 |
|---|---|---|
| TBN (Tasa Bruta de Natalidad) | B / P(t) × 1000 | 5.98 ‰ |
| TBM (Tasa Bruta de Mortalidad) | D / P(t) × 1000 | 12.96 ‰ |
| TBMig (Tasa Bruta Migratoria) | M / P(t) × 1000 | 1.48 ‰ |
| TC (Tasa de Crecimiento) | TBN − TBM + TBMig | −5.50 ‰ |
| ISF (Índice Sintético de Fecundidad) | 5 × Σf(x) | 1.198 |

La tasa de crecimiento negativa (−5.50‰) y el ISF muy por debajo del nivel de reemplazo (2.1) confirman que Japón se encuentra en una fase avanzada de decrecimiento poblacional.

### Sección 3 — Indicadores de estructura poblacional

- **IDV** (Índice de Dependencia de Vejez) = P65+ / P15–64 × 100 → **42.19**
- **IDJ** (Índice de Dependencia Juvenil) = P0–14 / P15–64 × 100 → **19.96**
- **IDT** (Índice de Dependencia Total) = IDV + IDJ → **62.16**

### Sección 4 — Índices de Friz, Sundbärg y Burgdöfer

| Índice | Valor | Clasificación |
|---|---|---|
| Friz | 64.05 | Población madura |
| Sundbärg A | 29.53 | Vieja / Regresiva |
| Sundbärg B | 110.32 | Vieja / Regresiva |
| Burgdöfer | 31.31 | Población vieja |

### Sección 5 — Pirámide poblacional 2024
Se construye la pirámide por grupos quinquenales y sexo. La forma de «barril invertido» evidencia el envejecimiento acelerado de la sociedad japonesa.

### Sección 6 — Ajuste del modelo de Gompertz
Se ajusta μ(x) = α · e^(β·x) a las tasas de mortalidad observadas por separado para hombres y mujeres usando `scipy.optimize.curve_fit`, con evaluación de bondad de ajuste mediante prueba KS.

### Sección 7 — Proyección poblacional (2024–2074)
Matriz de Leslie extendida con fecundidad, supervivencia y migración neta en pasos quinquenales.

| Año | Población (millones) |
|---|---|
| 2024 | 121.6 |
| 2034 | 117.2 |
| 2049 | 103.9 |
| 2064 | 87.4 |
| 2074 | 75.4 |

### Sección 8 — Intervalos de incertidumbre
Bandas de confianza mediante simulación estocástica variando supuestos de fecundidad y mortalidad.

### Sección 9 — Índice de envejecimiento proyectado
Evolución del índice de envejecimiento (mayores de 65 vs. menores de 15) a lo largo del horizonte de proyección.

---

## 📦 Dependencias

```bash
pip install numpy pandas matplotlib scipy
```

## 🔗 Fuentes de datos

- **Statistics Bureau of Japan** (2024)
- **Ministry of Health, Labour and Welfare Japan** — Tabla de vida 2023
- **National Institute of Population and Social Security Research (IPSS)**
