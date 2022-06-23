#!/usr/bin/env python3

# by Torben Menke https://entorb.net


import os
import re
import sys
import datetime as dt

os.chdir(os.path.dirname(sys.argv[0]) + "/..")

source_file = "hpmor-epub-2-flatten.tex"
target_file = "hpmor-epub-3-flatten-mod1.tex"

print("=== 3. modify flattened file ===")


with open(source_file, mode="r", encoding="utf-8", newline="\n") as fhIn:
    cont = fhIn.read()

# \today
date_str = dt.date.today().strftime("%d.%m.%Y")
cont = cont.replace("\\today{}", date_str)

# writtenNote env -> \writtenNoteA
cont = re.sub(
    r"\s*\\begin\{writtenNote\}\s*(.*?)\s*\\end\{writtenNote\}",
    r"\\writtenNoteA{\1}",
    cont,
    flags=re.DOTALL,
)

# some cleanup
cont = cont.replace("\\hplettrineextrapara", "")
# \vskip 1\baselineskip plus .5\textheight minus 1\baselineskip
cont = re.sub(
    r"\\vskip .*\\baselineskip",
    "",
    cont,
)

# fix „ at start of chapter
cont = cont.replace("\\lettrinepara[ante=„]", "„\\lettrinepara")

# align*
cont = cont.replace("\\begin{align*}", "")
cont = cont.replace("\\end{align*}", "")
cont = cont.replace("}&\\hbox{", "}\\hbox{")

with open(target_file, mode="w", encoding="utf-8", newline="\n") as fhOut:
    fhOut.write(cont)
