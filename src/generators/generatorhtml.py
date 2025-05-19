import os
from pathlib import Path
import sys
import toml
import shutil

from src.appcli import AppCLI
from src.utils import Utils

class GeneratorHTML:
    def __init__(self, cli, curricubook_settings):
        self.cli = cli
        self.curricubook_settings = curricubook_settings

    def generate(self):
        path = Path(self.cli.args.path) / "output" / "html"
        if not path.is_dir():
            path.mkdir(parents=True, exist_ok=True)

        Utils.print_if_verbose(self.cli, "...generating HTML header...")
        html = self.generate_head()
        
        Utils.print_if_verbose(self.cli, "...adding Curricubook content to document:")
        html += self.generate_body()

        Utils.print_if_verbose(self.cli, "...generating HTML footer...")
        html += self.generate_footer()

        Utils.print_if_verbose(self.cli, "...copying template assets...")
        self.copy_template_assets()
        
        with open(path / "index.html", "w") as f:
            f.write(html)

        Utils.print_if_verbose(self.cli, "...done!")

    def generate_head(self):
        html  = "<!DOCTYPE html>\n"
        html += "<html lang=\"en\">\n\n"

        html += "<head>\n"
        html += "    <meta charset=\"UTF-8\">\n"
        html += "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        html += f"    <title>{self.curricubook_settings['curricubook']['name']} - Curricubook</title>\n"
        html += f"    <link rel=\"stylesheet\" href=\"styles.css\">\n"
        html += "</head>\n\n"

        html += "<body>\n"

        return html

    def generate_body(self):
        html = ""

        return html

    def generate_footer(self):
        html  = "</body>\n\n"

        html += "</html>\n"

        return html

    def copy_template_assets(self):
        source_path = Path("templates") / self.curricubook_settings['generation']['template'].lower() / "html"

        css_source = source_path / "styles.css"
        css_target = Path(self.cli.args.path) / "output" / "html" / "styles.css"

        shutil.copy2(str(css_source), str(css_target))