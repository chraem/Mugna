from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PyQt5.uic import loadUi

import sys, main_images_rc, sqlite3

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        loadUi("assets/mainWindow.ui", self)

        # Validates the input in line edits
        validate(self.id_emp_LE, "int")

        validate(self.day_rate_LE, "float")
        validate(self.night_rate_LE, "float")
        validate(self.ot_rate_LE, "float")
        validate(self.allowance_rate_LE, "float")

        validate(self.day_worked_LE, "float")
        validate(self.night_worked_LE, "float")
        validate(self.ot_hours_LE, "float")
        validate(self.late_hours_LE, "float")


        self.add_emp_BTN.clicked.connect(self.add_data)

        self.show()


    def add_data(self):
        company_name = self.company_name_LE.text()
        
        employee_data ={
                "id": self.id_emp_LE.text() if self.id_emp_LE.text() != "" else show_pop_up("ID field cannot be empty!"),
                "fn": self.fn_emp_LE.text(),
                "mn": self.mn_emp_LE.text(),
                "ln": self.ln_emp_LE.text(),

                "day_rate": self.day_rate_LE.text(),
                "night_rate": self.night_rate_LE.text(),
                "ot_rate" :self.ot_rate_LE.text(),
                "allowance_rate": self.allowance_rate_LE.text(),

                "day_worked": self.day_worked_LE.text(),
                "night_worked": self.night_worked_LE.text(),
                "ot_hours": self.ot_hours_LE.text(),
                "late_hours": self.late_hours_LE.text(),
        }

        if (c.execute("""
                        INSERT INTO employees(
                            id,
                            fn, mn, ln,
                            day_rate, night_rate, ot_rate, allowance_rate,
                            day_worked, night_worked, ot_hours, late_hours
                        )
                        VALUES(
                                :id,
                                :fn, :mn, :ln,
                                :day_rate, :night_rate, :ot_rate, :allowance_rate,
                                :day_worked, :night_worked, :ot_hours, :late_hours
                              )
                      """, employee_data)
            ):
            conn.commit()
        else:
            show_pop_up("Failed to commit the values into database!")


# Global Functions
def validate(line_edit: str, data_type: str):
    # Prevents the user from inputting data types that are not specified
    if data_type == "int":
        line_edit.setValidator(QIntValidator())
    elif data_type == "float":
        line_edit.setValidator(QDoubleValidator(decimals=2))

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