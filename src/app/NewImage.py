# -*- coding: utf-8 -*-
import sys

from PIL import Image, ImageDraw, ImageFont, ImageGrab

from src.app.ReadImage import TextDetector
from src.app.TranslateFunction import Translator


class ImageTranslator:
    def __init__(self):
        pass

    def create_image(
        self, image_path="!clipboard!", source_lang="en", target_lang="pt"
    ):
        detector = TextDetector()
        translator = Translator()

        if image_path == "!clipboard!":
            original_image = ImageGrab.grabclipboard()
            detected_texts = detector.detect_text(clip="yes", clipImage=original_image)
        else:
            original_image = Image.open(image_path)
            detected_texts = detector.detect_text(image_path)

        draw = ImageDraw.Draw(original_image)

        font = ImageFont.load_default()

        text_color = "red"

        detected_texts = detected_texts[1:]

        detected_texts.sort(key=lambda x: (x[1][0][1], x[1][0][0]))

        groups = []
        current_group = [detected_texts[0]]
        for i in range(1, len(detected_texts)):
            dt = detected_texts[i][1][0]
            cg = current_group[-1][1][3]
            if (dt[1] > cg[1]) or (dt[0] > cg[0] + 200):
                groups.append(current_group)
                current_group = [detected_texts[i]]
            else:
                current_group.append(detected_texts[i])
        groups.append(current_group)
        for group in groups:
            group.sort(key=lambda x: x[1][0][0])
            main_str = ""
            for i in group:
                if len(main_str) > 0:
                    main_str = main_str + " " + i[0]
                else:
                    main_str = i[0]
            translated_text = translator.translate_text(
                main_str, target_language=target_lang, source_language=source_lang
            )  #
            try:
                bbox = draw.textbbox(group[0][1][0], translated_text, font=font)
                draw.rectangle(bbox, fill="white")
                draw.text(group[0][1][0], translated_text, fill=text_color, font=font)
            except UnicodeEncodeError as e:
                print(f"UnicodeEncodeError: {e}", file=sys.stderr)

        original_image.show()
