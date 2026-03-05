0. Download this repository.

One option is to download it as a Zip from [here](https://github.com/iangow/era_templates_pl/archive/refs/heads/main.zip).
If you downloaded as a Zip, unzip the contents to a directory on your computer where you want to keep the folder for your work with this book (this is the "working directory").
In the following steps it is assumed that you are using the terminal from the working directory.

1. Install `uv`.

On macOS or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Install Quarto CLI.

Install from [quarto.org](https://quarto.org/docs/get-started/).

3. Create/sync the project environment.

```bash
uv sync --python 3.13
```

4. Register the Jupyter kernel.

```bash
make kernel
```

5. Create a `.env` file in the working directory.

Example:

```env
WRDS_ID=your_wrds_username
DATA_DIR=/absolute/path/to/pq_data
```

6. Run the script in `update_wrds_pq.py` from the working directory.

```bash
uv run update_wrds_pq.py
```

7. Now you can use the templates in this repository.

I you have an IDE that can work with Quarto source files (`.qmd`), then you can use that.
Examples of such IDEs would be Positron, RStudio, or VS Code.

```bash
quarto render ffjr.qmd
```

An alternative would be Jupyter Lab.
You can convert the `.qmd` files to `ipynb` notebooks using `quarto convert`.

```bash
quarto convert ffjr.qmd  
```

You can then open the notebook using `jupyter lab`:

```bash
uv run jupyter lab ffjr.ipynb
```
