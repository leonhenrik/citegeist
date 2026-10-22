.PHONY: setup paper results clean check

setup:
	uv sync
	uv run python -m ipykernel install --user --name research-paper --display-name "Research Paper (.venv)"
	@echo "Setup complete. Select .venv as the Python interpreter, then run 'make paper'."

paper: results
	mkdir -p build
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build paper/main.tex
	@echo "Built build/paper.pdf"

results:
	uv run python scripts/build_results.py

check:
	uv run python -m compileall -q src scripts tests
	uv run python -m pytest

clean:
	rm -rf build
	rm -f outputs/figures/*.pdf outputs/tables/*.tex
