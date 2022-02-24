#!/usr/bin/env python3


"""CLI entry-point for module."""


from py_split_pdf import split_in_two
import argparse


def main():
    """The main function."""
    
    DESCRIPTION = """Split PDF in two.
    
    py_split_pdf_cli is a pythonic CLI app to split PDFs in two.
    """

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("pdf_path", 
                        metavar="pdf_path",
                        type=str, 
                        help="the path to the PDF you want to split")
    parser.add_argument("page_num", 
                        metavar="page_number",
                        type=int,
                        help="the page number where the PDF will be split into two")

    args = parser.parse_args()
    first_pdf_part_path, second_pdf_part_path = split_in_two(args.pdf_path, args.page_num)

    print(first_pdf_part_path + "\n" + second_pdf_part_path)

if __name__ == "__main__":
    main()

