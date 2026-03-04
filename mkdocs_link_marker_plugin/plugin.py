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


        ('external_link_parameters', config_options.Type(dict, default={})),
        ('external_mail_parameters', config_options.Type(dict, default={})),
      
        ('ignore_list', config_options.Type(list, default=[])),
    )

    def __init__(self):
        self.enabled = True

    @staticmethod
    def build_parameters(parameters):
        if not parameters:
            return ''
    
        return ' ' + ' '.join([f'{k}={v}' for k, v in parameters.items()])

    def on_page_content(self, html, page, config, files):
        if self.config['enable_external_link']:
            p_external_link = re.compile('<a href="(http.*?)">(.*?)</a>')
            def repl_external_link(match):
                href, content = match.group(1), match.group(2)
                parameters = self.build_parameters(self.config["external_link_parameters"])
                # Do not modify ignored urls
                if href in self.config['ignore_list']:
                    return f'<a href="{href}">{content}</a>'
                # Do not add icon if the content contains an <img> tag
                if re.search(r'<img\b', content, re.IGNORECASE):
                    return f'<a href="{href}"{parameters}>{content}</a>'
                return f'<a href="{href}"{parameters}>{content}&nbsp;{self.config["icon_external_link"]}</a>'
            html = p_external_link.sub(repl_external_link, html)

        if self.config['enable_mail']:
            p_mail = re.compile('<a href="(mailto:.*?)">(.*?)</a>')
            parameters = self.build_parameters(self.config["external_mail_parameters"])
            html = p_mail.sub(f'<a href="\\1"{parameters}>\\2&nbsp;' + self.config['icon_mail'] + '</a>', html)

        return html
