import os
from PyQt5.QtWidgets import QWidget, QTableWidget, QHeaderView, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton,\
    QLabel, QSpacerItem, QSizePolicy, QFileDialog, QGroupBox, QComboBox, QAbstractItemView, QMainWindow
from PyQt5.QtGui import QPixmap


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(open(os.getcwd() + "/styles/basic_style.css").read())
        self.table = QTableWidget()
        self.setting_table()

        self.layoutLeftMain = QVBoxLayout()
        self.group_box = QGroupBox()
        self.group_box_img = QGroupBox()

        self.layoutRightMain = QVBoxLayout()
        self.group_boxRightTable = QGroupBox()
        self.showImageButton = QPushButton("Show Image")
        self.showImageButton.clicked.connect(self.__show_image)
        self.group_boxRightTable.setLayout(self.layoutRightMain)
        self.layoutRightMain.addWidget(self.table)
        self.layoutRightMain.addWidget(self.showImageButton)

        self.layoutImg = QVBoxLayout()
        self.load_participants()

        self.group_box_img.setLayout(self.layoutImg)

        self.layoutLeftMain.addWidget(self.group_box)
        self.layoutLeftMain.addWidget(self.group_box_img)

        self.layoutLeft = QVBoxLayout()
        self.group_box.setLayout(self.layoutLeft)

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.__browse_file)

        self.word = QLineEdit()
        self.algorithm = QComboBox()
        self.load_algorithms()

        self.percentage = QComboBox()
        self.load_percentage()

        self.buttonSearch = QPushButton('Search')
        self.vertical_spacer = QSpacerItem(10, 5, QSizePolicy.Expanding)

        self.layoutLeft.setSpacing(5)

        self.layoutLeft.addWidget(QLabel('Video Path:'))
        self.layoutLeft.addWidget(self.file_path)
        self.layoutLeft.addWidget(self.browse_button)
        self.layoutLeft.addWidget(QLabel('Word:'))
        self.layoutLeft.addWidget(self.word)
        self.layoutLeft.addWidget(QLabel('Neural network Model'))
        self.layoutLeft.addWidget(self.algorithm)
        self.layoutLeft.addWidget(QLabel('Percentage'))
        self.layoutLeft.addWidget(self.percentage)
        self.layoutLeft.addWidget(self.buttonSearch)

        self.layoutLeftMain.addSpacerItem(self.vertical_spacer)

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.layoutLeftMain, 20)
        self.layout.addWidget(self.group_boxRightTable, 80)
        self.setLayout(self.layout)

    def __browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', 'Video file (*.mp4)')
        self.file_path.setText(file_name[0])

    def __show_image(self):
        index = self.table.selectionModel().currentIndex()
        if index.row() == -1:
            return
        image_path = self.table.item(index.row(), 5).text()
        self.selected_image = QLabel()
        self.pixmap = QPixmap(image_path)
        self.selected_image.setPixmap(self.pixmap)
        self.imgWidget = QMainWindow()
        self.imgWidget.setCentralWidget(self.selected_image)
        self.imgWidget.setGeometry(100, 100, 400, 400)
        self.imgWidget.setWindowTitle('Modulo: AT16 PROGRA-102')
        self.imgWidget.show()

    def get_button_search(self):
        return self.buttonSearch

    def load_percentage(self):
        for i in range(0, 110, 10):
            self.percentage.addItem(str(i))

    def load_participants(self):
        self.layoutImg.addWidget(QLabel('Trainer:'))
        self.layoutImg.addWidget(QLabel('\t Jose Paolo Sandoval Noel'))
        self.layoutImg.addWidget(QLabel('Trainees:'))
        self.layoutImg.addWidget(QLabel('\t Abraham Diego Uriquiola'))
        self.layoutImg.addWidget(QLabel('\t Abraham Jurado Aguilera'))
        self.layoutImg.addWidget(QLabel('\t Albert Inti Llanos Corianga'))
        self.layoutImg.addWidget(QLabel('\t Alex Castro'))
        self.layoutImg.addWidget(QLabel('\t Alvaro Q'))
        self.layoutImg.addWidget(QLabel('\t Amilkar Barrientos'))
        self.layoutImg.addWidget(QLabel('\t Dayler Martinez'))
        self.layoutImg.addWidget(QLabel('\t Freddy Claros'))
        self.layoutImg.addWidget(QLabel('\t Ivan Rodrigo Lazo'))
        self.layoutImg.addWidget(QLabel('\t Reynel Sanchez'))
        self.layoutImg.addWidget(QLabel('\t Rodrigo Coa Rodriguez'))
        self.layoutImg.addWidget(QLabel('\t Said Garnica Cruz'))

    def setting_table(self):
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(('Algorithm', 'Word', 'Percentage', 'Second', 'Time', 'image'))
        self.table.setColumnHidden(5, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def load_algorithms(self):
        self.algorithm.addItem("VGG16")
        self.algorithm.addItem("ResNet50")
