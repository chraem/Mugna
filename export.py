from os import path, getcwd


from openpyxl.utils import get_column_letter
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment, Fill, PatternFill

def generate_stub(company_name, employees, prepared_by):
	print(employees)

	for emp, employee_data in enumerate(employees):
        # print(emp, employee_data)
        # 0 (1, 'q', 'q', 'q', 1.0, 1.0, 1.0, 1.0, 1.0, 11.0, 1.0, 1.0, 1.0, 11.0, 1.0, 1.0, 14.0, '', 14.0)

        # Size
        col_per_stub = 11
        row_per_stub = 22

        # Offsets
        x_offset = emp % 2 * col_per_stub + 1
        y_offset = emp // 2 * row_per_stub + 1

        #Simulation of X Offset Computation
        # emp # %2 # *11 # + 1
        #  0  # 0  #  0  # 1
        #  1  # 1  #  11 # 12
        #  2  # 0  #  0  # 1
        #  3  # 1  #  11 # 12
        #  4  # 0  #  0  # 1

def save_wb(workbook, filename):
	workbook.save(path.normpath(getcwd()+"/mugna/exports/"+filename))




