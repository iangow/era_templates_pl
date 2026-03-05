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

5. Create a `.env` file.

Example:

```env
WRDS_ID=your_wrds_username
DATA_DIR=/absolute/path/to/pq_data
```

6. Run the script in `update_wrds_pq.py.

```bash
uv run update_wrds_pq.py
```

7. Now you can use the templates in this repository.

```
quarto render ffjr.qmd
```
