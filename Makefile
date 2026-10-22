.PHONY: setup paper results clean check

setup:
	uv sync
	uv run python -m ipykernel install --user --name research-paper --display-name "Research Paper (.venv)"
	@echo "Setup complete. Select .venv as the Python interpreter, then run 'make paper'."

paper: results
	uv run python -c "from pathlib import Path; Path('build').mkdir(exist_ok=True)"
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build paper/main.tex
	biber build/main
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build paper/main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build paper/main.tex
	@echo "Built build/main.pdf"

results:
	uv run python scripts/build_results.py

check:
	uv run python -m compileall -q src scripts tests
	uv run python -m pytest

clean:
	rm -rf build
	rm -f outputs/figures/*.pdf outputs/tables/*.tex
