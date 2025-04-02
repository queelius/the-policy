#!/usr/bin/env python3
"""
Complete Markdown to LaTeX Converter
Converts markdown to a properly formatted LaTeX document with all necessary features.
"""

import os
import re
import argparse
import subprocess
from pathlib import Path
import tempfile

def setup_argparse():
    parser = argparse.ArgumentParser(description='Convert Markdown novel to LaTeX')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('--output', '-o', help='Output LaTeX file')
    parser.add_argument('--author', help='Author name for the title page')
    parser.add_argument('--title', help='Title for the title page')
    return parser.parse_args()

def extract_title_and_author(markdown_file):
    """Extract title and author from the Markdown file"""
    title = "Novel Title"
    author = "Author Name"
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to extract title from first heading
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
    
    # Try to extract author from a "By Author" line
    author_match = re.search(r'[Bb]y\s+([^\n]+)', content)
    if author_match:
        author = author_match.group(1)
    
    return title, author

def create_latex_document(body_text, title, author):
    """Create a complete LaTeX document with proper formatting"""
    latex_doc = f"""\\documentclass[12pt,oneside]{{book}}

% Essential packages
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage{{amsmath,amssymb,amsfonts}}
\\usepackage{{graphicx}}
\\usepackage{{xcolor}}
\\usepackage{{microtype}}
\\usepackage{{booktabs}}
\\usepackage{{wrapfig}}
\\usepackage{{caption}}
\\usepackage{{titlesec}}
\\usepackage{{fancyhdr}}
\\usepackage{{epigraph}}
\\usepackage{{tikz}}

% For code listings and syntax highlighting
\\usepackage{{fancyvrb}}
\\usepackage{{framed}}
\\usepackage{{listings}}

% Define Shaded environment for code blocks
\\definecolor{{shadecolor}}{{rgb}}{{0.95, 0.95, 0.95}}
\\newenvironment{{Shaded}}{{\\begin{{snugshade}}}}{{\\end{{snugshade}}}}
\\newenvironment{{Highlighting}}{{\\begin{{Shaded}}\\begin{{flushleft}}\\small\\ttfamily}}{{\\end{{flushleft}}\\end{{Shaded}}}}

% Define code highlighting commands
\\newcommand{{\\KeywordTok}}[1]{{\\textcolor[rgb]{{0.00,0.44,0.13}}{{\\textbf{{#1}}}}}}
\\newcommand{{\\StringTok}}[1]{{\\textcolor[rgb]{{0.25,0.44,0.63}}{{#1}}}}
\\newcommand{{\\CommentTok}}[1]{{\\textcolor[rgb]{{0.38,0.63,0.69}}{{\\textit{{#1}}}}}}
\\newcommand{{\\FunctionTok}}[1]{{\\textcolor[rgb]{{0.02,0.16,0.49}}{{#1}}}}
\\newcommand{{\\OperatorTok}}[1]{{\\textcolor[rgb]{{0.00,0.00,0.00}}{{#1}}}}
\\newcommand{{\\NumberTok}}[1]{{\\textcolor[rgb]{{0.00,0.00,1.00}}{{#1}}}}
\\newcommand{{\\VariableTok}}[1]{{\\textcolor[rgb]{{0.00,0.00,0.00}}{{#1}}}}
\\newcommand{{\\ControlFlowTok}}[1]{{\\textcolor[rgb]{{0.00,0.44,0.13}}{{\\textbf{{#1}}}}}}
\\newcommand{{\\ConstantTok}}[1]{{\\textcolor[rgb]{{0.53,0.00,0.00}}{{#1}}}}
\\newcommand{{\\CharTok}}[1]{{\\textcolor[rgb]{{0.25,0.44,0.63}}{{#1}}}}
\\newcommand{{\\SpecialCharTok}}[1]{{\\textcolor[rgb]{{0.25,0.44,0.63}}{{#1}}}}
\\newcommand{{\\PreprocessorTok}}[1]{{\\textcolor[rgb]{{0.74,0.48,0.00}}{{#1}}}}
\\newcommand{{\\NormalTok}}[1]{{#1}}
\\newcommand{{\\ImportTok}}[1]{{\\textcolor[rgb]{{0.00,0.44,0.13}}{{\\textbf{{#1}}}}}}
\\newcommand{{\\OtherTok}}[1]{{\\textcolor[rgb]{{0.25,0.44,0.63}}{{#1}}}}
\\newcommand{{\\AttributeTok}}[1]{{\\textcolor[rgb]{{0.49,0.56,0.16}}{{#1}}}}
\\newcommand{{\\DecValTok}}[1]{{\\textcolor[rgb]{{0.00,0.00,1.00}}{{#1}}}}

% Set page margins
\\usepackage{{geometry}}
\\geometry{{
    paper=a5paper,
    inner=0.75in,
    outer=0.5in,
    top=0.5in,
    bottom=0.5in,
    bindingoffset=0.25in,
    headheight=15pt  % Fix for fancyhdr warning
}}

% Fix for overfull boxes
\\setlength{{\\emergencystretch}}{{3em}}
\\tolerance=1000
\\hbadness=1500

% Typography enhancements
\\usepackage{{lmodern}}
\\usepackage{{setspace}}
\\onehalfspacing

% Fix for hyperref issues
\\usepackage{{hyperref}}
\\hypersetup{{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    filecolor=black,
    urlcolor=blue,
    pdftitle={{{title}}},
    pdfauthor={{{author}}},
    pdfproducer={{LaTeX}},
    pdfcreator={{Markdown to LaTeX Converter}}
}}

% Chapter styling
\\titleformat{{\\chapter}}[display]
    {{\\normalfont\\huge\\bfseries}}{{\\chaptertitlename\\ \\thechapter}}{{20pt}}{{\\Huge}}
\\titlespacing*{{\\chapter}}{{0pt}}{{50pt}}{{40pt}}

% Header and footer
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[LE,RO]{{\\thepage}}
\\fancyhead[RE]{{\\textit{{\\leftmark}}}}
\\fancyhead[LO]{{\\textit{{\\rightmark}}}}
\\renewcommand{{\\headrulewidth}}{{0.4pt}}
\\renewcommand{{\\footrulewidth}}{{0pt}}

% Chapter image command
\\newcommand{{\\chapterimage}}[4][l]{{%
  \\begin{{wrapfigure}}{{#1}}{{#3}}
    \\centering
    \\includegraphics[width=#3]{{#2}}
    \\ifx\\relax#4\\relax\\else
      \\caption{{#4}}
    \\fi
  \\end{{wrapfigure}}
}}

% Decorative chapter image
\\newcommand{{\\chaptersymbol}}[3][l]{{%
  \\begin{{wrapfigure}}{{#1}}{{#3}}
    \\centering
    \\includegraphics[width=#3]{{#2}}
    \\vspace{{-15pt}}
  \\end{{wrapfigure}}
}}

% Cover page command
\\newcommand{{\\coverpage}}[3]{{%
  \\clearpage
  \\thispagestyle{{empty}}
  \\begin{{tikzpicture}}[remember picture, overlay]
    % Full page background image
    \\node[inner sep=0pt] at (current page.center) {{
      \\includegraphics[width=\\paperwidth,height=\\paperheight]{{#1}}
    }};
    
    % Transparent overlay for better text readability
    \\fill[black, opacity=0.4] (current page.south west) rectangle (current page.north east);
    
    % Title 
    \\node[align=center, text width=0.8\\paperwidth] at (current page.center) {{
      \\fontsize{{30}}{{36}}\\selectfont\\color{{white}}\\textbf{{#2}}
    }};
    
    % Author name
    \\node[align=center, text width=0.8\\paperwidth, yshift=-3cm] at (current page.center) {{
      \\fontsize{{20}}{{24}}\\selectfont\\color{{white}}by #3
    }};
  \\end{{tikzpicture}}
  \\newpage
}}

% For epigraphs and quotations
\\usepackage{{epigraph}}
\\setlength\\epigraphwidth{{0.7\\textwidth}}
\\setlength\\epigraphrule{{0pt}}

% Title information
\\title{{{title}}}
\\author{{{author}}}
\\date{{\\today}}

\\begin{{document}}

% Uncomment to add a cover page
% \\coverpage{{images/cover.jpg}}{{{title}}}{{{author}}}

\\frontmatter
\\maketitle
\\tableofcontents
\\clearpage

\\mainmatter

% To add chapter images, use:
% \\chapterimage[r]{{images/chapter1.jpg}}{{0.4\\textwidth}}{{Caption}}
% Options: [l] for left, [r] for right placement

{body_text}

\\backmatter

\\end{{document}}
"""
    return latex_doc

def convert_markdown_to_latex_body(input_file):
    """
    Use pandoc to convert Markdown to LaTeX body content
    with proper handling of headings and code blocks
    """
    # Create temp file for output
    with tempfile.NamedTemporaryFile(suffix='.tex', delete=False) as temp:
        temp_filename = temp.name
    
    # Run pandoc to convert markdown to latex
    cmd = [
        'pandoc',
        input_file,
        '--from=markdown+tex_math_dollars+raw_tex',
        '--to=latex',
        '--top-level-division=chapter',
        '--wrap=none',
        '--highlight-style=tango',
        '--output=' + temp_filename
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error converting with pandoc: {result.stderr}")
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)
        return None
    
    # Read the converted content
    with open(temp_filename, 'r', encoding='utf-8') as f:
        latex_body = f.read()
    
    # Clean up
    os.unlink(temp_filename)
    
    # Fix issues with pandoc's output
    
    # 1. Remove hyperlink targets that cause issues and replace with labels
    latex_body = re.sub(
        r'\\hypertarget\{([^}]+)\}\s*\{\\chapter\s*\{([^}]+)\}\s*\}',
        r'\\chapter{\\label{\1}\2}',
        latex_body
    )
    
    latex_body = re.sub(
        r'\\hypertarget\{([^}]+)\}\s*\{\\section\s*\{([^}]+)\}\s*\}',
        r'\\section{\\label{\1}\2}',
        latex_body
    )
    
    latex_body = re.sub(
        r'\\hypertarget\{([^}]+)\}\s*\{\\subsection\s*\{([^}]+)\}\s*\}',
        r'\\subsection{\\label{\1}\2}',
        latex_body
    )
    
    # 2. Fix cross-references
    latex_body = re.sub(
        r'\\hyperlink\{([^}]+)\}\{([^}]+)\}',
        r'\\ref{\1}',
        latex_body
    )
    
    return latex_body

def main():
    args = setup_argparse()
    
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found")
        return
    
    # Determine output filename if not specified
    output_file = args.output if args.output else input_path.with_suffix('.tex')
    
    # Extract title and author from file or use command line args
    file_title, file_author = extract_title_and_author(args.input_file)
    title = args.title or file_title
    author = args.author or file_author
    
    print(f"Converting '{args.input_file}' to LaTeX...")
    print(f"Title: {title}")
    print(f"Author: {author}")
    
    # Convert markdown to latex body
    latex_body = convert_markdown_to_latex_body(args.input_file)
    if not latex_body:
        print("Conversion failed!")
        return
    
    # Create complete LaTeX document
    latex_document = create_latex_document(latex_body, title, author)
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_document)
    
    print(f"\nConversion complete! Your LaTeX file is: {output_file}")
    print(f"You can compile it with: pdflatex {output_file}")
    print("\nTips:")
    print("1. Create an 'images' folder for your cover and chapter images")
    print("2. Uncomment the \\coverpage line to add a cover")
    print("3. Add \\chapterimage commands after chapter headings")

if __name__ == "__main__":
    main()