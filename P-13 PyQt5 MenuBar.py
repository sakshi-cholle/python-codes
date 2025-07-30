import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QLabel,
    QLineEdit, QVBoxLayout, QWidget, QMessageBox
)

class SimpleAdder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Adder")
        self.setGeometry(100, 100, 300, 150)

        # === Menu ===
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        add_action = QAction("Add", self)
        add_action.triggered.connect(self.add_numbers)
        file_menu.addAction(add_action)

        # === Inputs and Label ===
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.label_result = QLabel("Result:", self)

        layout = QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.label_result)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_numbers(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 + num2
            self.label_result.setText(f"Result: {result}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleAdder()
    window.show()
    sys.exit(app.exec_())
