(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("revtex4-1" "aps" "rmp" "reprint" "amsmath" "amssymb" "graphicx" "longbibliography")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("threeparttablex" "para" "online" "flushleft") ("inputenc" "utf8")))
   (add-to-list 'LaTeX-verbatim-environments-local "semiverbatim")
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "../sections/introduction/introduction"
    "../sections/theory/theory"
    "../sections/method/method"
    "../sections/results/results"
    "revtex4-1"
    "revtex4-110"
    "bm"
    "graphicx"
    "epstopdf"
    "wrapfig"
    "array"
    "listings"
    "threeparttablex"
    "booktabs"
    "dcolumn"
    "color"
    "ifthen"
    "diagbox"
    "pifont"
    "wasysym"
    "amssymb"
    "caption"
    "subcaption"
    "listofitems"
    "tikz"
    "enumitem"
    "textpos"
    "multirow"
    "bigdelim"
    "float"
    "upgreek"
    "inputenc"
    "hyperref"
    "xcolor"
    "subfiles")
   (LaTeX-add-labels
    "eq:14")
   (LaTeX-add-bibliographies
    "References"))
 :latex)

