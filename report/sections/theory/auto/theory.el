(TeX-add-style-hook
 "theory"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("subfiles" "../../main/main.tex")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-environments-local "semiverbatim")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "subfiles"
    "subfiles10")
   (LaTeX-add-labels
    "sec:theory"
    "sec:neural-network"
    "eq:art-neurons"
    "fig:neuron"
    "eq:2"
    "eq:weighted-sum"
    "eq:6"
    "eq:layer-output"
    "eq:layer-output-l"
    "eq:uptate-weight"
    "eq:uptate-bias"
    "sec:statistics"
    "eq:discover-sig"
    "eq:profile-likelihood-ratio"
    "eq:wilks-test"
    "eq:discovery-likelihood-ratio"
    "eq:discovery-likelihood-ratio-s-b"
    "eq:discovery-likelihood-ratio-mu"
    "eq:relation-likelihood"
    "eq:relation-likelihood-approx"
    "eq:5"
    "eq:discovery-sig-likelihood"
    "sec:likel-estim"
    "eq:likilhood-loss"
    "eq:min-likelihood-loss"
    "eq:min-likelihood-conditon"
    "eq:likelihood-condition-1"
    "eq:likelihood-condition-stright"
    "eq:likelihood-rhp"
    "eq:4"
    "eq:1"
    "eq:7"
    "eq:likelihood-loss-2"
    "eq:9"
    "sec:estim-prof-log"))
 :latex)

