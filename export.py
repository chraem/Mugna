from os import path, getcwd

from openpyxl.utils import get_column_letter
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment, Fill, PatternFill
# print(emp, employee_data)
# 0 (1, 'q', 'q', 'q', 1.0, 1.0, 1.0, 1.0, 1.0, 11.0, 1.0, 1.0, 1.0, 11.0, 1.0, 1.0, 14.0, '', 14.0)

def generate_stub(company_name, employees, prepared_by, ws):
    for emp, employee_data in enumerate(employees):
        col_per_stub= 11
        row_per_stub= 22

        # Outsets
        x_onset= emp % 2 * col_per_stub + 1
        y_onset= emp // 2 * row_per_stub + 1

        # Simulation of X Onset Computation # Simulation of Y Onset Computation
        # emp # %2 # *11 # + 1              # emp # //2 # *11 # + 1
        #  0  # 0  #  0  #  1               #  0  #  0  #  0  #  1
        #  1  # 1  #  11 #  12              #  1  #  0  #  0  #  1
        #  2  # 0  #  0  #  1               #  2  #  1  #  11 #  12
        #  3  # 1  #  11 #  12              #  3  #  1  #  11 #  12
        #  4  # 0  #  0  #  1               #  4  #  2  #  22 #  23

        x= [get_column_letter(x_onset + i) for i in range(col_per_stub)]
        x.insert(0,'-')
        # 0, A, B, C, D, E, F, G, H, I, J, K
        # 0, L, M, N, O, P, Q, R, S, T, U, V
        y= [str(row_number) for row_number in range(y_onset, row_per_stub + y_onset)]
        y.insert(0,'-')
        
        # emp # y_onset # row_per_stub + y_onset # row_number
        #  0  # 1       # 22 + 1                 # 1, 2, 3, 4, ..., 23
        #  1  # 1       # 22 + 1                 # 1, 2, 3, 4, ..., 23
        #  2  # 12      # 22 + 12                # 12, 13, 14, 15, ..., 34
        #  3  # 12      # 22 + 12                # 12, 13, 14, 15, ..., 34
        #  4  # 23      # 22 + 23                # 23, 24, 25, ..., 45

        # Font
        ANB18= Font(name="Arial Narrow", size=18, bold=True)
        ANB12= Font(name="Arial Narrow", size=12, bold=True)
        ANN12= Font(name="Arial Narrow", size=12, bold=False)

        # Fill Color
        fill1= PatternFill(fill_type="solid", start_color="FFF2CC")
        fill2= PatternFill(fill_type="solid", start_color="FFE699")

        # Border Style
        TDDD = Side(border_style = "thin", style="dashDotDot")
        #medium = Side()


        # Stub Labels
        ws[x[2]+y[2]]= company_name;                               ws[x[2]+y[2]].font= ANB18

        ws[x[2]+y[4]]= "Employee ID";                              ws[x[2]+y[4]].font= ANB12
        ws[x[9]+y[4]]= "Period: ";                                 ws[x[9]+y[4]].font= ANN12

        ws[x[2]+y[6]]= "First Name";                               ws[x[2]+y[6]].font= ANN12
        ws[x[5]+y[6]]= "Middle Name";                              ws[x[5]+y[6]].font= ANN12
        ws[x[8]+y[6]]= "Last Name";                                ws[x[8]+y[6]].font= ANN12

        ws[x[2]+y[8]]= "Day Shift Hourly Rate";                    ws[x[2]+y[8]].font= ANN12
        ws[x[5]+y[8]]= "Hour(s) Worked";                           ws[x[5]+y[8]].font= ANN12
        ws[x[8]+y[8]]= "Total Day Shift Pay";                      ws[x[8]+y[8]].font= ANN12

        ws[x[2]+y[9]]= "Night Shift Hourly Rate";                  ws[x[2]+y[9]].font= ANN12
        ws[x[5]+y[9]]= "Hour(s) Worked";                           ws[x[5]+y[9]].font= ANN12
        ws[x[8]+y[9]]= "Total Night Shift Pay";                    ws[x[8]+y[9]].font= ANN12

        ws[x[2]+y[10]]= "Holiday Hourly Rate";                     ws[x[2]+y[10]].font= ANN12
        ws[x[5]+y[10]]= "Hour(s) Worked";                          ws[x[5]+y[10]].font= ANN12
        ws[x[8]+y[10]]= "Total Holiday Pay";                       ws[x[8]+y[10]].font= ANN12

        ws[x[2]+y[11]]= "Overtime Hourly Rate";                    ws[x[2]+y[11]].font= ANN12
        ws[x[5]+y[11]]= "Hour(s) Worked";                          ws[x[5]+y[11]].font= ANN12
        ws[x[8]+y[11]]= "Total Overtime Pay";                      ws[x[8]+y[11]].font= ANN12

        ws[x[2]+y[13]]= "Deduction";                               ws[x[2]+y[13]].font= ANB12
        ws[x[3]+y[13]]= "Amount";                                  ws[x[2]+y[14]].font= ANB12

        ws[x[5]+y[13]]= "Gross Pay";                               ws[x[5]+y[13]].font= ANB12
        ws[x[5]+y[14]]= "Total Deduction";                         ws[x[5]+y[13]].font= ANB12
        ws[x[8]+y[13]]= "Net Pay";                                 ws[x[8]+y[13]].font= ANB12

        ws[x[5]+y[13]]= "Received by ";                            ws[x[5]+y[13]].font= ANB12        
        ws[x[8]+y[13]]= "Prepared by "+prepared_by;                ws[x[8]+y[13]].font= ANB12

        # Fills
        for col in range(x_onset+1, col_per_stub-1):
            ws[x[col]+y[8]].fill = fill1
            ws[x[col]+y[10]].fill = fill1

        for col in range(x_onset+1, col_per_stub-7):
            ws[x[col]+y[13]].fill = fill1

        for col in range(x_onset+4, col_per_stub-4):
            ws[x[col]+y[13]].fill = fill1
            ws[x[col]+y[14]].fill = fill1

        for col in range(col_per_stub-2, col_per_stub-1):
            ws[x[col]+y[13]].fill = fill2
            ws[x[col]+y[14]].fill = fill2

        # Borders



def save_wb(workbook, filename):
	workbook.save(path.normpath(getcwd()+"/mugna/exports/"+filename))
