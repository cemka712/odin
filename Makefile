SHELL := /bin/bash


.PHONY: requirements
requirements: pyproject.toml
	uv lock
	uv sync
	uv sync --group dev

# --- QA ---

.PHONY: ruff
ruff: requirements
	uv run ruff check . $(ARGS)


.PHONY: run1
run1: requirements
	uv run python -m src.main