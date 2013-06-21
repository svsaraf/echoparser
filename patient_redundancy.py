from tempfile import TemporaryFile
from xlwt import Workbook
from time import localtime, strftime
import os
import sys
from xlrd import *
import re
import odict
import pdb

def setupcancer(inputdictionary):
	book = Workbook(encoding='utf-8')
	sheet = book.add_sheet("Filtered Output")
	inputbook = open_workbook('dataset.xls', formatting_info=True)
	inputsheet = inputbook.sheet_by_index(0)
	locationsheetx = 1
	locationsheety = 1
	for row_index in range(inputsheet.nrows):
		if (row_index > 0):
			if inputsheet.cell(row_index,0).value in inputdictionary:
				print ""
			else:
				if inputsheet.cell(row_index,10).value == 'Y':
					for col_index in range(inputsheet.ncols):
						sheet.write(locationsheetx, locationsheety, inputsheet.cell(row_index,col_index).value)
						inputdictionary[inputsheet.cell(row_index,0).value] = ''
						locationsheety += 1
					locationsheety = 1
					locationsheetx+=1

	for row_index2 in range(inputsheet.nrows):
		if (row_index2 > 0):
			if inputsheet.cell(row_index2,0).value in inputdictionary:
				print ""
			else:
				for col_index2 in range(inputsheet.ncols):
					sheet.write(locationsheetx, locationsheety, inputsheet.cell(row_index2,col_index2).value)
					inputdictionary[inputsheet.cell(row_index2,0).value] = ''
					locationsheety +=1
				locationsheety = 1
				locationsheetx += 1

	book.save("output_dataset" + ".xls")
	return inputdictionary

total = len(sys.argv)
print "HELLO"
inputdictionary = {}
inputdictionary = setupcancer(inputdictionary)
print len(inputdictionary)
print "Done"

