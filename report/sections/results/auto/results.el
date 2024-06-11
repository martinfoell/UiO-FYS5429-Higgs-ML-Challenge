(TeX-add-style-hook
 "results"
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
   (TeX-add-symbols
    '("captionDatasetZ" 1)
    '("captionDataset" 1)
    "FillMean"
    "FillZero"
    "FillPhiRandom"
    "RemoveJets"
    "RemovePhi"
    "JetsNone"
    "JetsOne"
    "JetsTwo"
    "captionAcc"
    "captionLoss"
    "captionROC"
    "captionBkgSig"
    "captionLik")
   (LaTeX-add-labels
    "sec:results"
    "sec:fillmean-dataset"
    "fig:FillMean_acc"
    "fig:FillMean_loss"
    "fig:FillMean_roc"
    "fig:FillMean_1"
    "fig:FillMean_bkg_sig"
    "fig:FillMean_likelihood"
    "fig:FillMean_Z"
    "sec:fillzero"
    "fig:FillZero_acc"
    "fig:FillZero_loss"
    "fig:FillZero_roc"
    "fig:FillZero_1"
    "fig:FillZero_bkg_sig"
    "fig:FillZero_likelihood"
    "fig:FillZero_Z"
    "fig:FillPhiRandom_acc"
    "fig:FillPhiRandom_loss"
    "fig:FillPhiRandom_roc"
    "fig:FillPhiRandom_1"
    "fig:FillPhiRandom_bkg_sig"
    "fig:FillPhiRandom_likelihood"
    "fig:FillPhiRandom_Z"
    "sec:removephi"
    "fig:RemovePhi_acc"
    "fig:RemovePhi_loss"
    "fig:RemovePhi_roc"
    "fig:RemovePhi_1"
    "fig:RemovePhi_bkg_sig"
    "fig:RemovePhi_likelihood"
    "fig:RemovePhi_Z"
    "fig:RemoveJets_acc"
    "fig:RemoveJets_loss"
    "fig:RemoveJets_roc"
    "fig:RemoveJets_1"
    "fig:RemoveJets_bkg_sig"
    "fig:RemoveJets_likelihood"
    "fig:RemoveJets_Z"
    "fig:JetsNone_acc"
    "fig:JetsNone_loss"
    "fig:JetsNone_roc"
    "fig:JetsNone_1"
    "fig:JetsNone_bkg_sig"
    "fig:JetsNone_likelihood"
    "fig:JetsNone_Z"
    "fig:JetsOne_acc"
    "fig:JetsOne_loss"
    "fig:JetsOne_roc"
    "fig:JetsOne_1"
    "fig:JetsOne_bkg_sig"
    "fig:JetsOne_likelihood"
    "fig:JetsOne_Z"
    "fig:JetsTwo_acc"
    "fig:JetsTwo_loss"
    "fig:JetsTwo_roc"
    "fig:JetsTwo_1"
    "fig:JetsTwo_bkg_sig"
    "fig:JetsTwo_likelihood"
    "fig:JetsTwo_Z"
    "tab:acronyms"
    "sec:conclusion"
    "sec:appendix"
    "fig:sub1"
    "fig:sub2"
    "fig:sub3"
    "fig:sub4"
    "fig:main"))
 :latex)

