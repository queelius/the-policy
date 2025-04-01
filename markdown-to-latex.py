#!/usr/bin/env python3
"""
Markdown to LaTeX Converter for Novel
This script converts a novel written in Markdown with LaTeX math to pure LaTeX format.
"""

import os
import re
import argparse
import subprocess
from pathlib import Path

def setup_argparse():
    parser = argparse.ArgumentParser(description='Convert Markdown novel to LaTeX')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('--output', '-o', help='Output LaTeX file')
    parser.add_argument('--template', '-t', help='LaTeX template file')
    parser.add_argument('--document-class', default='book', 
                      help='LaTeX document class (default: book)')
    parser.add_argument('--author', help='Author name for the title page')
    parser.add_argument('--title', help='Title for the title page')
    return parser.parse_args()

def create_latex_template(args):
    """Create a basic LaTeX template for the novel."""
    template = f"""\\documentclass[12pt,oneside]{{ {args.document_class} }}

% Essential packages
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage{{amsmath,amssymb,amsfonts}}
\\usepackage{{graphicx}}
\\usepackage{{xcolor}}
\\usepackage{{microtype}}
\\usepackage{{booktabs}}
\\usepackage{{hyperref}}
\\usepackage{{geometry}}

% Set page margins
\\geometry{{
    paper=a4paper,
    inner=1.5in,
    outer=1in,
    top=1in,
    bottom=1in,
    bindingoffset=.5in
}}

% Typography enhancements
\\usepackage{{lmodern}}  % Latin Modern font
\\usepackage{{setspace}}
\\onehalfspacing

% Chapter and section formatting
\\usepackage{{titlesec}}
\\titleformat{{\\chapter}}[display]
    {{\\normalfont\\huge\\bfseries}}{{\\chaptertitlename\\ \\thechapter}}{{20pt}}{{\\Huge}}
\\titlespacing*{{\\chapter}}{{0pt}}{{50pt}}{{40pt}}

% Header and footer
\\usepackage{{fancyhdr}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[LE,RO]{{\\thepage}}
\\fancyhead[RE]{{\\textit{{\\leftmark}}}}
\\fancyhead[LO]{{\\textit{{\\rightmark}}}}
\\renewcommand{{\\headrulewidth}}{{0.4pt}}
\\renewcommand{{\\footrulewidth}}{{0pt}}

% Title information
\\title{{{args.title if args.title else 'Novel Title'}}}
\\author{{{args.author if args.author else 'Author Name'}}}
\\date{{\\today}}

\\begin{{document}}

\\frontmatter
\\maketitle
\\tableofcontents
\\clearpage

\\mainmatter

% Your chapters will be inserted here

\\backmatter
% Bibliography, appendices, etc.

\\end{{document}}
"""
    return template

def convert_with_pandoc(input_file, output_file, template_file=None):
    """
    Convert Markdown to LaTeX using pandoc.
    If template_file is provided, it will be used as a template.
    """
    cmd = ['pandoc', input_file, '-f', 'markdown', '-t', 'latex', '-o', output_file]
    
    if template_file:
        cmd.extend(['--template', template_file])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error during pandoc conversion: {result.stderr}")
        return False
    
    print(f"Successfully converted {input_file} to {output_file}")
    return True

def post_process_latex(latex_file):
    """
    Perform additional processing on the generated LaTeX file.
    - Fix any issues with math environments
    - Enhance chapter/section styling
    - Any other custom modifications
    """
    with open(latex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix potential issues with math environments
    # (Sometimes pandoc doesn't handle certain math expressions correctly)
    content = re.sub(r'\\begin{align}\s*\\begin{aligned}', r'\\begin{align}', content)
    content = re.sub(r'\\end{aligned}\s*\\end{align}', r'\\end{align}', content)
    
    # Add any other custom modifications here
    
    with open(latex_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Post-processed {latex_file}")

def main():
    args = setup_argparse()
    
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found")
        return
    
    # Determine output filename if not specified
    output_file = args.output if args.output else input_path.with_suffix('.tex')
    
    # Create LaTeX template if needed
    if not args.template:
        template_file = input_path.with_name(f"{input_path.stem}_template.tex")
        with open(template_file, 'w', encoding='utf-8') as f:
            f.write(create_latex_template(args))
        print(f"Created LaTeX template: {template_file}")
    else:
        template_file = args.template
    
    # Convert the Markdown to LaTeX
    if convert_with_pandoc(str(input_path), str(output_file), str(template_file)):
        # Perform post-processing
        post_process_latex(output_file)
        print(f"\nConversion complete! Your LaTeX file is: {output_file}")
        print(f"You can compile it with: pdflatex {output_file}")

if __name__ == "__main__":
    main()