import sys
import sqlite3
import os
import subprocess
import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PyQt5.QtCore import QRegExp
from PyQt5.uic import loadUi
from openpyxl import Workbook, load_workbook

from mugna import main_images_rc

deductions_DICT, visible = {}, False

class MainWindow(QMainWindow):
    """
        Contains all the essential functions for main window.
    """
    def  __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mugna/assets/mainWindow.ui", self)

        validate(self.id_emp_LE, "int")
        validate(self.fn_emp_LE, "name")
        validate(self.mn_emp_LE, "name")
        validate(self.ln_emp_LE, "name")
        validate(self.prepared_by_LE, "name")

        validate(self.day_rate_LE, "float")
        validate(self.night_rate_LE, "float")
        validate(self.ot_rate_LE, "float")
        validate(self.holiday_rate_LE, "float")

        validate(self.day_worked_LE, "float")
        validate(self.night_worked_LE, "float")
        validate(self.ot_hours_LE, "float")
        validate(self.holiday_worked_LE, "float")

        self.stacked_widget_page(0)
        self.report_TBL.setRowCount(0)
        self.calculator.setVisible(visible)

        self.new_BTN.clicked.connect(self.clear_data)
        self.add_BTN.clicked.connect(self.add_data)
        self.export_BTN.clicked.connect(self.export_data)         
        self.back_BTN.clicked.connect(lambda: self.stacked_widget_page(0))

        self.add_deduction_BTN.clicked.connect(self.add_row)
        self.remove_deduction_BTN.clicked.connect(self.remove_specific_row)
        self.report_BTN.clicked.connect(self.show_report)
        

        self.day_rate_LE.textChanged.connect(self.reload_total_day_pay)
        self.night_rate_LE.textChanged.connect(self.reload_total_night_pay)
        self.holiday_rate_LE.textChanged.connect(self.reload_total_holiday_pay)
        self.ot_rate_LE.textChanged.connect(self.reload_total_ot_pay)

        self.day_worked_LE.textChanged.connect(self.reload_total_day_pay)
        self.night_worked_LE.textChanged.connect(self.reload_total_night_pay)
        self.holiday_worked_LE.textChanged.connect(self.reload_total_holiday_pay)
        self.ot_hours_LE.textChanged.connect(self.reload_total_ot_pay)

        self.total_day_pay_LE.textChanged.connect(self.reload_gross_pay)
        self.total_night_pay_LE.textChanged.connect(self.reload_gross_pay)
        self.total_holiday_pay_LE.textChanged.connect(self.reload_gross_pay)
        self.total_ot_pay_LE.textChanged.connect(self.reload_gross_pay)

        self.gross_pay_LE.textChanged.connect(self.reload_net_pay)
        self.total_deduction_LE.textChanged.connect(self.reload_net_pay)
        self.deductions_TBL.itemChanged.connect(self.reload_total_deduction)

        self.open_calc_BTN.clicked.connect(self.calculator_visibility)

        self.show()

    def clear_data(self):
        """
        Clears all the line edits excluding the company name and prepared by line edits.
        """
        to_throw = [   self.id_emp_LE, self.fn_emp_LE, self.mn_emp_LE, self.ln_emp_LE,
                    self.gross_pay_LE, self.total_deduction_LE, self.net_pay_LE,
                    self.day_rate_LE, self.night_rate_LE, self.holiday_rate_LE,
                    self.ot_rate_LE, self.day_worked_LE, self.night_worked_LE,
                    self.holiday_worked_LE, self.ot_hours_LE, self.total_day_pay_LE,
                    self.total_night_pay_LE, self.total_holiday_pay_LE, self.total_ot_pay_LE,
                    self.gross_pay_LE, self.total_deduction_LE, self.net_pay_LE
                ]

        for i, throw in enumerate(to_throw):
            throw.clear()

        self.deductions_TBL.setRowCount(0)

    def add_data(self):
        """
        Reads all the data inputted in line edits and commits them on database.
        """
        global deductions_DICT

        try:
            employee_data ={
                "id": self.id_emp_LE.text(),

                "fn": self.fn_emp_LE.text(),
                "mn": self.mn_emp_LE.text(),
                "ln": self.ln_emp_LE.text(),

                "day_rate": self.day_rate_LE.text(),
                "night_rate": self.night_rate_LE.text(),
                "holiday_rate": self.holiday_rate_LE.text(),
                "ot_rate" :self.ot_rate_LE.text(),

                "day_worked": self.day_worked_LE.text(),
                "night_worked": self.night_worked_LE.text(),
                "holiday_worked": self.holiday_worked_LE.text(),
                "ot_hours": self.ot_hours_LE.text(),

                "total_day_pay": self.total_day_pay_LE.text(),
                "total_night_pay": self.total_night_pay_LE.text(),
                "total_holiday_pay": self.total_holiday_pay_LE.text(),
                "total_ot_pay": self.total_ot_pay_LE.text(),
                "gross_pay": self.gross_pay_LE.text(),
                "total_deduction": self.total_deduction_LE.text(),
                "net_pay": self.net_pay_LE.text()
                }

                # Get the inputs from table widget
            for row in range(self.deductions_TBL.rowCount()):
                deduction = self.deductions_TBL.item(row, 0).text()
                amount = self.deductions_TBL.item(row, 1).text()
                deductions_DICT[deduction] = amount

            if (c.execute("""
                            INSERT INTO employees(
                                id,
                                fn, mn, ln,
                                day_rate, night_rate, holiday_rate, ot_rate, 
                                day_worked, night_worked, holiday_worked, ot_hours,
                                total_day_pay, total_night_pay, total_holiday_pay, total_ot_pay, 
                                gross_pay, total_deduction, net_pay)
                            VALUES(
                                :id,
                                :fn, :mn, :ln,
                                :day_rate, :night_rate, :holiday_rate, :ot_rate, 
                                :day_worked, :night_worked, :holiday_worked, :ot_hours,
                                :total_day_pay, :total_night_pay, :total_holiday_pay, :total_ot_pay,
                                :gross_pay, :total_deduction, :net_pay
                                )
                            """, employee_data
            )):
                conn.commit()

            for deduction in deductions_DICT:
                if(c.execute("""
                                INSERT INTO deductions(id, deduction, amount)
                                VALUES(?, ?, ?)
                            """, (employee_data["id"], deduction, deductions_DICT[deduction],)
                )):
                    conn.commit()
        except:
            c.execute("SELECT id FROM employees WHERE id = :id LIMIT 1", employee_data)
            if c.fetchone():
                show_pop_up("ID: "+employee_data["id"]+" already exists!")
            elif self.id_emp_LE.text() == "":
                show_pop_up("ID field cannot be empty!")
            else:
                show_pop_up("An error occurred")

    def show_report(self):
        """
        Displays all the data in the database to table widget.
        """
        self.stacked_widget_page(1)
        self.report_TBL.resizeColumnsToContents()
        if c.execute("SELECT * FROM employees"):
            emps = c.fetchall()

            self.report_TBL.setRowCount(len(emps))

            for row, emp_in_row in enumerate(emps):
                for in_row, emp_data in enumerate(emp_in_row):
                    self.report_TBL.setItem(row, in_row, QTableWidgetItem(str(emp_in_row[in_row]) if str(emp_in_row[in_row]) != "" else "None"))

    def calculator_visibility(self):
        """
        Hides and show the calculator frame.
        """
        global visible

        if visible == False:
            self.calculator.setVisible(True); visible = True
            self.open_calc_BTN.setStyleSheet("""QPushButton{image: url(:/images/close.png);
                                                 background-color: rgb(5, 55, 66);
                                                 border-radius: 5px;
                                                 padding: 2px; padding-right:8px;}
                                                 QPushButton:hover{padding-right: 8px;}
                                              """)
        else:
            self.calculator.setVisible(False); visible = False
            self.open_calc_BTN.setStyleSheet("""QPushButton{image: url(:/images/open.png);
                                                 background-color: rgb(5, 55, 66);
                                                 border-radius: 5px;
                                                 padding: 2px; padding-right:8px;}
                                                 QPushButton:hover{padding-right: 8px;}
                                              """)

    def add_row(self):
        self.deductions_TBL.setRowCount(self.deductions_TBL.rowCount()+ 1)

    def remove_specific_row(self):
        self.deductions_TBL.removeRow(self.deductions_TBL.currentRow())

    def stacked_widget_page(self, page):
        if page == 0:
            self.emp_SW.setCurrentIndex(0)
            self.export_BTN.setVisible(False)
            self.back_BTN.setVisible(False)
            self.report_BTN.setVisible(True)
            self.add_BTN.setVisible(True)
            self.label_6.setVisible(True)
            self.prepared_by_LE.setVisible(True)
            self.prev_BTN.setVisible(True)
            self.next_BTN.setVisible(True)
            self.company_name_LBL.setVisible(True)
            self.company_name_LE.setVisible(True)
        else:
            self.emp_SW.setCurrentIndex(1)
            self.export_BTN.setVisible(True)
            self.back_BTN.setVisible(True)
            self.new_BTN.setVisible(False)
            self.add_BTN.setVisible(False)
            self.report_BTN.setVisible(False)
            self.label_6.setVisible(False)
            self.prepared_by_LE.setVisible(False)
            self.prev_BTN.setVisible(False)
            self.next_BTN.setVisible(False)
            self.company_name_LE.setVisible(False)
            self.company_name_LBL.setVisible(False)

    def reload_total_day_pay(self):
        """
        Updates the line edit for total day pay each time the line edits for day rate and worked changed.
        """
        day_rate = float(self.day_rate_LE.text()) if self.day_rate_LE.text() != "" else 0.0
        day_worked = float(self.day_worked_LE.text()) if self.day_worked_LE.text() != "" else 0.0
        self.total_day_pay_LE.setText(str(day_rate*day_worked))

    def reload_total_night_pay(self):
        """
        Updates the line edit for total night pay each time the line edits for night rate and worked changed.
        """
        night_rate = float(self.night_rate_LE.text()) if self.night_rate_LE.text() != "" else 0.0
        night_worked = float(self.night_worked_LE.text()) if self.night_worked_LE.text() != "" else 0.0
        self.total_night_pay_LE.setText(str(night_rate*night_worked))

    def reload_total_holiday_pay(self):
        """
        Updates the line edit for total holiday pay each time the line edits for holiday rate and worked changed.
        """
        holiday_rate = float(self.holiday_rate_LE.text()) if self.holiday_rate_LE.text() != "" else 0.0
        holiday_worked = float(self.holiday_worked_LE.text()) if self.holiday_worked_LE.text() != "" else 0.0
        self.total_holiday_pay_LE.setText(str(holiday_rate*holiday_worked))

    def reload_total_ot_pay(self):
        """
        Updates the line edit for total ot pay each time the line edits for ot rate and worked changed.
        """
        ot_rate = float(self.ot_rate_LE.text()) if self.ot_rate_LE.text() != "" else 0.0
        ot_worked = float(self.ot_hours_LE.text()) if self.ot_hours_LE.text() != "" else 0.0
        self.total_ot_pay_LE.setText(str(ot_rate*ot_worked))

    def reload_gross_pay(self):
        """
        Updates the line edit for gross pay each time the line edits for totals changed.
        """
        self.gross_pay_LE.setText(str(
              (float(self.total_day_pay_LE.text())     if self.total_day_pay_LE.text() != "" else 0.0)
            + (float(self.total_night_pay_LE.text())   if self.total_night_pay_LE.text() != "" else 0.0)
            + (float(self.total_holiday_pay_LE.text()) if self.total_holiday_pay_LE.text() != "" else 0.0)
            + (float(self.total_ot_pay_LE.text())      if self.total_ot_pay_LE.text() != "" else 0.0)
                                  ))

    def reload_total_deduction(self):
        """
        Updates the line edit for total deduction each time the deductionst table changed.
        """
        global deductions_DICT
        num_of_row, deductions = self.deductions_TBL.rowCount(), 0.0

        for row in range(num_of_row):
            pre_deduction = self.deductions_TBL.item(row, 0)
            pre_amount = self.deductions_TBL.item(row, 1)

            deduction = self.deductions_TBL.item(row, 0).text() if pre_deduction != None and pre_deduction.text() != "" else "Deduction"+str(row)
            amount =  self.deductions_TBL.item(row, 1).text() if pre_amount != None and pre_amount.text() else 0.0

            deductions_DICT[deduction] = amount
            deductions += float(deductions_DICT[deduction])

        self.total_deduction_LE.setText(str(deductions))

    def reload_net_pay(self):
        """
        Updates the line edit for total night pay each time the line edits for gross pay and total deduction changed.
        """
        self.net_pay_LE.setText(str(
            (float(self.gross_pay_LE.text()) if self.gross_pay_LE.text() != "" else 0.0)
            - (float(self.total_deduction_LE.text()) if self.total_deduction_LE.text() != "" else 0.0)
            ))

    def export_data(self):
        """
        Generates excel file
        """
        date_and_time = datetime.datetime.now().strftime("%m-%d-%Y(%I-%M-%S%p)")
        company_name = self.company_name_LE.text()
        prepared_by = self.prepared_by_LE.text()

        workbook = load_workbook(os.getcwd()+"mugna/basis.xlsx")
        worksheet = workbook.active

        if c.execute("SELECT * FROM employees"):
            employees = c.fetchall()

            for emp, empployee_data in enumerate(employees):
                # print(emp, empployee_data)
                # 0 (1, 'q', 'q', 'q', 1.0, 1.0, 1.0, 1.0, 1.0, 11.0, 1.0, 1.0, 1.0, 11.0, 1.0, 1.0, 14.0, '', 14.0)
                pass

        open_file_explorer()
        workbook.save(os.getcwd() + "/exports/"+date_and_time+"-Payroll Stub.xlsx")

def validate(line_edit: str, data_type: str):
    if data_type == "int":
        line_edit.setValidator(QIntValidator())
    elif data_type == "float":
        line_edit.setValidator(QDoubleValidator(decimals=2))
    elif data_type == "name":
        line_edit.setValidator(QRegExpValidator(QRegExp("[\\w\\s'.]+"), line_edit))

def show_pop_up(message: str):
    pop_up = QMessageBox()
    pop_up.setWindowTitle("Warning")
    pop_up.setText(message)
    pop_up.setIcon(QMessageBox.Warning)
    pop_up.setStandardButtons(QMessageBox.Ok)
    pop_up.exec_()

def open_file_explorer():
    if (subprocess.run([
        os.path.normpath(os.path.join(os.getenv('WINDIR'), 'explorer.exe')),
        os.path.join(os.getcwd(), 'exports')
        ])):
        pass
    else:
        show_pop_up("Failed to load File Explorer. File is saved as ", "in " + os.getcwd() +"/exports")


def close_db():
    conn.close()


conn = sqlite3.connect("mugna/database/stub.sqlite")
c = conn.cursor()
c.execute("DELETE FROM employees")
c.execute("DELETE FROM deductions")

# App initialization
app = QApplication(sys.argv)
app.aboutToQuit.connect(close_db)
mainWindow = MainWindow()
sys.exit(app.exec_())
