# mkdocs-link-marker

MkDocs plugin for marking external or mail links in your documentation.

![comparison](https://github.com/timmeinerzhagen/mkdocs-link-marker/blob/main/docs/comparison.png)
## Setup

1. Install the plugin:
    ```bash
    pip install mkdocs-link-marker
    ```
2. Add the plugin to your `mkdocs.yml`
    ```bash
    plugins:
        - search
        - link-marker
    ```

## Usage

Run the build!

## Options

`enable_external_link`
Whether to mark external links with the according icon.
Default: True

`icon_external_link`
Change the default icon for marking external links.
Default: ⧉

`enable_mail`
Whether to mark mail links with the according icon.
Default: True

`icon_mail`
Change the default icon for marking mail links.
Default: ✉
