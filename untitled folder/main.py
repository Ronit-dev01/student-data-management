import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction 


class StudentManagement(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Management System")
        self.setGeometry(200, 100, 1100, 650)

        self.initUI()

    def initUI(self):

        # ---------- Menu ----------
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # ---------- Status ----------
        self.statusBar().showMessage("Ready")

        # ---------- Main Widget ----------
        widget = QWidget()
        self.setCentralWidget(widget)

        main_layout = QHBoxLayout()

        # ================= Left Panel ==================
        left_layout = QFormLayout()

        self.id = QLineEdit()
        self.name = QLineEdit()
        self.age = QLineEdit()
        self.course = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()

        left_layout.addRow("Student ID", self.id)
        left_layout.addRow("Name", self.name)
        left_layout.addRow("Age", self.age)
        left_layout.addRow("Course", self.course)
        left_layout.addRow("Email", self.email)
        left_layout.addRow("Phone", self.phone)

        self.addBtn = QPushButton("Add Student")
        self.updateBtn = QPushButton("Update")
        self.deleteBtn = QPushButton("Delete")
        self.clearBtn = QPushButton("Clear")

        left_layout.addRow(self.addBtn)
        left_layout.addRow(self.updateBtn)
        left_layout.addRow(self.deleteBtn)
        left_layout.addRow(self.clearBtn)

        # ================= Right Panel ==================
        right_layout = QVBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Student")

        right_layout.addWidget(self.search)

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Name",
            "Age",
            "Course",
            "Email",
            "Phone"
        ])

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        right_layout.addWidget(self.table)

        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 5)

        widget.setLayout(main_layout)


app = QApplication(sys.argv)

window = StudentManagement()
window.show()

sys.exit(app.exec())
