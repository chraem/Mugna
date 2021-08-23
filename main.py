from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PyQt5.QtCore import QRegExp, QSize
from PyQt5.uic import loadUi

import sys, main_images_rc, sqlite3

deductions_DICT, visible = {}, False

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        loadUi("assets/mainWindow.ui", self)
    
        validate(self.id_emp_LE, "int")
        validate(self.fn_emp_LE, "name"); validate(self.mn_emp_LE, "name"); validate(self.ln_emp_LE, "name")
        validate(self.day_rate_LE, "float"); validate(self.night_rate_LE, "float"); 
        validate(self.ot_rate_LE, "float"); validate(self.holiday_rate_LE, "float")

        validate(self.day_worked_LE, "float"); validate(self.night_worked_LE, "float")
        validate(self.ot_hours_LE, "float"); validate(self.holiday_worked_LE, "float")

        self.stacked_widget_page(0)
        self.report_TBL.setRowCount(0)
        self.calculator.setVisible(visible)

        self.new_BTN.clicked.connect(self.clear_data)
        self.add_BTN.clicked.connect(self.add_data)

        self.add_deduction_BTN.clicked.connect(self.add_row)
        self.remove_deduction_BTN.clicked.connect(self.remove_specific_row)
        self.report_BTN.clicked.connect(self.show_report)

        self.day_rate_LE.textChanged.connect(self.reload_total_day_pay); 
        self.night_rate_LE.textChanged.connect(self.reload_total_night_pay); 
        self.holiday_rate_LE.textChanged.connect(self.reload_total_holiday_pay); 
        self.ot_rate_LE.textChanged.connect(self.reload_total_ot_pay); 

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

        self.open_calc_BTN.clicked.connect(self.open_calculator)

        self.show()

    def clear_data(self):
        self.stacked_widget_page(0)
        throw = [   self.id_emp_LE, self.fn_emp_LE, self.mn_emp_LE, self.ln_emp_LE,
                    self.gross_pay_LE, self.total_deduction_LE, self.net_pay_LE,
                    self.day_rate_LE, self.night_rate_LE, self.holiday_rate_LE,
                    self.ot_rate_LE, self.day_worked_LE, self.night_worked_LE,
                    self.holiday_worked_LE, self.ot_hours_LE, self.total_day_pay_LE,
                    self.total_night_pay_LE, self.total_holiday_pay_LE, self.total_ot_pay_LE,
                    self.gross_pay_LE, self.total_deduction_LE, self.net_pay_LE
                ]

        for i in range(len(throw)):
            throw[i].clear()

        self.deductions_TBL.setRowCount(0)
        
    def add_data(self):
        global deductions_DICT
        
        try:
            company_name = self.company_name_LE.text()

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
            if (c.fetchone()):
                show_pop_up("ID: "+employee_data["id"]+" already exists!")
            elif self.id_emp_LE.text() == "":
                show_pop_up("ID field cannot be empty!")
            else:
                show_pop_up("An error occurred")

    
    def show_report(self):
        self.stacked_widget_page(1)
        self.report_TBL.resizeColumnsToContents()
        if ( c.execute("SELECT * FROM employees") ):
            emps = c.fetchall()
            
            self.report_TBL.setRowCount(len(emps))

            for row, emp_in_row in enumerate(emps):
                for in_row, emp_data in enumerate(emp_in_row):
                    self.report_TBL.setItem(row, in_row, QTableWidgetItem(str(emp_in_row[in_row]) if str(emp_in_row[in_row]) != "" else "None"))

    def export_stub(self):
        pass

    def open_calculator(self):
        global visible
        if visible == False:
            self.calculator.setVisible(True); visible = True
        else:
            self.calculator.setVisible(False); visible = False

    def add_row(self):
        self.deductions_TBL.setRowCount(self.deductions_TBL.rowCount()+ 1)
        
    def remove_specific_row(self):
        self.deductions_TBL.removeRow(self.deductions_TBL.currentRow())
        
    def stacked_widget_page(self, page):
        if page == 0:
            self.emp_SW.setCurrentIndex(0)
            self.export_BTN.setVisible(False)
            self.report_BTN.setVisible(True); self.add_BTN.setVisible(True)
            self.label_6.setVisible(True); self.prepared_by_LE.setVisible(True)
            self.prev_BTN.setVisible(True); self.next_BTN.setVisible(True)
        else:
            self.emp_SW.setCurrentIndex(1)
            self.add_BTN.setVisible(False)
            self.report_BTN.setVisible(False)
            self.export_BTN.setVisible(True)
            self.label_6.setVisible(False); self.prepared_by_LE.setVisible(False)
            self.prev_BTN.setVisible(False); self.next_BTN.setVisible(False)

    def reload_total_day_pay(self):
        day_rate = float(self.day_rate_LE.text()) if self.day_rate_LE.text() != "" else 0.0
        day_worked = float(self.day_worked_LE.text()) if self.day_worked_LE.text() != "" else 0.0
        self.total_day_pay_LE.setText(str(day_rate*day_worked))

    def reload_total_night_pay(self):
        night_rate = float(self.night_rate_LE.text()) if self.night_rate_LE.text() != "" else 0.0
        night_worked = float(self.night_worked_LE.text()) if self.night_worked_LE.text() != "" else 0.0
        self.total_night_pay_LE.setText(str(night_rate*night_worked))

    def reload_total_holiday_pay(self):
        holiday_rate = float(self.holiday_rate_LE.text()) if self.holiday_rate_LE.text() != "" else 0.0
        holiday_worked = float(self.holiday_worked_LE.text()) if self.holiday_worked_LE.text() != "" else 0.0
        self.total_holiday_pay_LE.setText(str(holiday_rate*holiday_worked))

    def reload_total_ot_pay(self):
        ot_rate = float(self.ot_rate_LE.text()) if self.ot_rate_LE.text() != "" else 0.0
        ot_worked = float(self.ot_hours_LE.text()) if self.ot_hours_LE.text() != "" else 0.0
        self.total_ot_pay_LE.setText(str(ot_rate*ot_worked))

    def reload_gross_pay(self):
        self.gross_pay_LE.setText(str(
              (float(self.total_day_pay_LE.text())     if self.total_day_pay_LE.text() != "" else 0.0)
            + (float(self.total_night_pay_LE.text())   if self.total_night_pay_LE.text() != "" else 0.0)
            + (float(self.total_holiday_pay_LE.text()) if self.total_holiday_pay_LE.text() != "" else 0.0)
            + (float(self.total_ot_pay_LE.text())      if self.total_ot_pay_LE.text() != "" else 0.0)
                                  ))

    def reload_total_deduction(self):
        global deductions_DICT
        num_of_row, deductions = self.deductions_TBL.rowCount(), 0.0
        
        for row in range(num_of_row):
            pre_deduction = self.deductions_TBL.item(row, 0)
            pre_amount = self.deductions_TBL.item(row, 1)
        
            deduction = self.deductions_TBL.item(row, 0).text() if pre_deduction != None and pre_deduction.text() != "" else "LeftEmpty"+str(row)
            amount =  self.deductions_TBL.item(row, 1).text() if pre_amount != None and pre_amount.text() else 0.0
            
            deductions_DICT[deduction] = amount 
            deductions += float(deductions_DICT[deduction])
        
        self.total_deduction_LE.setText(str(deductions))

    def reload_net_pay(self):
        self.net_pay_LE.setText(str(
            (float(self.gross_pay_LE.text()) if self.gross_pay_LE.text() != "" else 0.0) 
            - (float(self.total_deduction_LE.text()) if self.total_deduction_LE.text() != "" else 0.0)
            ))
                
# Global Functions
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

def close_db():
    conn.close()

conn = sqlite3.connect("database/stub.sqlite")
c = conn.cursor()
c.execute("DELETE FROM employees"); c.execute("DELETE FROM deductions")

# App initialization
app = QApplication(sys.argv)
app.aboutToQuit.connect(close_db)
mainWindow = MainWindow()
sys.exit(app.exec_())