(TeX-add-style-hook
 "test"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "xparse"
    "expl3")
   (LaTeX-add-xparse-macros
    '("\\NewDocumentCommand{\\splitstring}{m}" "splitstring" "m" "New")))
 :latex)

