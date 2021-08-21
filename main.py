from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PyQt5.QtCore import QRegExp
from PyQt5.uic import loadUi

import sys, main_images_rc, sqlite3

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        loadUi("assets/mainWindow.ui", self)

        # Validates the input in line edits
        validate(self.id_emp_LE, "int")

        validate(self.ln_emp_LE, "name")

        validate(self.day_rate_LE, "float")
        validate(self.night_rate_LE, "float")
        validate(self.ot_rate_LE, "float")
        validate(self.holiday_rate_LE, "float")

        validate(self.day_worked_LE, "float")
        validate(self.night_worked_LE, "float")
        validate(self.ot_hours_LE, "float")
        validate(self.holiday_worked_LE, "float")

        self.add_emp_BTN.clicked.connect(self.add_data)
        self.add_deduction_BTN.clicked.connect(self.add_row)
        self.remove_deduction_BTN.clicked.connect(self.remove_specific_row)

        self.show()


    def add_data(self):
        deductions_DICT = {}

        #try:
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
            }

        # Get the inputs from table widget
        for row in range(self.deductions_TBL.rowCount()):
            for col in range(self.deductions_TBL.columnCount()):
                deduction = self.deductions_TBL.item(row, 0).text()
                amount = self.deductions_TBL.item(row, 1).text()
                deductions_DICT[deduction] = amount

        if (c.execute("""
                        INSERT INTO employees(
                            id,
                            fn, mn, ln,
                            day_rate, night_rate, holiday_rate, ot_rate, 
                            day_worked, night_worked, holiday_worked, ot_hours)
                        VALUES(
                            :id,
                            :fn, :mn, :ln,
                            :day_rate, :night_rate, :holiday_rate, :ot_rate, 
                            :day_worked, :night_worked, :holiday_worked, :ot_hours
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
        
        # except:
        #     c.execute("SELECT id FROM employees WHERE id = :id LIMIT 1", employee_data)
        #     if (c.fetchone()):
        #         show_pop_up("ID: "+employee_data["id"]+" already exists!")
        #     elif self.id_emp_LE.text() == "":
        #         show_pop_up("ID field cannot be empty!")
        #     else:
        #         show_pop_up("Failed to commit the values into database!")

    def add_row(self):
        # Add new row
        self.deductions_TBL.setRowCount(self.deductions_TBL.rowCount()+ 1)
        
    def remove_specific_row(self):
        # Removes the selected row
        self.deductions_TBL.removeRow(self.deductions_TBL.currentRow())
        

# Global Functions
def validate(line_edit: str, data_type: str):
    # Prevents the user from inputting data types that are not specified
    if data_type == "int":
        line_edit.setValidator(QIntValidator())
    elif data_type == "float":
        line_edit.setValidator(QDoubleValidator(decimals=2))
    elif data_type == "name":
        line_edit.setValidator(QRegExpValidator(QRegExp("[a-zA-Z.\\s]+"), line_edit))

def show_pop_up(message: str):
    pop_up = QMessageBox()
    pop_up.setWindowTitle("Warning")
    pop_up.setText(message)
    pop_up.setIcon(QMessageBox.Warning)
    pop_up.setStandardButtons(QMessageBox.Ok)
    pop_up.exec_()

def close_db():
    # Close database when called
    conn.close()

conn = sqlite3.connect("database/stub.sqlite")
c = conn.cursor()

# App initialization
app = QApplication(sys.argv)
app.aboutToQuit.connect(close_db)
mainWindow = MainWindow()
sys.exit(app.exec_())


# NOTES
# Comment out try catch if okay na ung validator for table column
# Add String validator
