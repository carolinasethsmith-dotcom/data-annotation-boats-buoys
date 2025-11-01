# data-annotation-boats-buoys
Practice project for object detection (boats and buoys) — Data Annotation portfolio example.

# Data Annotation Practice — Boats and Buoys (Object Detection)

**Objective:** Create a small, high-quality dataset for object detection (`boat`, `buoy`) with clear guidelines, QA, and metrics, simulating a professional workflow similar to projects on platforms like SuperAnnotate.

## Classes
- `1: boat` — Motorboats/sailboats, dinghies, jet skis (if you choose), etc.
- `2: buoy` — Navigation buoys (cardinal, lateral, mooring, etc.).

> Note: If you prefer, you can exclude jet skis or add them as a separate class later.

## Structure
- `guidelines/` — Detailed annotation criteria.
- `datasets/images/` — Source images (50–200 to start).
- `annotations/images_coco/` — Annotations in COCO format.
- `qa/` — Checklists and quality reports.
- `project/` — Roadmap, backlog, and metrics.
- `scripts/` — Validation utilities.

## Results (example — update with your real data)
- 50 images annotated, 12% with QA corrections (slightly cropped boxes).
- Average time per image: 40–60 s (depending on object density).
- Most common errors: including wake in the box, confusing buoys with coastal lampposts.

<<<<<<< HEAD
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
=======
## Next steps
- Add `segmentation` (polygons) for boats.
- Expand classes: `jetski`, `sailboat` vs `motorboat`, `person`.
- Perform inter-annotator validation (consistency between two annotators).
>>>>>>> 75e4b45d0e908bf202c94ee9985e720c818bdd9b
