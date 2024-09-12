import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class RoundedWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle('Example with Rounded Elements')

        # Создаем вертикальный layout
        layout = QVBoxLayout()

        # Создаем три текстовых поля с подписями и закруглёнными углами
        for i in range(3):
            label = QLabel(f'Field {i + 1}:', self)
            layout.addWidget(label)

            line_edit = QLineEdit(self)
            line_edit.setStyleSheet("""
                QLineEdit {
                    border: 2px solid gray;
                    border-radius: 10px;
                    padding: 5px;
                }
            """)
            layout.addWidget(line_edit)

        # Создаем пять кнопок с закруглёнными углами
        for i in range(5):
            button = QPushButton(f'Button {i + 1}', self)
            button.setStyleSheet("""
                QPushButton {
                    border: 2px solid #8f8f91;
                    border-radius: 10px;
                    background-color: #f0f0f0;
                    padding: 5px;
                }
                QPushButton:pressed {
                    background-color: #dcdcdc;
                }
            """)
            layout.addWidget(button)

        # Устанавливаем layout для окна
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RoundedWindow()
    window.show()
    sys.exit(app.exec())