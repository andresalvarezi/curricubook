import os
from pathlib import Path
import sys
import toml

from src.appcli import AppCLI
from src.utils import Utils

class GeneratorPDF:
    def __init__(self, cli, curricubook_settings):
        self.cli = cli
        self.curricubook_settings = curricubook_settings

    def generate(self):
        self.template_path = Path("templates") / self.curricubook_settings['generation_pdf']['template'].lower() / "pdf"

        path = Path(self.cli.args.path) / "output" / "pdf"
        if not path.is_dir():
            path.mkdir(parents=True, exist_ok=True)

        Utils.print_if_verbose(self.cli, "...done!")
