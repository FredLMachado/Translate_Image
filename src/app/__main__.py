# -*- coding: utf-8 -*-
import argparse

from dotenv import load_dotenv

from src.app.NewImage import ImageTranslator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file", type=str, help="File path. Leave empty for clipboard file"
    )
    parser.add_argument("-t", "--target", type=str, help="Target Language")
    parser.add_argument("-s", "--source", type=str, help="Source Language")
    args = parser.parse_args()

    load_dotenv()

    path = "!clipboard!"
    target = "pt"
    source = "en"
    if args.file:
        path = args.file
        print("File path:", args.file)
    if args.target:
        target = args.target
    if args.source:
        source = args.source
        print("Another String:", args.another_string)
    tr = ImageTranslator()
    tr.create_image(image_path=path, source_lang=source, target_lang=target)


if __name__ == "__main__":
    main()
