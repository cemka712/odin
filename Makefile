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


.PHONY: launch
launch: requirements
	uv run beg.py