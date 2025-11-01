# data-annotation-boats-buoys
Practice project for object detection (boats and buoys) — Data Annotation portfolio example.
# Data Annotation Practice — Barcos y Boyas (Detección de Objetos)

**Objetivo:** Crear un dataset pequeño y de calidad para detección de objetos (`boat`, `buoy`) con *guidelines* claras, QA y métricas, simulando un flujo profesional similar al de proyectos en plataformas como SuperAnnotate.

## Clases
- `1: boat` — Embarcaciones a motor/vela, dinghies, motos de agua (si lo decides), etc.
- `2: buoy` — Boyas de señalización (cardinales, laterales, de amarre, etc.).

> Nota: Si lo prefieres, puedes excluir motos de agua o separarlas como otra clase más adelante.

## Estructura
- `guidelines/` — Criterios detallados de anotación.
- `datasets/images/` — Imágenes fuente (50–200 para empezar).
- `annotations/images_coco/` — Anotaciones en formato COCO.
- `qa/` — Checklists y reportes de calidad.
- `project/` — Roadmap, backlog y métricas.
- `scripts/` — Utilidades de validación.

## Resultados (ejemplo — actualiza con tus datos reales)
- 50 imágenes anotadas, 12% con correcciones QA (cajas ligeramente recortadas).
- Tiempo medio por imagen: 40–60 s (dependiendo de densidad).
- Errores más comunes: incluir wake/estela en la caja, confundir balizas con farolas costeras.

## Próximos pasos
- Añadir `segmentation` (polígonos) para barcos.
- Ampliar clases: `jetski`, `sailboat` vs `motorboat`, `person`.
- Validación entre dos anotadores (consistencia inter-annotator).

## Uso rápido
1. Coloca imágenes en `datasets/images/`.
2. Anota y rellena `annotations/images_coco/sample_coco.json`.
3. Ejecuta `scripts/validate_coco.py` para chequeos básicos.
4. Pasa QA con `qa/checklists/image_qc_checklist.md` y documenta en `qa/reports/`.
---

## 📸 Créditos de imágenes

Las imágenes utilizadas en este proyecto provienen de bancos libres de derechos — **Unsplash**, **Pexels** y **Pixabay** — y se emplean únicamente con fines educativos y demostrativos dentro de un entorno de práctica de anotación de datos (*Data Annotation Practice Project*).

No se realiza uso comercial de las imágenes, ni se distribuyen con fines de venta o publicidad.  
Cada imagen mantiene los derechos originales de sus respectivos autores según las licencias abiertas de dichas plataformas.
