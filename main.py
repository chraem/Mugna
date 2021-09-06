import sys
import sqlite3
import subprocess
from datetime import datetime
from os import path, getenv, getcwd
from openpyxl import Workbook, load_workbook

from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide2.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PySide2.QtCore import QRegExp, QTimer

from mugna.assets import main_images_rc, ui_mainWindow
from export import generate_stub, save_wb

deductions_DICT, visible = {}, False

class MainWindow(QMainWindow):
    """
        Contains all the essential functions for main window.
    """
    def  __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        validate(self.ui.id_emp_LE, "int")
        validate(self.ui.fn_emp_LE, "name")
        validate(self.ui.mn_emp_LE, "name")
        validate(self.ui.ln_emp_LE, "name")
        validate(self.ui.prepared_by_LE, "name")

        validate(self.ui.day_rate_LE, "float")
        validate(self.ui.night_rate_LE, "float")
        validate(self.ui.ot_rate_LE, "float")
        validate(self.ui.holiday_rate_LE, "float")

        validate(self.ui.day_worked_LE, "float")
        validate(self.ui.night_worked_LE, "float")
        validate(self.ui.ot_hours_LE, "float")
        validate(self.ui.holiday_worked_LE, "float")

        validate(self.ui.period_LE, "date")

        self.stacked_widget_page(0)
        self.ui.report_TBL.setRowCount(0)
        self.ui.calculator.setVisible(visible)

        self.ui.clear_BTN.clicked.connect(self.clear_data)
        self.ui.add_BTN.clicked.connect(self.add_data)
        self.ui.export_BTN.clicked.connect(self.export_data)         
        self.ui.back_BTN.clicked.connect(lambda: self.stacked_widget_page(0))

        self.ui.add_deduction_BTN.clicked.connect(self.add_row)
        self.ui.remove_deduction_BTN.clicked.connect(self.remove_specific_row)
        self.ui.report_BTN.clicked.connect(self.show_report)
        

        self.ui.day_rate_LE.textChanged.connect(self.reload_total_day_pay)
        self.ui.night_rate_LE.textChanged.connect(self.reload_total_night_pay)
        self.ui.holiday_rate_LE.textChanged.connect(self.reload_total_holiday_pay)
        self.ui.ot_rate_LE.textChanged.connect(self.reload_total_ot_pay)

        self.ui.day_worked_LE.textChanged.connect(self.reload_total_day_pay)
        self.ui.night_worked_LE.textChanged.connect(self.reload_total_night_pay)
        self.ui.holiday_worked_LE.textChanged.connect(self.reload_total_holiday_pay)
        self.ui.ot_hours_LE.textChanged.connect(self.reload_total_ot_pay)

        self.ui.total_day_pay_LE.textChanged.connect(self.reload_gross_pay)
        self.ui.total_night_pay_LE.textChanged.connect(self.reload_gross_pay)
        self.ui.total_holiday_pay_LE.textChanged.connect(self.reload_gross_pay)
        self.ui.total_ot_pay_LE.textChanged.connect(self.reload_gross_pay)

        self.ui.gross_pay_LE.textChanged.connect(self.reload_net_pay)
        self.ui.total_deduction_LE.textChanged.connect(self.reload_net_pay)
        self.ui.deductions_TBL.itemChanged.connect(self.reload_total_deduction)

        self.ui.open_calc_BTN.clicked.connect(self.calculator_visibility)

        self.show()

    def clear_data(self):
        """
        Clears all the line edits excluding the company name and prepared by line edits.
        """
        to_throw = [self.ui.id_emp_LE, self.ui.fn_emp_LE, self.ui.mn_emp_LE, self.ui.ln_emp_LE,
                    self.ui.gross_pay_LE, self.ui.total_deduction_LE, self.ui.net_pay_LE,
                    self.ui.day_rate_LE, self.ui.night_rate_LE, self.ui.holiday_rate_LE,
                    self.ui.ot_rate_LE, self.ui.day_worked_LE, self.ui.night_worked_LE,
                    self.ui.holiday_worked_LE, self.ui.ot_hours_LE, self.ui.total_day_pay_LE,
                    self.ui.total_night_pay_LE, self.ui.total_holiday_pay_LE, self.ui.total_ot_pay_LE,
                    self.ui.gross_pay_LE, self.ui.total_deduction_LE, self.ui.net_pay_LE
                   ]

        for i, throw in enumerate(to_throw):
            throw.clear()

        self.ui.deductions_TBL.setRowCount(0)

    def add_data(self):
        """
        Reads all the data inputted in line edits and commits them on database.
        """
        global deductions_DICT

        try:
            employee_data ={
                "id": self.ui.id_emp_LE.text(),

                "fn": self.ui.fn_emp_LE.text(),
                "mn": self.ui.mn_emp_LE.text(),
                "ln": self.ui.ln_emp_LE.text(),

                "day_rate": self.ui.day_rate_LE.text(),
                "night_rate": self.ui.night_rate_LE.text(),
                "holiday_rate": self.ui.holiday_rate_LE.text(),
                "ot_rate" :self.ui.ot_rate_LE.text(),

                "day_worked": self.ui.day_worked_LE.text(),
                "night_worked": self.ui.night_worked_LE.text(),
                "holiday_worked": self.ui.holiday_worked_LE.text(),
                "ot_hours": self.ui.ot_hours_LE.text(),

                "total_day_pay": self.ui.total_day_pay_LE.text(),
                "total_night_pay": self.ui.total_night_pay_LE.text(),
                "total_holiday_pay": self.ui.total_holiday_pay_LE.text(),
                "total_ot_pay": self.ui.total_ot_pay_LE.text(),
                "gross_pay": self.ui.gross_pay_LE.text(),
                "total_deduction": self.ui.total_deduction_LE.text(),
                "net_pay": self.ui.net_pay_LE.text()
                }

            # Get inputs from table widget
            for row in range(self.ui.deductions_TBL.rowCount()):
                deduction = self.ui.deductions_TBL.item(row, 0).text()
                amount = self.ui.deductions_TBL.item(row, 1).text()
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

            self.ui.notification_LBL.setText("Added successfully.")
            self.ui.notification_LBL.setVisible(True)
            QTimer.singleShot(500, self.show_notification_LBL)
        except:
            c.execute("SELECT id FROM employees WHERE id = :id LIMIT 1", employee_data)
            if c.fetchone():
                show_pop_up("ID: "+employee_data["id"]+" already exists!")
            elif self.ui.id_emp_LE.text() == "":
                show_pop_up("ID field cannot be empty!")
            else:
                show_pop_up("An error occurred")

    def show_report(self):
        """
        Displays all the data in the database to table widget.
        """
        self.stacked_widget_page(1)
        self.ui.report_TBL.resizeColumnsToContents()
        if c.execute("SELECT * FROM employees"):
            emps = c.fetchall()

            self.ui.report_TBL.setRowCount(len(emps))

            for row, emp_in_row in enumerate(emps):
                for in_row, emp_data in enumerate(emp_in_row):
                    self.ui.report_TBL.setItem(row, in_row, QTableWidgetItem(str(emp_in_row[in_row]) if str(emp_in_row[in_row]) != "" else "None"))

    def calculator_visibility(self):
        """
        Hides and show the calculator frame.
        """
        global visible

        if visible == False:
            self.ui.calculator.setVisible(True); visible = True
            self.ui.open_calc_BTN.setStyleSheet("""QPushButton{image: url(:/images/close.png);
                                                 background-color: rgb(5, 55, 66);
                                                 border-radius: 5px;
                                                 padding: 2px; padding-right:8px;}
                                                 QPushButton:hover{padding-right: 8px;}
                                              """)
        else:
            self.ui.calculator.setVisible(False); visible = False
            self.ui.open_calc_BTN.setStyleSheet("""QPushButton{image: url(:/images/open.png);
                                                 background-color: rgb(5, 55, 66);
                                                 border-radius: 5px;
                                                 padding: 2px; padding-right:8px;}
                                                 QPushButton:hover{padding-right: 8px;}
                                              """)

    def add_row(self):
        self.ui.deductions_TBL.setRowCount(self.ui.deductions_TBL.rowCount() + 1)

        if self.ui.deductions_TBL.rowCount() > 7:
            show_pop_up("Exceeded maximum number of deductions.")
            self.ui.deductions_TBL.setRowCount(7)


    def remove_specific_row(self):
        self.ui.deductions_TBL.removeRow(self.ui.deductions_TBL.currentRow())

    def stacked_widget_page(self, page):
        if page == 0:
            self.ui.emp_SW.setCurrentIndex(0)
            self.ui.export_BTN.setVisible(False)
            self.ui.back_BTN.setVisible(False)
            self.ui.report_BTN.setVisible(True)
            self.ui.add_BTN.setVisible(True)
            self.ui.clear_BTN.setVisible(True)
            self.ui.label_6.setVisible(True)
            self.ui.prepared_by_LE.setVisible(True)
            self.ui.prev_BTN.setVisible(True)
            self.ui.next_BTN.setVisible(True)
            self.ui.company_name_LBL.setVisible(True)
            self.ui.company_name_LE.setVisible(True)
            self.ui.label_7.setVisible(True)
            self.ui.period_LE.setVisible(True)
        else:
            self.ui.emp_SW.setCurrentIndex(1)
            self.ui.export_BTN.setVisible(True)
            self.ui.back_BTN.setVisible(True)
            self.ui.clear_BTN.setVisible(False)
            self.ui.add_BTN.setVisible(False)
            self.ui.report_BTN.setVisible(False)
            self.ui.label_6.setVisible(False)
            self.ui.prepared_by_LE.setVisible(False)
            self.ui.prev_BTN.setVisible(False)
            self.ui.next_BTN.setVisible(False)
            self.ui.company_name_LE.setVisible(False)
            self.ui.company_name_LBL.setVisible(False)
            self.ui.label_7.setVisible(False)
            self.ui.period_LE.setVisible(False)

    def reload_total_day_pay(self):
        """
        Updates the line edit for total day pay each time the line edits for day rate and worked changed.
        """
        day_rate = float(self.ui.day_rate_LE.text()) if self.ui.day_rate_LE.text() != "" else 0.0
        day_worked = float(self.ui.day_worked_LE.text()) if self.ui.day_worked_LE.text() != "" else 0.0
        self.ui.total_day_pay_LE.setText(str(day_rate*day_worked))

    def reload_total_night_pay(self):
        """
        Updates the line edit for total night pay each time the line edits for night rate and worked changed.
        """
        night_rate = float(self.ui.night_rate_LE.text()) if self.ui.night_rate_LE.text() != "" else 0.0
        night_worked = float(self.ui.night_worked_LE.text()) if self.ui.night_worked_LE.text() != "" else 0.0
        self.ui.total_night_pay_LE.setText(str(night_rate*night_worked))

    def reload_total_holiday_pay(self):
        """
        Updates the line edit for total holiday pay each time the line edits for holiday rate and worked changed.
        """
        holiday_rate = float(self.ui.holiday_rate_LE.text()) if self.ui.holiday_rate_LE.text() != "" else 0.0
        holiday_worked = float(self.ui.holiday_worked_LE.text()) if self.ui.holiday_worked_LE.text() != "" else 0.0
        self.ui.total_holiday_pay_LE.setText(str(holiday_rate*holiday_worked))

    def reload_total_ot_pay(self):
        """
        Updates the line edit for total ot pay each time the line edits for ot rate and worked changed.
        """
        ot_rate = float(self.ui.ot_rate_LE.text()) if self.ui.ot_rate_LE.text() != "" else 0.0
        ot_worked = float(self.ui.ot_hours_LE.text()) if self.ui.ot_hours_LE.text() != "" else 0.0
        self.ui.total_ot_pay_LE.setText(str(ot_rate*ot_worked))

    def reload_gross_pay(self):
        """
        Updates the line edit for gross pay each time the line edits for totals changed.
        """
        self.ui.gross_pay_LE.setText(str(
              (float(self.ui.total_day_pay_LE.text())     if self.ui.total_day_pay_LE.text() != "" else 0.0)
            + (float(self.ui.total_night_pay_LE.text())   if self.ui.total_night_pay_LE.text() != "" else 0.0)
            + (float(self.ui.total_holiday_pay_LE.text()) if self.ui.total_holiday_pay_LE.text() != "" else 0.0)
            + (float(self.ui.total_ot_pay_LE.text())      if self.ui.total_ot_pay_LE.text() != "" else 0.0)
                                  ))

    def reload_total_deduction(self):
        """
        Updates the line edit for total deduction each time the deductions table changed.
        """
        global deductions_DICT
        num_of_row, deductions = self.ui.deductions_TBL.rowCount(), 0.0

        for row in range(num_of_row):
            pre_deduction = self.ui.deductions_TBL.item(row, 0)
            pre_amount = self.ui.deductions_TBL.item(row, 1)

            deduction = self.ui.deductions_TBL.item(row, 0).text() if pre_deduction != None and pre_deduction.text() != "" else "Deduction"+str(row)
            amount =  self.ui.deductions_TBL.item(row, 1).text() if pre_amount != None and pre_amount.text() else 0.0

            deductions_DICT[deduction] = amount
            deductions += float(deductions_DICT[deduction])

        self.ui.total_deduction_LE.setText(str(deductions))

    def reload_net_pay(self):
        """
        Updates the line edit for total night pay each time the line edits for gross pay and total deduction changed.
        """
        self.ui.net_pay_LE.setText(str(
            (float(self.ui.gross_pay_LE.text()) if self.ui.gross_pay_LE.text() != "" else 0.0)
            - (float(self.ui.total_deduction_LE.text()) if self.ui.total_deduction_LE.text() != "" else 0.0)
            ))

    def export_data(self):
        """
        Generates excel file
        """
        date_and_time = datetime.now().strftime("%m-%d-%Y(%I-%M-%S%p)")
        company_name = self.ui.company_name_LE.text()
        prepared_by = self.ui.prepared_by_LE.text()
        period = self.ui.period_LE.text()

        wb = load_workbook(path.normpath(getcwd()+"/mugna/assets/basis.xlsx"))
        ws = wb.active

        if c.execute("SELECT * FROM employees"):
            employees = c.fetchall()
            generate_stub(company_name=company_name, employees=employees, period=period, prepared_by=prepared_by, ws=ws)
        
        try:
            filename = date_and_time+"-Payroll Stub.xlsx"
            save_wb(wb, filename)
            self.ui.notification_LBL.setText("Exported successfully.")
            self.ui.notification_LBL.setVisible(True)
            QTimer.singleShot(1500, self.show_notification_LBL)
            open_file_explorer(filename)
        except:
            show_pop_up("Failed to export.")

    def show_notification_LBL(self):
        self.ui.notification_LBL.setVisible(False)


def validate(widget: str, data_type: str):
    if data_type == "int":
        widget.setValidator(QIntValidator())
    elif data_type == "float":
        widget.setValidator(QDoubleValidator(decimals=2))
    elif data_type == "name":
        widget.setValidator(QRegExpValidator(QRegExp("[\\w\\s'.-]+"), line_edit))
    elif data_type == "date":
        widget.setValidator(QRegExpValidator(QRegExp("[\\w\\s\\d'.,-/]+"), line_edit))

def show_pop_up(message: str):
    pop_up = QMessageBox()
    pop_up.setWindowTitle("Warning")
    pop_up.setText(message)
    pop_up.setIcon(QMessageBox.Warning)
    pop_up.setStandardButtons(QMessageBox.Ok)
    pop_up.exec_()

def open_file_explorer(filename: str):
    try:
        subprocess.run([
        path.normpath(path.join(getenv("WINDIR"), "explorer.exe")),
        path.normpath(getcwd()+"/mugna/exports")
        ])
    except:
        show_pop_up("Failed to load File Explorer. File is saved as " 
            + filename + " in " 
            + (path.normpath(getcwd()+"/mugna/exports")))


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
