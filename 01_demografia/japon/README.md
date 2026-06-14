# 🗾 Análisis Demográfico y Proyección Poblacional de Japón

**Proyecto académico — Ciencias Actuariales**  
Eduardo Carrillo Reyna · Facultad de Contaduría y Administración

---

## 📋 Descripción del proyecto

Este proyecto realiza un análisis demográfico completo de Japón empleando técnicas
actuariales y estadísticas. El análisis cubre cuatro bloques principales:

1. **Tasas demográficas básicas** — TBN, TBM, TNC, TBF, TMI y esperanza de vida
2. **Modelo de Gompertz** — ajuste de la fuerza de mortalidad adulta
3. **Matriz de Leslie** — modelo matricial de proyección poblacional por grupos quinquenales
4. **Proyección a 5, 10 y 20 años** — con migración neta incorporada

---

## 📁 Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `demografia_japon.py` | Código principal con los 6 bloques del análisis |
| `base_datos_japon.csv` | Población por grupos quinquenales, supervivencia, ASFR y migración |
| `tabla_vida_japon_2023.csv` | Tabla de vida completa (qx, px, lx, dx, Lx, Tx, ex) por sexo |

### Estructura de `base_datos_japon.csv`

| Columna | Descripción |
|---|---|
| `grupo_edad` | Grupo quinquenal (0-4, 5-9, ..., 85+) |
| `poblacion_hombres / mujeres` | Población absoluta por sexo |
| `supervivencia_hombres / mujeres` | Probabilidad de sobrevivir al siguiente grupo (Sₓ) |
| `asfr` | Tasa específica de fecundidad (por mujer del grupo) |
| `razon_masculinidad` | Razón H/M en el grupo |
| `migracion_neta_hombres / mujeres` | Flujo migratorio neto por periodo quinquenal |

### Estructura de `tabla_vida_japon_2023.csv`

| Columna | Descripción |
|---|---|
| `edad` | Edad exacta |
| `qx_h / qx_m` | Probabilidad de muerte entre x y x+1 |
| `px_h / px_m` | Probabilidad de supervivencia (1 − qx) |
| `lx_h / lx_m` | Sobrevivientes a la edad x (de una cohorte de 100,000) |
| `dx_h / dx_m` | Defunciones entre x y x+1 |
| `Lx_h / Lx_m` | Años-persona vividos en [x, x+1) |
| `Tx_h / Tx_m` | Años-persona vividos a partir de x |
| `ex_h / ex_m` | Esperanza de vida a la edad x |

---

## ⚙️ Requisitos e instalación

```bash
pip install numpy pandas matplotlib scipy
```

---

## ▶️ Cómo ejecutar

```bash
# Asegúrate de estar en la carpeta del proyecto
cd 01_demografia/japon

# Ejecutar el análisis completo
python demografia_japon.py
```

El script genera automáticamente 4 gráficas:
- `gompertz_hombres.png` — Ajuste del modelo de Gompertz para hombres
- `gompertz_mujeres.png` — Ajuste del modelo de Gompertz para mujeres
- `piramide_2020.png` — Pirámide de población (año base)
- `proyeccion_poblacion.png` — Proyección de la población total

---

## 🔢 Fundamentos matemáticos

### Tasa Bruta de Natalidad
```
TBN = (Nacimientos / Población media) × 1000
```

### Modelo de Gompertz
```
μ(x) = a · exp(b · x)
```
- **a** = intensidad de mortalidad basal (riesgo en edad 0)
- **b** = tasa de envejecimiento biológico

La estimación de a y b se realiza por mínimos cuadrados no lineales sobre la
fuerza de mortalidad transformada: `μ(x) = −ln(1 − qx)`

### Matriz de Leslie
```
       [ F₀  F₁  F₂  ···  Fₙ ]
       [ S₀  0   0   ···  0  ]
L  =   [ 0   S₁  0   ···  0  ]
       [ ·   ·   ·   ···  ·  ]
       [ 0   0   ···  Sₙ₋₁ 0 ]
```
La tasa intrínseca de crecimiento se obtiene del eigenvalor dominante λ₁:
```
r = ln(λ₁) / 5    (por año, con periodo quinquenal)
```

---

*Proyecto académico — Ciencias Actuariales | UAQ*
