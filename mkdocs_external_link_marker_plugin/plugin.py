import re
import yaml
from pathlib import Path
import logging

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class ExternalLinkMarkerPlugin(BasePlugin):
    config_scheme = (
        ('external_link_icon', config_options.Type(str, default='.fa-external-link-alt')),
    )

    def __init__(self):
        self.enabled = True

    def on_page_content(self, html, page, config, files):

        print("html: ", html)
        return html.replace('</a>', '</a>Hello')