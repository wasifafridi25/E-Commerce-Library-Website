import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QFontMetrics
from PyQt6.QtCore import Qt

class LandmarkTriviaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Landmark Trivia App")
        self.setGeometry(500, 200, 600, 400)

        self.questions = [
            {
                "question": "Which city is home to the Eiffel Tower?",
                "options": ["Rome", "Paris", "London", "New York"],
                "answer": "Paris"
            },
            {
                "question": "Which monument is located in India?",
                "options": ["Great Wall of China", "Colosseum", "Taj Mahal", "Statue of Liberty"],
                "answer": "Taj Mahal"
            },
            {
                "question": "What is the name of the famous statue in Rio de Janeiro?",
                "options": ["Christ the Redeemer", "The Sphinx", "Mona Lisa", "Statue of Liberty"],
                "answer": "Christ the Redeemer"
            },
            {
                "question": "Where is the Great Wall located?",
                "options": ["China", "USA", "Egypt", "Brazil"],
                "answer": "China"
            }
        ]

        self.current_question_index = 0
        self.score = 0

        self.question_label = QLabel()
        self.question_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.option_buttons = []

        self.next_button = QPushButton("Next Question")
        self.next_button.clicked.connect(self.next_question)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout)

        self.display_question(self.current_question_index)

    def display_question(self, question_index):
        # Remove previous QRadioButtons
        for button in self.option_buttons:
            self.layout.removeWidget(button)
            button.setParent(None)
            button.deleteLater()
        self.option_buttons.clear()

        question = self.questions[question_index]

        self.question_label.setText(question["question"])

        options = question["options"]
        random.shuffle(options)

        for i, option in enumerate(options):
            button = QRadioButton(option)
            self.option_buttons.append(button)
            self.layout.insertWidget(i+1, button)

        self.next_button.setEnabled(True)

    def next_question(self):
        selected_button = None
        for button in self.option_buttons:
            if button.isChecked():
                selected_button = button
                break

        if selected_button is not None:
            selected_option = selected_button.text()
            correct_answer = self.questions[self.current_question_index]["answer"]

            if selected_option == correct_answer:
                self.score += 1

            self.current_question_index += 1

            if self.current_question_index < len(self.questions):
                self.display_question(self.current_question_index)
            else:
                self.show_result()
        else:
            QMessageBox.warning(self, "Answer Required", "Please select an answer.")

    def show_result(self):
        result_message = f"You answered {self.score} out of {len(self.questions)} questions correctly."
        QMessageBox.information(self, "Quiz Result", result_message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    landmark_trivia_app = LandmarkTriviaApp()
    landmark_trivia_app.show()

    sys.exit(app.exec())
