# Guidelines — Detección de Objetos: Barcos y Boyas

## Objetivo
Etiquetar con **cajas delimitadoras (bounding boxes)** las clases:
- `boat` (id=1)
- `buoy` (id=2)

## Definiciones y alcance
- **boat**: cualquier embarcación flotante diseñada para transporte o recreo. Incluye veleros, lanchas, yates, botes auxiliares (dinghies). Opcional: motos de agua (decide y sé consistente).
- **buoy**: boyas de señalización o amarre. Incluye boyas cardinales/laterales, esféricas, cilíndricas y de amarre.

**NO etiquetar como boat:**
- Embarcaciones en remolque sobre tierra.
- Maquetas, fotos en cuadros, reflejos sin objeto real.
- Boyas fijas tipo faro/torreta en muelles (si son estructuras grandes tipo *beacon* fijo → no es buoy).

## Reglas de dibujo
- La **bbox** debe cubrir el objeto visible completo, con margen ≤ 3 px.
- Si el objeto está **parcialmente fuera** de la imagen, ajusta la caja a la parte visible.
- Si está **ocluido**, dibuja la caja sobre la parte visible, sin adivinar lo oculto.
- No incluyas **estelas, sombras o reflejos**.

## Casos límite
- **Barcos muy lejanos**: si ocupan < 10×10 px y no hay certeza → no anotar.
- **Boyas semisumergidas**: anota si la parte visible permite identificarla como boya.
- **Confusión boya/baliza fija**: estructuras rígidas unidas a muelle/roca suelen NO ser `buoy`.

## Consistencia de clases
- Si decides excluir `jetski` de `boat`, documenta en README y no los anotes o crea una clase nueva en otra iteración.

## Calidad (errores críticos)
- Caja sin clase o clase incorrecta.
- Caja recortada (no cubre el borde del casco/mástil si es claramente visible).
- Cajas con área cero o negativas.
- Duplicados del mismo objeto.

## Nomenclatura
- Imágenes: `image_001.jpg`, `image_002.jpg`, ...
- IDs de imágenes en COCO deben corresponder 1:1 con `file_name`.

## Ejemplos
Incluye 5 ejemplos correctos/incorrectos (con capturas) cuando avances el proyecto.
