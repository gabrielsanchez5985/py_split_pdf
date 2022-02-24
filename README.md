# py_split_pdf

**py_split_pdf** is a helper function to help you split PDFs in two.

*Powered by [PyPDF2](https://pypi.org/project/PyPDF2/).*

## Architecture

`py_split_pdf.py`  
This module contains the function that splits the PDF in two.

`py_split_pdf_cli.py`  
This module is the CLI to use the split function.

## Usage

**Before you begin**

- Make sure you have Python 3.8 or up installed. 
- **On Windows**, add `python` to `PATH`. Then, use `python` instead of `python3` in your terminal.
- Recommended: Create a [Python virtual environment](https://docs.python.org/3/library/venv.html).

**Procedure**

1. Download or clone this repo.
2. Open your terminal and navigate to the repo's folder.
3. Run `pip install -r requirements.txt` on your terminal.
4. Run: 

    ```bash
    python3 py_split_pdf_cli.py [-h] pdf_path page_number
    ```

    **Positional arguments:**

    `pdf_path`  
        The path to the PDF you want to split.

    `page_number`  
        The page number where the PDF will be split into two

    **Optional arguments:**

    `-h`, `--help`  
        Show help message and exit.

    - Optional for Linux: You can modify the file to be executable using `chmod +x py_split_pdf_cli.py` and run `./py_split_pdf_cli.py [-h] pdf_path page_number`.

**Optional usage for Windows users**

You can create an executable using Python libraries like [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/).

## Contributing

You can contribute by openning issues or sending Pull Requests (PRs).

If you open an issue, make sure to be as clear and descriptive as you can. If you open a PR, its approval depends on what you are changing. Make sure to be descriptive in PRs too.
