import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QFont, QPixmap, QColor, QPalette, QPainter, QBrush
# from PyQt5.QtCore import QMargins
from PyQt6.QtCore import Qt

class StudentID(QWidget):
    def __init__(self):
        super().__init__()
        self.background_image_path = 'background_logo.png'
        self.initializeUI()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.1)  # adjust to desired transparency level
        painter.drawPixmap(self.rect(), QPixmap(self.background_image_path))
        
    def initializeUI(self):
        self.setGeometry(500, 200, 600, 300)  # Increased the height by 50%
        self.setWindowTitle("Student ID")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Top Section
        self.createTopSection(main_layout)

        # Student Information
        self.createStudentInfo(main_layout)

        self.show()

    def createTopSection(self, layout):
        top_widget = QWidget(self)
        top_layout = QHBoxLayout(top_widget)
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(0)

        # University Logo
        logo_label = QLabel(top_widget)
        pixmap_logo = QPixmap("university_logo.jpg")
        logo_label.setPixmap(pixmap_logo)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        top_layout.addWidget(logo_label)

        # Second Picture
        second_pic_label = QLabel(top_widget)
        pixmap_second_pic = QPixmap("second_picture.png")
        second_pic_label.setPixmap(pixmap_second_pic)
        second_pic_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        top_layout.addWidget(second_pic_label)

        layout.addWidget(top_widget)
    
    def createStudentInfo(self, layout):
        main_layout = QGridLayout()

        # Create the labels
        name_label = QLabel("Name:               Jin, Ping")
        id_label = QLabel("Student ID#:     19691")
        issue_date_label = QLabel("Issue Date:       09/02/2022")
        exp_date_label = QLabel("Exp. Date:        01/04/2024")

        # Create the image labels
        image_label = QLabel(self)
        pixmap_image = QPixmap("student_photo.jpg")
        pixmap_image_with_space = pixmap_image.scaledToWidth(150)  # Add space by scaling the pixmap
        image_label.setPixmap(pixmap_image_with_space)
        
        image_layout = QVBoxLayout()
        image_layout.addSpacing(40)  # Add left spacing to image
        image_layout.addWidget(image_label)
        image_layout.addStretch(1)
        
        image_vert_layout = QVBoxLayout()
        image_vert_layout.addLayout(image_layout)

        image_label2 = QLabel(self)
        pixmap_image = QPixmap("barcode.jpg")
        image_label2.setPixmap(pixmap_image)
        barcode_layout = QHBoxLayout()
        barcode_layout.addSpacing(0)  
        barcode_layout.addWidget(image_label2)

        string_label = QLabel("\t*1-019691*")
        string_layout = QVBoxLayout()
        string_layout.addWidget(string_label)
        string_layout.addSpacing(20)  

        # Create a sub-grid for the labels
        label_layout = QGridLayout()
        label_layout.addWidget(name_label, 0, 0) 
        label_layout.addWidget(id_label, 1, 0)  
        label_layout.addWidget(issue_date_label, 2, 0)  
        label_layout.addWidget(exp_date_label, 3, 0)  
        label_layout.addLayout(barcode_layout, 4, 0)  
        label_layout.addLayout(string_layout, 5, 0)         
        label_layout.setVerticalSpacing(10)  

        # Create a layout for student photo and label
        # student_layout = QVBoxLayout()
        # student_layout.addWidget(image_label)
        # student_layout.addSpacing(50)  # Add vertical spacing between the image and label
        # Create a layout for student photo and label
        # student_layout = QHBoxLayout()  # Changed from QVBoxLayout to QHBoxLayout
        # student_layout.addSpacing(40)  # Modify the size to adjust the space as per requirement
        #  # Adding space at the beginning of the layout
        # student_layout.addWidget(image_label)
        # student_layout.addSpacing(10)  # Add vertical spacing between the image and label

        student_layout = QHBoxLayout()  # Changed from QVBoxLayout to QHBoxLayout
        student_layout.addSpacing(40)  # Modify this value to adjust the space as per requirement
        student_layout.addWidget(image_label)
        student_layout.addSpacing(10)  # Add vertical spacing between the image and label

        student_label = QLabel("STUDENT")
        student_label.setFont(QFont("Arial", 14))
        student_layout.addWidget(student_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add the sub-grid and the other widgets to the main grid
        main_layout.addLayout(student_layout, 0, 0)
        main_layout.addLayout(label_layout, 0, 1)

        layout.addLayout(main_layout)
        main_layout.setHorizontalSpacing(200)
        main_layout.setVerticalSpacing(0)
        main_layout.setRowStretch(1, 1)  # Stretch the first row to occupy extra space

        # Remove the blue background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.white)  
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    student_id = StudentID()
    sys.exit(app.exec())
