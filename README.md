# isrmltoolkit - Outlier Detection & Winsorization Toolkit

Una colección de herramientas para preprocesamiento de datos en proyectos de Machine Learning, enfocadas en la detección y tratamiento de valores atípicos (outliers), winsorización y análisis visual comparativo.

Actualmente incluye métodos clásicos y modernos para identificar y corregir valores extremos, además de visualizaciones útiles. Más herramientas se encuentran en desarrollo.

---

## Características principales

- Detección de outliers con múltiples métodos:
  - IQR (`iqr_outliers`)
  - Z-Score (`z_outliers`)
  - Mahalanobis Distance (`maha_outliers`)
  - Isolation Forest (`iso_outliers`)
- Winsorización automática para variables numéricas
- Comparación visual de boxplots antes y después del tratamiento
- Modular y fácil de integrar en pipelines de Machine Learning

---

## Instalación

```bash
pip install isrmltoolkit
