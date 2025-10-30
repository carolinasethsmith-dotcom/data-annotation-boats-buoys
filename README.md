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

## Next steps
- Add `segmentation` (polygons) for boats.
- Expand classes: `jetski`, `sailboat` vs `motorboat`, `person`.
- Perform inter-annotator validation (consistency between two annotators).
