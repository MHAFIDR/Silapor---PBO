from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                               QComboBox, QTextEdit, QMessageBox, QFrame, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from database.db_manager import DatabaseManager
# HAPUS BARIS INI: from views.login_window import LoginWindow

class UserWindow(QWidget):
    def __init__(self, user_email): 
        super().__init__()
        self.setWindowTitle("SILAPOR - Mahasiswa")
        self.resize(600, 600)
        
        self.db = DatabaseManager()
        self.email = user_email 
        
        outer = QVBoxLayout(self)
        outer.setContentsMargins(30, 30, 30, 30)
        outer.setSpacing(10)

        # === HEADER & LOGOUT ===
        header_layout = QHBoxLayout()
        title_box = QVBoxLayout()
        title_box.setSpacing(2)
        
        self.title = QLabel("📝  Formulir Pelaporan")
        self.title.setObjectName("pageTitle")
        title_box.addWidget(self.title)
        
        self.welcome = QLabel(f"👤  Login sebagai: {self.email}")
        self.welcome.setObjectName("welcomeLabel")
        title_box.addWidget(self.welcome)
        
        header_layout.addLayout(title_box)
        header_layout.addStretch()
        
        self.btn_logout = QPushButton("🚪  Logout")
        self.btn_logout.setObjectName("dangerBtn")
        self.btn_logout.setCursor(Qt.PointingHandCursor)
        self.btn_logout.clicked.connect(self.handle_logout)
        header_layout.addWidget(self.btn_logout)
        outer.addLayout(header_layout)

        # === CARD FORM ===
        self.card = QFrame()
        self.card.setObjectName("card")
        
        shadow = QGraphicsDropShadowEffect(self.card)
        shadow.setBlurRadius(40)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 12)
        self.card.setGraphicsEffect(shadow)
        
        outer.addWidget(self.card)

        layout = QVBoxLayout(self.card)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(8)

        self.label_tipe = QLabel("📂  Pilih Jenis Laporan")
        self.label_tipe.setObjectName("fieldLabel")
        layout.addWidget(self.label_tipe)

        self.combo_tipe = QComboBox()
        self.combo_tipe.addItems(["Fasilitas Rusak", "Barang Hilang"])
        layout.addWidget(self.combo_tipe)

        self.label_deskripsi = QLabel("📋  Deskripsi Detail")
        self.label_deskripsi.setObjectName("fieldLabel")
        layout.addWidget(self.label_deskripsi)

        self.input_deskripsi = QTextEdit()
        self.input_deskripsi.setPlaceholderText("Jelaskan secara detail apa yang rusak atau hilang, dan lokasinya...")
        self.input_deskripsi.setMinimumHeight(180)
        layout.addWidget(self.input_deskripsi)

        layout.addSpacing(10)

        self.btn_submit = QPushButton("📤  KIRIM LAPORAN")
        self.btn_submit.setObjectName("loginBtn")
        self.btn_submit.setCursor(Qt.PointingHandCursor)
        self.btn_submit.clicked.connect(self.submit_laporan)
        layout.addWidget(self.btn_submit)

    def submit_laporan(self):
        tipe = self.combo_tipe.currentText()
        deskripsi = self.input_deskripsi.toPlainText().strip()
        
        if not deskripsi:
            QMessageBox.warning(self, "Peringatan", "⚠️  Deskripsi laporan tidak boleh kosong!")
            return
            
        if self.db.add_report(self.email, tipe, deskripsi):
            QMessageBox.information(self, "Sukses", "✅  Laporan berhasil dikirim!\n\nTerima kasih atas partisipasi Anda.")
            self.input_deskripsi.clear() 
        else:
            QMessageBox.critical(self, "Error", "❌  Gagal mengirim laporan. Periksa koneksi database.")

    def handle_logout(self):
        # IMPORT DIPINDAHKAN KE SINI AGA TIDAK TERJADI CIRCULAR IMPORT
        from views.login_window import LoginWindow
        self.next_window = LoginWindow()
        self.next_window.show()
        self.close()