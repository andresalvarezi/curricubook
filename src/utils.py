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
        Utils.print_if_verbose(cli, f"...looking for elements in {target_dir}")

        for item in target_dir.iterdir():
            if item.is_file() and item.suffix.lower() == '.toml':
                Utils.print_if_verbose(cli, f"...found element: {item.name}")
                elements.append({
                    "name": item.stem,
                    "metadata": item,
                    "content": Path(base_path_str) / element_type / f"{item.stem}.md"
                })

        Utils.print_if_verbose(cli, f"...{len(elements)} elements where found")
        return elements