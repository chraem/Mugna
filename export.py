from os import path, getcwd


from openpyxl.utils import get_column_letter
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment, Fill, PatternFill

def generate_stub(company_name, employees, prepared_by):
	print(employees)

	for emp, empployee_data in enumerate(employees):
              print(emp, empployee_data)
              #0 (1, 'q', 'q', 'q', 1.0, 1.0, 1.0, 1.0, 1.0, 11.0, 1.0, 1.0, 1.0, 11.0, 1.0, 1.0, 14.0, '', 14.0)

def save_wb(workbook, filename):
	workbook.save(path.normpath(getcwd()+"/mugna/exports/"+filename))




