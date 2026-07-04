import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont 
from views.login_window import LoginWindow
from styles.theme import MODERN_QSS

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # FIX ERROR QFont::setPointSize
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    app.setStyleSheet(MODERN_QSS)
    
    window = LoginWindow()
    window.show()
    
    sys.exit(app.exec())