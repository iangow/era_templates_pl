.PHONY: kernel

kernel:
	./.venv/bin/python -m ipykernel install --user --name era_templates_pl --display-name "Python (.venv) era_templates_pl"
