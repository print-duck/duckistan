# Importing modules
import csv
from xlsxwriter.workbook import Workbook

# Input file path
tsv_file = 'data.tsv'
# Output file path
xlsx_file = 'imdb.xlsx'

# Creating an XlsxWriter workbook object and adding
# a worksheet.
workbook = Workbook(xlsx_file)
worksheet = workbook.add_worksheet()

# Reading the tsv file.
read_tsv = csv.reader(open(tsv_file, 'r', encoding='utf-8'), delimiter='\t')

# We'll use a loop with enumerate to pass the data
# together with its row position number, which we'll
# use as the cell number in the write_row() function.
for row, data in enumerate(read_tsv):
	worksheet.write_row(row, 0, data)

# Closing the xlsx file.
workbook.close()
