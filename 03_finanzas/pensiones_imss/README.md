# 🏦 Simulador Profesional de Pensión IMSS

**Asignatura:** Finanzas Actuariales / Seguridad Social  
**Proyecto:** Calculadora interactiva de pensión IMSS — Comparativa Ley 73 vs Ley 97  
**Herramienta:** HTML + JavaScript (aplicación web sin dependencias externas)

---

## 🎯 ¿Qué hace esta aplicación?

Es un **simulador profesional de pensión IMSS** completamente interactivo que evalúa todas las opciones de retiro disponibles para un trabajador mexicano, desde la lectura automática de su constancia de semanas cotizadas hasta la recomendación final priorizada con score de conveniencia. Cubre el análisis actuarial y financiero completo en 15 secciones.

---

## 📋 Descripción de cada sección

### 1. Lectura de constancia IMSS
Carga la **Constancia de Semanas Cotizadas** del IMSS. Soporta PDF con texto, PDF escaneado (OCR vía Tesseract.js), imagen JPG/PNG y pegado directo de texto. Los campos detectados (NSS, semanas, SBC, historial laboral y brechas sin cotizar) se pre-llenan automáticamente y son editables.

### 2. Datos del trabajador
Captura edad, salario base de cotización (SBC), semanas acumuladas y saldo AFORE. Incluye botón **"Cargar ejemplo demo"** para explorar sin datos reales.

### 3. Régimen aplicable
Determina automáticamente si el trabajador pertenece a **Ley 73**, **Ley 97** o ambas, con base en su historial de cotización y fecha de afiliación al IMSS.

### 4. Pensión base Ley 73
Calcula la pensión conforme al Art. 167 LSS:
- **Cuantía básica:** 35% del SBC promedio de las últimas 250 semanas
- **Incrementos:** +1.25% por cada año adicional de servicio (de 10 a 25 años)
- **PMG:** Verifica la Pensión Mínima Garantizada (~$7,811.68 indexada al INPC)

### 5. Análisis por edades de retiro (60–65 años)
Proyecta la pensión estimada para cada año de retiro posible con semáforo de conveniencia y gráficas de costo de oportunidad acumulado.

### 6. Costo de oportunidad mensual
Calcula mes a mes el punto de equilibrio en que esperar más años para retirarse se vuelve más rentable que retirarse a los 60.

### 7. Modalidad 40 prospectiva
Tabla de costos anuales y acumulados para cotizar voluntariamente con un SBC mayor, con proyección de mejora en pensión y tiempo de recuperación.

### 8. Modalidad 40 retroactiva
Costo de cubrir periodos pasados sin cotizar aplicando el recargo acumulable del **2.07% mensual** (Art. 287 LSS). Permite seleccionar qué brechas históricas incluir.

### 9. Financiamiento con 3 financieras
Comparativa de crédito en tres bancos para financiar la inversión M40: CAT, mensualidad, intereses totales, flujo neto y tabla de amortización completa.

### 10. Comparativa Ley 73 vs Ley 97
Estimación Ley 97 a partir del saldo AFORE: retiro programado, renta vitalicia teórica y comparativa directa incluyendo riesgo, certeza del flujo y herencia.

### 11. Resumen maestro — Comparativo final
Tabla con todas las opciones: pensión mensual/anual, inversión inicial, costo financiero, flujo neto a 10/20/25 años, riesgo, complejidad, liquidez y **score de conveniencia**.

### 12. Recomendación priorizada
Recomendación final con justificación detallada de la opción más conveniente según el perfil del trabajador.

### 13. Supuestos y parámetros editables
Todas las constantes son auditables y modificables: inflación, rendimiento AFORE, esperanza de vida, tasas bancarias. Etiquetas indican origen: `oficial`, `editable`, `estimado`.

### 14. Fórmulas y normativa
Fórmulas actuariales utilizadas con referencias a la Ley del Seguro Social (Arts. 154, 162, 167, 168, 287).

### 15. Exportar resultados
Genera reportes imprimibles y de respaldo para expediente personal o asesor.

---

## 🧮 Modelos y fórmulas clave

| Concepto | Base legal / fórmula |
|---|---|
| Cuantía básica Ley 73 | Art. 167 LSS: 35% SBC promedio últimas 250 semanas |
| Incremento por años de servicio | +1.25% por cada año adicional de 10 a 25 años cotizados |
| PMG (Pensión Mínima Garantizada) | Indexada al INPC, referencia ~$7,811.68 (2024) |
| Recargo M40 retroactiva | 2.07% mensual acumulable (Art. 287 LSS) |
| Retiro programado Ley 97 | Saldo AFORE / esperanza de vida CONAPO (meses restantes) |
| Costo de oportunidad | Σ pensión mensual × meses esperados hasta equilibrio |

---

## 🚀 Cómo usar

```bash
# Solo abre el archivo HTML en cualquier navegador moderno
open pensiones_imss.html
# No requiere servidor, instalación ni dependencias
```

1. Carga tu constancia IMSS **o** usa **"Cargar ejemplo demo"**
2. Verifica y ajusta los datos pre-llenados
3. Da clic en **"Calcular pensión"**
4. Navega por las secciones 4–12
5. Exporta desde la sección 15

---

## 📦 Tecnología

- **HTML5 + CSS3 + JavaScript puro** — Sin frameworks ni servidor
- **Tesseract.js** — OCR para PDFs escaneados
- **PDF.js** — Extracción de texto de PDFs digitales
- **Chart.js** — Visualizaciones interactivas
- Funciona completamente **offline** desde el navegador

---

## 🔗 Referencias normativas

- Ley del Seguro Social (LSS) — Arts. 154, 162, 167, 168, 287
- CONSAR — Parámetros de retiro programado
- CONAPO — Tablas de esperanza de vida
- INEGI / INPC — Actualización de PMG
