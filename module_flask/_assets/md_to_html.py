"""
# markdown - Convert Markdown text to HTML - Python code example - Kite
# https://kite.com/python/examples/2545/markdown-convert-markdown-text-to-html
"""
print(__doc__)

import markdown

md = markdown.Markdown()

filename = 'index.md'

with open(filename, mode='r', encoding='utf8') as f:
    contents = f.readlines()
    



converts = [
        md.convert("# sample heading text"),
        md.convert("[sample link text](kite.com)"),
        md.convert("**sample bold text**"),
    ]


for conv in converts:
    print(conv)
