import toml
from pathlib import Path
from markdown import markdown
from lorem_text import lorem

from src.appcli import AppCLI

class Utils():

    @staticmethod
    def print_if_verbose(cli, message):
        if cli.args.verbose:
            print(message)

    @staticmethod
    def load_elements(cli, base_path_str, element_type):
        elements = {}

        target_dir = Path(base_path_str) / element_type
        Utils.print_if_verbose(cli, f"Loading Curricubook elements from: {target_dir}")

        for item in target_dir.iterdir():
            if item.is_file() and item.suffix.lower() == '.toml':
                metadata_file = toml.load(item)

                key = f"{metadata_file['metadata']['start_date_year']}_{metadata_file['metadata']['start_date_month']}"
                while key in elements:
                    key += "."

                elements[key] = {
                    "item_name": item.stem,
                    "title": metadata_file['metadata']['title'],
                    "start_date_year": metadata_file['metadata']['start_date_year'],
                    "start_date_month": metadata_file['metadata']['start_date_month'],
                    "end_date_year": metadata_file['metadata']['end_date_year'],
                    "end_date_month": metadata_file['metadata']['end_date_month'],
                    "metadata": item,
                    "content_brief": Path(base_path_str) / element_type / f"{item.stem}_brief.md",
                    "content_long": Path(base_path_str) / element_type / f"{item.stem}_long.md"
                }

        Utils.print_if_verbose(cli, f"Sorting {len(elements)} elements...")
        elements = dict(sorted(elements.items()))

        return elements.values()

    @staticmethod
    def load_curricubook_settings(cli, curricubook_path):
        curricubook_file = Path(curricubook_path)
        Utils.print_if_verbose(cli, f"Loading Curricubook settings from: {curricubook_file}")

        if not curricubook_file.is_file():
            return None

        return toml.load(curricubook_file)

    @staticmethod
    def load_template_metadata(cli, template_path):
        template_file = Path(template_path) / "metadata.toml"
        Utils.print_if_verbose(cli, f"Loading template metadata from: {template_file}")

        if not template_file.is_file():
            return None

        return toml.load(template_file)

    @staticmethod
    def markdown_to_html(markdown_str):
        return markdown(markdown_str, extensions=['tables'])

    def generate_lorem_ipsum(num_paragraphs):
        paragraphs = lorem.paragraphs(num_paragraphs)
        
        final_lorem = ""
        for paragraph in paragraphs.splitlines():
            final_lorem += f"{paragraph}\n\n"

        return final_lorem
    