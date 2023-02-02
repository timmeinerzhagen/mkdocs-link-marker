from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mkdocs-external-link-marker',
    version='0.1.2',
    description='MkDocs plugin for marking external links.',    
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='mkdocs link external',
    url='https://github.com/timmeinerzhagen/mkdocs-external-link-marker',
    author='Tim Jonas Meinerzhagen',
    author_email='tim@meinerzhagen.me',
    license='MIT',
    license_files = ('LICENSE'),
    classifiers=[
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        "License :: OSI Approved :: MIT License",
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=1.0',
        'jinja2'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'external-link-marker = mkdocs_external-link-marker_plugin.plugin:ExternalLinkMarkerPlugin'
        ]
    }
)