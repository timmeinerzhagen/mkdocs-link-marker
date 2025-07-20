import re
import yaml
from pathlib import Path
import logging

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class LinkMarkerPlugin(BasePlugin):
    config_scheme = (
        ('enable_external_link', config_options.Type(bool, default=True)),
        ('icon_external_link', config_options.Type(str, default='⧉')),

        ('enable_mail', config_options.Type(bool, default=True)),
        ('icon_mail', config_options.Type(str, default='✉')),
    )

    def __init__(self):
        self.enabled = True

    def on_page_content(self, html, page, config, files):
        if self.config['enable_external_link']:
            p_external_link = re.compile('<a href="(http.*?)">(.*?)</a>')
            def repl_external_link(match):
                href, content = match.group(1), match.group(2)
                # Do not add icon if the content contains an <img> tag
                if re.search(r'<img\b', content, re.IGNORECASE):
                    return f'<a href="{href}">{content}</a>'
                return f'<a href="{href}">{content}&nbsp;{self.config["icon_external_link"]}</a>'
            html = p_external_link.sub(repl_external_link, html)

        if self.config['enable_mail']:
            p_mail = re.compile('<a href="(mailto:.*?)">(.*?)</a>')
            html = p_mail.sub('<a href="\\1">\\2&nbsp;' + self.config['icon_mail'] + '</a>', html)

        return html