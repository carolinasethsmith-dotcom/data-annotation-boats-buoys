# Annotations — Boats & Buoys Dataset

This folder contains annotation data for the "Boats & Buoys" dataset.

Contents
- images_coco/ — directory containing images and (optionally) COCO-style files or related image assets.
- labels.text — label mapping file listing classes and their IDs.
- (optional) annotations in COCO, Pascal VOC, YOLO, or other formats.

Label file (labels.text)
- Current contents:
  ```
  1| Boat
  2| Buoy
  ```
- Format: each line lists the label ID, a separator (|), and the label name.
- Note: Some tooling expects zero-based label indices (0, 1, ...). Confirm your training pipeline's label indexing convention and convert if necessary.

Recommended README sections (English)
1. Overview
   - Short dataset description (what it contains, purpose).
   - Example: "Images of water scenes annotated with two classes: boats and buoys."

2. Directory structure
   - Explain each file/folder in annotations, e.g.:
     - annotations/images_coco/ — image files and COCO JSON annotation(s) if present.
     - annotations/labels.text — label ID → class name mapping.
     - annotations/*.json — annotation files (if any).

3. Annotation format(s)
   - If you use COCO: describe that the JSON includes "images", "annotations", "categories", and how category IDs map to labels.text.
   - If you use YOLO: explain label file naming convention (one .txt per image) and normalized bbox format (class_id x_center y_center width height).
   - If you use Pascal VOC: note XML structure per image.

4. How to use
   - Example commands or snippets to convert or load annotations into common frameworks (PyTorch, Detectron2, MMDetection, YOLOv5).
   - Mention whether labels.text uses 0-based or 1-based IDs and, if needed, provide a conversion snippet.

5. Quality and verification
   - Notes about annotation quality checks performed (if any).
   - Advice for additional checks (class balance, bounding box validity).

6. License
   - State the dataset license or usage terms (e.g., CC BY 4.0) or indicate "TBD".

7. Contributors & contact
   - List maintainers, how to report issues, and contact information.

8. Example
   - Provide one small example demonstrating how an image maps to annotation entry and label mapping. For example:
     - labels.text:
       ```
       1| Boat
       2| Buoy
       ```
     - COCO category entry example:
       ```json
       { "id": 1, "name": "Boat" }
       ```
     - YOLO example (if image `0001.jpg` has one boat):
       ```
       0 0.512 0.432 0.2 0.15
       ```
       (Note: YOLO uses zero-based class indices; here class 0 corresponds to "Boat".)

Notes and suggestions
- Make sure the README is entirely in English. If you have an existing README that contains other languages, replace those sections with the English text above or provide parallel translated sections (English first).
- Confirm whether your label indexing is zero- or one-based and harmonize labels.text and any annotation JSONs accordingly.
- If you want, I can produce a README tailored to the exact annotation format you use (COCO, YOLO, VOC). To do that I would need either:
  - the annotation file(s) (e.g., COCO JSON), or
  - a sample annotation file or a description of the annotation format used.

If you want, I can also create the README file in the repository for you — paste here whether you use COCO, YOLO, or VOC and I will adapt the README examples accordingly.

