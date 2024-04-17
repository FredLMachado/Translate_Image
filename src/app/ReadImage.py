# -*- coding: utf-8 -*-
import io

from google.cloud import vision


class TextDetector:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def detect_text(self, image_path="nil", clipImage="nil", clip="no"):
        if clip == "yes":
            with io.BytesIO() as output:
                clipImage.save(output, format="PNG")
                content = output.getvalue()
        else:
            with open(image_path, "rb") as image_file:
                content = image_file.read()

        image = vision.Image(content=content)

        response = self.client.text_detection(image=image)
        texts = response.text_annotations

        if texts:
            return [
                (
                    text.description,
                    [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices],
                )
                for text in texts
            ]
        else:
            return []
