(TeX-add-style-hook
 "read"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "catchfile"
    "etoolbox")
   (TeX-add-symbols
    '("splitlines" 1)))
 :latex)

