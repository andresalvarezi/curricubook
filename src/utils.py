import toml
from pathlib import Path

from src.appcli import AppCLI

class Utils():

    @staticmethod
    def print_if_verbose(cli, message):
        if cli.args.verbose:
            print(message)

    @staticmethod
    def load_elements(cli, base_path_str, element_type):
        elements = []

        target_dir = Path(base_path_str) / element_type

        for item in target_dir.iterdir():
            if item.is_file() and item.suffix.lower() == '.toml':
                metadata_file = toml.load(item)

                elements.append({
                    "item_name": item.stem,
                    "title": metadata_file['metadata']['title'],
                    "date": metadata_file['metadata']['date'],
                    "metadata": item,
                    "content_brief": Path(base_path_str) / element_type / f"{item.stem}_brief.md",
                    "content_long": Path(base_path_str) / element_type / f"{item.stem}_long.md"
                })

        return elements

    @staticmethod
    def load_curricubook_settings(cli, curricubook_path):
        curricubook_file = Path(curricubook_path)
        if not curricubook_file.is_file():
            return None

        return toml.load(curricubook_file)
