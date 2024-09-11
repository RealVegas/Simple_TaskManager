import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor, QBrush, QMouseEvent
from PyQt6.QtCore import Qt


class RoundedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rounded Corners Window")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        # Добавляем кнопки для закрытия и сворачивания окна
        self.close_button = QPushButton('×', self)
        self.close_button.setStyleSheet("""
                        QPushButton {
                            border: 0px solid #8f8f91;
                            border-radius: 6px;
                            background-color: #f0f0f0;
                            padding: 0px;
                        }
                        QPushButton:pressed {
                            background-color: #dcdcdc;
                        }
                    """)
        self.close_button.setGeometry(self.width() - 40, 10, 30, 30)
        self.close_button.clicked.connect(self.close)

        self.minimize_button = QPushButton("_", self)
        self.minimize_button.setStyleSheet("""
                                QPushButton {
                                    border: 0px solid #8f8f91;
                                    border-radius: 6px;
                                    background-color: #f0f0f0;
                                    padding: 0px;
                                }
                                QPushButton:pressed {
                                    background-color: #dcdcdc;
                                }
                            """)
        self.minimize_button.setGeometry(self.width() - 80, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)

        # Переменная для хранения позиции курсора
        self.startPos = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(100, 150, 200, 225)))  # Цвет и непрозрачность
        painter.setPen(Qt.PenStyle.NoPen)
        rect = self.rect()
        rect.setWidth(rect.width() - 1)
        rect.setHeight(rect.height() - 1)
        painter.drawRoundedRect(rect, 10, 10)  # Устанавливаем радиус закругления

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.startPos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton and self.startPos is not None:
            self.move(event.globalPosition().toPoint() - self.startPos)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.startPos = None


def main():
    app = QApplication(sys.argv)
    window = RoundedWindow()
    window.show()
    sys.exit(app.exec())


main()