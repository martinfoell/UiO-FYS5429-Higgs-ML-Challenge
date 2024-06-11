(TeX-add-style-hook
 "method"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("subfiles" "../../main/main.tex")))
   (TeX-run-style-hooks
    "latex2e"
    "subfiles"
    "subfiles10")
   (TeX-add-symbols
    "makelabel")
   (LaTeX-add-labels
    "tab:acronyms"))
 :latex)

