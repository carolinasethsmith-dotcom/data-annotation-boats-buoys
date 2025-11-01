import json
import cv2
import os

# Base directory (your project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
ANNOTATION_FILE = os.path.join(BASE_DIR, "annotations", "images_coco", "sample_coco.json")
IMAGE_DIR = os.path.join(BASE_DIR, "datasets", "images")

# Load COCO annotations
with open(ANNOTATION_FILE, "r") as f:
    coco = json.load(f)

# Category names
categories = {cat["id"]: cat["name"] for cat in coco["categories"]}

# Show each image with boxes
for img_info in coco["images"]:
    image_path = os.path.join(IMAGE_DIR, img_info["file_name"])
    image = cv2.imread(image_path)

    if image is None:
        print(f"⚠️ Could not open {img_info['file_name']}")
        continue

    # Draw boxes for each annotation
    for ann in coco["annotations"]:
        if ann["image_id"] == img_info["id"]:
            x, y, w, h = ann["bbox"]
            cat_name = categories[ann["category_id"]]
            color = (0, 255, 0) if cat_name == "boat" else (0, 0, 255)
            cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), color, 2)
            cv2.putText(image, cat_name, (int(x), int(y) - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow(img_info["file_name"], image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
