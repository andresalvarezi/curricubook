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
        source_path = Path("templates") / self.curricubook_settings['generation']['template'].lower() / "html" / "header.html"
        with open(source_path, "r") as f:
            html = f.read()

        html = html.replace("{curricubook.name}", self.curricubook_settings['curricubook']['name'])
        html = html.replace("{curricubook.author_name}", self.curricubook_settings['curricubook']['author_name'])
        html = html.replace("{curricubook.author_email}", self.curricubook_settings['curricubook']['author_email'])

        return html

    def generate_body(self):
        html = ""

        for element_type in [ "education", "work", "personal", "extra" ]:
            current_elements = Utils.load_elements(self.cli, self.cli.args.path, element_type)

            if len(current_elements) > 0:
                html += self.generate_section_html(html, element_type, current_elements)

        return html

    def generate_section_html(self, html, element_type, current_elements):
        html = ""

        source_path = Path("templates") / self.curricubook_settings['generation']['template'].lower() / "html" / "beginsection.html"
        with open(source_path, "r") as f:
            htmlsection = f.read()

        htmlsection = htmlsection.replace("{section.name}", element_type)
        html += htmlsection

        for elem in current_elements:
            html += self.generate_element_html(html, element_type, elem)

        source_path = Path("templates") / self.curricubook_settings['generation']['template'].lower() / "html" / "endsection.html"
        with open(source_path, "r") as f:
            htmlsection = f.read()

        htmlsection = htmlsection.replace("{section.name}", element_type)
        html += htmlsection

        return html

    def generate_element_html(self, html, element_type, elem):
        source_path = Path("templates") / self.curricubook_settings['generation']['template'].lower() / "html" / "element.html"
        with open(source_path, "r") as f:
            html = f.read()

        html = html.replace("{element.item_name}", elem['item_name'])
        html = html.replace("{element.title}", elem['title'])
        html = html.replace("{element.date}", elem['date'])
 
        with open(str(elem['content_brief']), "r") as f:
            content_brief = f.read()

        with open(str(elem['content_long']), "r") as f:
            content_long = f.read()

        html = html.replace("{element.content_brief}", Utils.markdown_to_html(content_brief))
        html = html.replace("{element.content_long}", Utils.markdown_to_html(content_long))

        return html

    def generate_footer(self):
        source_path = Path("templates") / self.curricubook_settings['generation']['template'].lower() / "html" / "footer.html"
        with open(source_path, "r") as f:
            html = f.read()

        html = html.replace("{curricubook.name}", self.curricubook_settings['curricubook']['name'])
        html = html.replace("{curricubook.author_name}", self.curricubook_settings['curricubook']['author_name'])
        html = html.replace("{curricubook.author_email}", self.curricubook_settings['curricubook']['author_email'])

        return html

    def copy_template_assets(self):
        source_path = Path("templates") / self.curricubook_settings['generation']['template'].lower() / "html"

        css_source = source_path / "assets"
        css_target = Path(self.cli.args.path) / "output" / "html" / "assets"

        if css_target.is_dir():
            shutil.rmtree(css_target)

        shutil.copytree(css_source, css_target)
