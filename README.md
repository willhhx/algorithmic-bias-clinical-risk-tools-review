# When the number is not neutral: bias in clinical risk prediction tools

Narrative literature review prepared for the Emory University Journal of Public Health (Literature Review).

## Contents
- `latex/manuscript.tex`, `latex/manuscript.pdf`: the review
- `data/extracted_figures.csv`: every figure used, with source, DOI, and where it was found
- `outputs/results.json`, `results.csv`: derived numbers (ratios, differences)
- `outputs/figure1_clinical_algorithm_bias.png`: Figure 1 (300 dpi)
- `verification.md`: citation checks, figure traceability, known issues, word count

## Reproduce
```
python3 analysis.py
python3 build_paper.py        # needs pdflatex
python3 build_verification.py
```
Needs pandas and matplotlib.

## Notes
Figures were read from article abstracts or full texts; see verification.md for what was read for each source and items to check by hand (notably a correction notice for the Sjoding letter).
