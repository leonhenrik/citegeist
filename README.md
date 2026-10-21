# VS Code Research Paper Template

Local-first research workflow: Python, Jupyter, native LaTeX, BibLaTeX/Biber, Zotero + Better BibTeX, Git, and Make.

## Prerequisites
Install Git, Python 3.12, `uv`, GNU Make, VS Code, Zotero + Better BibTeX, and a TeX distribution providing `latexmk`, `pdflatex`, and `biber`. On Windows, WSL is the most straightforward Make-based setup.

## First run
1. Open this folder in VS Code.
2. Run `uv sync`.
3. Run `uv run python -m ipykernel install --user --name research-paper --display-name "Research Paper (.venv)"`.
4. Select `.venv` as the Python interpreter and the named kernel for notebooks.
5. Run `make paper`.
6. Open `build/paper.pdf`.

## Project map
- `data/raw/`: original inputs; ignored by Git except for its README.
- `data/processed/`: derived datasets, generated locally.
- `notebooks/`: exploration and diagnostics.
- `src/research/`: reusable analysis functions.
- `scripts/build_results.py`: reproducible manuscript-artifact generation.
- `outputs/figures/`, `outputs/tables/`: generated files referenced by LaTeX.
- `paper/main.tex`: native LaTeX manuscript.
- `refs/references.bib`: Better BibLaTeX export destination.
- `build/`: PDF and LaTeX auxiliary files, ignored by Git.

## Zotero + Better BibTeX
1. Install Better BibTeX: https://retorque.re/zotero-better-bibtex/installation/
2. Create a Zotero collection for the paper.
3. Right-click it and choose **Export Collection**.
4. Choose **Better BibLaTeX**, because this project uses `biblatex` + Biber.
5. Enable **Keep updated** and save to `refs/references.bib`.
6. Cite entries using the generated keys, e.g. `\parencite{smith2024causal}`.
7. Keep Zotero running for auto-export. Run `make paper` after references change.

The included `.bib` has a demo entry so the template compiles before Zotero setup. Replace it with the auto-export. Do not manually edit a file managed by Better BibTeX because Zotero may overwrite it. Commit the exported bibliography if you need historical builds to remain reproducible.

## Commands
- `make paper`: regenerate figures/tables and compile `build/paper.pdf`.
- `make results`: regenerate figures/tables only.
- `make check`: basic Python syntax and tests.
- `make clean`: remove generated files.

## Reproducibility
`uv.lock` should be generated with `uv lock` and committed to pin resolved Python dependencies. TeX distribution versions are not pinned by uv, so record OS, TeX distribution/version, and journal class version for archival work. Document data provenance and access conditions. For large or restricted data, use suitable storage and do not commit secrets or confidential data.

## New paper
Copy this repository or use it as a template. Update title/author and manuscript sections, create a Zotero collection, add analysis to `src/research/`, and keep publication-critical code in scripts/modules rather than relying on notebook execution order.
