

import os
import sys
from typing import Generator
from generate_docs import unreal_engine_blocks
import yaml
import html

from Blueprint import Blueprint, BlueprintInput, BlueprintOutput
from Delegate import Delegate, DelegateInput, DelegateOutput
from read_header_file import parse_delegates

mkdocs_base_config = {
    'site_name': "UnrealFP",
    'extra_javascript': ['javascripts/klee.min.js'],
    'extra_css': ['stylesheets/unreal-fp.css'],
    'theme': {
        'name': 'material',
        'color_mode': 'dark',
        'include_sidebar': True
    },
    'markdown_extensions': ['md_in_html', 'pymdownx.extra'],
    'repo_url': 'https://gitlab.com/vaslabs/unrealfp'
    
}

generator_config = {
    'excluded_files': [
        'UnrealFunctionalProgramming.h',
        'UnrealFunctionalProgrammingBPLibrary.h'
    ],
    'readme': '../README.md'
}

def scan_directory(path: str) -> Generator[str, any, None]:
    for root, dirs, files in os.walk(path):
        for file in files:
            base_name = os.path.basename(file)
            if file.endswith(".h") and base_name not in generator_config['excluded_files']:
                yield os.path.join(root, file)


def generate_files(docs_directory: str, scanned_files):
    """
    Generate a markdown table of contents for markdown, with 
    the base name of each file as the title.
    """
    files_to_document = []
    nav_entries = []
    for file in scanned_files:
        files_to_document.append(file)
        base_name = _filename(file) # discard the format
        nav_entry = {base_name: f"{base_name}.md"}
        nav_entries.append(nav_entry)
    mkdocs_config = mkdocs_base_config.copy()
    mkdocs_config['nav'] = nav_entries

    with open(os.path.join(docs_directory, "mkdocs.yml"), "w") as f:
        yaml.dump(mkdocs_config, f)
    
    return files_to_document

def _filename(file: str):
    return  os.path.basename(file)[:-2].lower()

def generate_markdown_for_each_file(docs_directory: str, files_to_document):
    all_delegates = parse_all_delegates(files_to_document)
    for file in files_to_document:
        blocks = unreal_engine_blocks(file, all_delegates)
        markdown_file = os.path.join(f"{docs_directory}/docs", f"{_filename(file)}.md")
        with open(markdown_file, "w") as f:
            f.write(file_header(os.path.basename(file)[:-2]))
            for block in blocks:
                document_blueprint_metadata(block.blueprint, f)
                html = as_html(block.raw)
                f.write(html)
                f.writelines(["", ""])

def parse_all_delegates(files: list[str]) -> list[Delegate]:
    all_delegates = []
    for file in files:
        with open(file, "r") as f:
            delegates = parse_delegates(f.readlines())
            all_delegates.extend(delegates)
    return all_delegates

def file_header(file: str):
    return f"""# {file}\n\n"""

def as_html(block):
    return f"""
<div class="blueprint">
    <canvas class="klee" "data-klee-paste"="false">
        {html.escape(block)}
    </canvas>
</div>
    """

def document_blueprint_metadata(blueprint: Blueprint, f):
    f.write(f"\n### {blueprint.name}\n\n")
    f.write("\n<div markdown=\"1\">\n")

    f.write(f"<details markdown=\"1\">\n")
    f.write(f"<summary>Inputs</summary>\n\n")
    for input in blueprint.inputs:
        if (input.delegate):
            f.write(f"- **{input.name}** : {input.unreal_category}\n")
            write_delegate_details(input.delegate, f)
        else:
            f.write(f"- **{input.name}** : {input.unreal_container_type} {input.unreal_category}\n")
    f.write(f"\n</details>\n\n")
    f.write("\n</div>\n\n")
    write_outputs(blueprint.outputs, f)


def write_outputs(outputs: list[BlueprintOutput], f):
    f.write("\n<div markdown=\"1\">\n")

    f.write(f"<details markdown=\"1\">\n")
    f.write(f"<summary>Outputs</summary>\n\n")
    if not outputs:
        f.write("()\n")
    else:
        for output in outputs:
            f.write(f"- `{output.unreal_signature}`\n")
    f.write(f"\n</details>\n\n")
    f.write("\n</div>\n")


def write_inputs(inputs: list[BlueprintInput], f):
    f.write("\n<div markdown=\"1\">\n")

    f.write(f"<details markdown=\"1\">\n")
    f.write(f"<summary>Inputs</summary>\n\n")
    for input in inputs:
        if (input.delegate):
            f.write(f"- **{input.name}** : Delegate\n")
            write_delegate_details(input.delegate, f)
        else:
            f.write(f"- **{input.name}** : {input.unreal_signature}\n")
    f.write(f"\n</details>\n\n")
    f.write("\n</div>\n")

def write_delegate_details(delegate: Delegate, f):
    f.write(f"    - {delegate.name}: `{(format_inputs(delegate.inputs))} => {(format_outputs(delegate.outputs))}`\n")

def format_inputs(inputs: list[DelegateInput]):
    """ format inputs in the form of field_type, ..."""
    return ", ".join([f"{input.type}" for input in inputs])

def format_outputs(outputs: list[DelegateOutput]):
    """ format outputs in the form of field_type, ..."""
    if not outputs:
        return "()"
    return ", ".join([output.unreal_signature for output in outputs])

if __name__ == "__main__":
    scan_dir = sys.argv[1]
    docs_dir = sys.argv[2]

    scanned_files = scan_directory(scan_dir)
    files_to_document = generate_files(docs_dir, scanned_files)
    generate_markdown_for_each_file(docs_dir, files_to_document)
    
    # if readme is set copy it to the docs as index.md
    if 'readme' in generator_config:
        readme = generator_config['readme']
        with open(readme, "r") as f:
            readme_content = f.read()
        with open(os.path.join(docs_dir, "docs/index.md"), "w") as f:
            f.write(readme_content)