#!/usr/bin/env python3


"""
Simplistic pythonic PDF splitter.

This module has the function to split a PDF in two. It also 
contains helper functions to improve readability and reuse.
"""


from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path


def split_in_two(pdf_path, target_page_to_split_in_two):
    """Split a PDF in two. Uses input PDF folder as the output folder.

    Parameters:
        pdf_path (str): The PDF file path.

        target_page_to_split_in_two (int): The target page number where the split happens.

    Returns:
        A tuple containing the output PDFs location. The output location is the same as the input PDF folder.

    Raises:
        ValueError: When file validation fails.
    """
    

    pdf_path_obj = Path(pdf_path).resolve()

    if not pdf_path_obj.is_file():
        raise ValueError(f"File validation failed for input '{pdf_path}'.")

    pdf_instance = PdfFileReader(str(pdf_path_obj))

    pdf_path_first_split = f'{str(pdf_path_obj)} (1).pdf'
    pdf_path_second_split= f'{str(pdf_path_obj)} (2).pdf'
    _create_pdf(
        pdf_path_first_split,
        _set_pdf_writer(pdf_instance, range(target_page_to_split_in_two))
        )
    _create_pdf(
        pdf_path_second_split,
        _set_pdf_writer(pdf_instance, range(target_page_to_split_in_two, pdf_instance.getNumPages()))
        )

    return pdf_path_first_split, pdf_path_second_split


def _set_pdf_writer(pdf_reader_instance, page_range):
    """Set pdf_writer with the pages it needs."""

    pdf_writer = PdfFileWriter()
    for page in page_range:
        pdf_writer.addPage(pdf_reader_instance.getPage(page))

    return pdf_writer


def _create_pdf(pdf_path, pdf_writer):
    """Create output PDF."""

    with open(pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
