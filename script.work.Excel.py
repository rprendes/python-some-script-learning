#! python3
# bull_Excel.py - Number of breed and animals by breeds

import pandas as pd
from openpyxl import load_workbook
import pprint
import openpyxl

print('Opening workbook...')

# import excle file
#wb = openpyxl.load_workbook(filename="1000BullGenomesAnimalListDistRun7-TaurusRawRelease-20190521.xlsx")
# Import the excel file and call it xls_file
df = pd.ExcelFile("Excel-20190521.xlsx")
df
## count 
summary=df.Breed.value_counts()
#export 
summary.to_excel("test.xlsx")

workbook.save(filename="hello_world.xlsx")
