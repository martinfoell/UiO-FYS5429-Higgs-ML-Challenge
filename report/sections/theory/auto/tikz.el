(TeX-add-style-hook
 "tikz"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "border=3pt" "tikz")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("contour" "outline")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "amsmath"
    "listofitems"
    "contour"
    "xcolor")
   (TeX-add-symbols
    '("setAngles" 3)
    "NC"
    "nstyle"
    "lay"
    "NI"
    "NO"
    "yshift"
    "agr"))
 :latex)

