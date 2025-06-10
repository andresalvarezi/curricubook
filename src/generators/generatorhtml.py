import os
from pathlib import Path
import sys
import toml
import shutil

from src.appcli import AppCLI
from src.utils import Utils
from src.version import Version

class GeneratorHTML:
    def __init__(self, cli, curricubook_settings):
        self.cli = cli
        self.curricubook_settings = curricubook_settings

    def generate(self):
        self.template_metadata = Utils.load_template_metadata(self.cli, Path("templates") / self.curricubook_settings['generation_html']['template'].lower())
        self.template_path = Path("templates") / self.curricubook_settings['generation_html']['template'].lower() / "html"

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
        source_path = self.template_path / self.template_metadata['html']['header']
        with open(source_path, "r") as f:
            html = f.read()

        html = html.replace("{curricubook.name}", self.curricubook_settings['curricubook']['name'])
        html = html.replace("{curricubook.author_name}", self.curricubook_settings['curricubook']['author_name'])
        html = html.replace("{curricubook.author_email}", self.curricubook_settings['curricubook']['author_email'])

        return html

    def generate_body(self):
        html = ""

        html += self.generate_aboutme_html()

        for element_type in [ "education", "work", "personal", "extra" ]:
            current_elements = Utils.load_elements(self.cli, self.cli.args.path, element_type)

            if len(current_elements) > 0:
                html += self.generate_section_html(element_type, current_elements)

        return html

    def generate_aboutme_html(self):
        htmlaboutme = ""

        source_path = self.template_path / self.template_metadata['html']['about_me']
        with open(source_path, "r") as f:
            htmlaboutme = f.read()

        htmlaboutme = htmlaboutme.replace("{aboutme.author_name}", self.curricubook_settings['curricubook']['author_name'])
        htmlaboutme = htmlaboutme.replace("{aboutme.author_email}", self.curricubook_settings['curricubook']['author_email'])

        htmlaboutme = htmlaboutme.replace("{aboutme.links_homepage}", self.curricubook_settings['curricubook']['links_homepage'])
        htmlaboutme = htmlaboutme.replace("{aboutme.links_linkedin}", self.curricubook_settings['curricubook']['links_linkedin'])
        htmlaboutme = htmlaboutme.replace("{aboutme.links_github}", self.curricubook_settings['curricubook']['links_github'])

        with open(str(Path(self.cli.args.path) / "aboutme.md"), "r") as f:
            content = f.read()

        htmlaboutme = htmlaboutme.replace("{aboutme.content}", Utils.markdown_to_html(content))

        return htmlaboutme

    def generate_section_html(self, element_type, current_elements):
        html = ""

        source_path = self.template_path / self.template_metadata['html'][element_type]['begin_section']
        with open(source_path, "r") as f:
            htmlsection = f.read()

        htmlsection = htmlsection.replace("{section.name}", element_type.capitalize())
        html += htmlsection

        for elem in current_elements:
            html += self.generate_element_html(element_type, elem)

        source_path = self.template_path / self.template_metadata['html'][element_type]['end_section']
        with open(source_path, "r") as f:
            htmlsection = f.read()

        htmlsection = htmlsection.replace("{section.name}", element_type)
        html += htmlsection

        return html

    def generate_element_html(self, element_type, elem):
        source_path = self.template_path / self.template_metadata['html'][element_type]['element']
        with open(source_path, "r") as f:
            html = f.read()

        html = html.replace("{element.item_name}", elem['item_name'])
        html = html.replace("{element.title}", elem['title'])
        html = html.replace("{element.start_date_year}", str(elem['start_date_year']))
        html = html.replace("{element.start_date_month}", str(elem['start_date_month']))
        html = html.replace("{element.end_date_year}", str(elem['end_date_year']))
        html = html.replace("{element.end_date_month}", str(elem['end_date_month']))

        with open(str(elem['content_brief']), "r") as f:
            content_brief = f.read()

        with open(str(elem['content_long']), "r") as f:
            content_long = f.read()

        html = html.replace("{element.content_brief}", Utils.markdown_to_html(content_brief))
        html = html.replace("{element.content_long}", Utils.markdown_to_html(content_long))

        return html

    def generate_footer(self):
        source_path = self.template_path / self.template_metadata['html']['footer']
        with open(source_path, "r") as f:
            html = f.read()

        html = html.replace("{curricubook.core.url}", Version.curricubook_url)
        html = html.replace("{curricubook.core.version}", Version.curricubook_version)

        html = html.replace("{curricubook.name}", self.curricubook_settings['curricubook']['name'])
        html = html.replace("{curricubook.author_name}", self.curricubook_settings['curricubook']['author_name'])
        html = html.replace("{curricubook.author_email}", self.curricubook_settings['curricubook']['author_email'])

        return html

    def copy_template_assets(self):
        css_source = self.template_path / "assets"
        css_target = Path(self.cli.args.path) / "output" / "html" / "assets"

        if css_target.is_dir():
            shutil.rmtree(css_target)

        shutil.copytree(css_source, css_target)
