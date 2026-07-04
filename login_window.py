from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLineEdit, 
                               QLabel, QMessageBox, QFrame, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from database.db_manager import DatabaseManager
from views.user_window import UserWindow
from views.admin_window import AdminWindow
from views.tech_window import TechWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("loginContainer")
        self.setWindowTitle("SILAPOR - Login")
        self.resize(440, 560)
        
        self.db = DatabaseManager()

        outer = QVBoxLayout(self)
        outer.setContentsMargins(40, 40, 40, 40)

        self.card = QFrame()
        self.card.setObjectName("loginCard")
        
        # Efek bayangan gelap tebal
        shadow = QGraphicsDropShadowEffect(self.card)
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(0, 20)
        self.card.setGraphicsEffect(shadow)
        
        outer.addWidget(self.card)

        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(6)

        self.icon = QLabel("🎓")
        self.icon.setObjectName("loginIcon")
        card_layout.addWidget(self.icon)

        self.title = QLabel("SILAPOR")
        self.title.setObjectName("loginTitle")
        card_layout.addWidget(self.title)

        self.subtitle = QLabel("Sistem Pelaporan Kampus")
        self.subtitle.setObjectName("loginSubtitle")
        card_layout.addWidget(self.subtitle)

        card_layout.addSpacing(20)

        self.lbl_email = QLabel("📧  Alamat Email")
        self.lbl_email.setObjectName("fieldLabel")
        card_layout.addWidget(self.lbl_email)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("masukkan email anda...")
        card_layout.addWidget(self.email_input)

        self.lbl_pass = QLabel("🔒  Kata Sandi")
        self.lbl_pass.setObjectName("fieldLabel")
        card_layout.addWidget(self.lbl_pass)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("masukkan password...")
        self.password_input.setEchoMode(QLineEdit.Password)
        card_layout.addWidget(self.password_input)

        self.email_input.returnPressed.connect(self.handle_login)
        self.password_input.returnPressed.connect(self.handle_login)

        card_layout.addSpacing(25)

        self.login_btn = QPushButton("🚀  MASUK KE DASHBOARD")
        self.login_btn.setObjectName("loginBtn")
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_btn.clicked.connect(self.handle_login)
        card_layout.addWidget(self.login_btn)

        card_layout.addStretch()

        outer.addStretch()

        self.footer = QLabel("© 2026 SILAPOR - UAS Pemrograman Berorientasi Objek")
        self.footer.setObjectName("loginFooter")
        outer.addWidget(self.footer)

    def handle_login(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        role = self.db.check_login(email, password)

        if role == "user":
            self.next_window = UserWindow(email) 
            self.next_window.show()
            self.close()
        elif role == "admin":
            self.next_window = AdminWindow() 
            self.next_window.show()
            self.close()
        elif role == "teknisi":
            self.next_window = TechWindow(email) 
            self.next_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Akses Ditolak", "Email atau Password tidak valid!\n\nSilakan coba lagi.")