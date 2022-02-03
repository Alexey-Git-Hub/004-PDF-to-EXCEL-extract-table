# ------------------------------------------------------------------------
# Extracting tables from PDF
#
# Made by Alexey Loik
# ------------------------------------------------------------------------


# https://www.thepythoncode.com/article/extract-pdf-tables-in-python-camelot

file = "table.pdf"

import camelot


def run():
    # tables = camelot.read_pdf(file)
    tables = camelot.read_pdf(file, backend="poppler")
    print("Total tables extracted:", tables.n)

    print(tables[0].df)

    # tables[0].to_csv("foo.csv")

    tables[0].to_excel("foo.xlsx")


if __name__ == '__main__':
    run()

