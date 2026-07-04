from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                               QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView, QLineEdit)
from PySide6.QtCore import Qt
from database.db_manager import DatabaseManager
# HAPUS BARIS INI: from views.login_window import LoginWindow

class TechWindow(QWidget):
    def __init__(self, tech_email):
        super().__init__()
        self.setWindowTitle("SILAPOR - Dashboard Teknisi")
        self.resize(950, 650)
        
        self.db = DatabaseManager()
        self.email = tech_email
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(12)

        # === HEADER & LOGOUT ===
        header_layout = QHBoxLayout()
        title_box = QVBoxLayout()
        title_box.setSpacing(2)
        
        self.title = QLabel("🛠️  Dashboard Teknisi")
        self.title.setObjectName("pageTitle")
        title_box.addWidget(self.title)
        
        self.welcome = QLabel(f"👤  Teknisi: {self.email}")
        self.welcome.setObjectName("welcomeLabel")
        title_box.addWidget(self.welcome)
        
        header_layout.addLayout(title_box)
        header_layout.addStretch()
        
        self.btn_logout = QPushButton("🚪  Logout")
        self.btn_logout.setObjectName("dangerBtn")
        self.btn_logout.setCursor(Qt.PointingHandCursor)
        self.btn_logout.clicked.connect(self.handle_logout)
        header_layout.addWidget(self.btn_logout)
        main_layout.addLayout(header_layout)

        # === TABEL ===
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["No.", "ID", "Tipe / Lokasi", "Deskripsi Keluhan", "Status", "Tanggal"])
        self.table.verticalHeader().setVisible(False)
        
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed); self.table.setColumnWidth(0, 50)
        header.setSectionResizeMode(1, QHeaderView.Fixed); self.table.setColumnWidth(1, 80)
        header.setSectionResizeMode(2, QHeaderView.Fixed); self.table.setColumnWidth(2, 160)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.Fixed); self.table.setColumnWidth(4, 140)
        header.setSectionResizeMode(5, QHeaderView.Fixed); self.table.setColumnWidth(5, 180)
        
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        main_layout.addWidget(self.table)

        # === SEARCH & CONTROL ===
        control_layout = QHBoxLayout()
        control_layout.setSpacing(10)
        
        self.search_input = QLineEdit()
        self.search_input.setObjectName("searchBar")
        self.search_input.setPlaceholderText("🔍 Cari tugas (deskripsi, tipe)...")
        self.search_input.textChanged.connect(self.load_tasks)
        control_layout.addWidget(self.search_input)
        
        control_layout.addStretch()
        
        self.btn_selesai = QPushButton("✅  Tandai Selesai")
        self.btn_selesai.setObjectName("successBtn")
        self.btn_selesai.setCursor(Qt.PointingHandCursor)
        self.btn_selesai.clicked.connect(self.mark_as_done)
        control_layout.addWidget(self.btn_selesai)
        
        self.btn_refresh = QPushButton("🔄")
        self.btn_refresh.setObjectName("secondaryBtn")
        self.btn_refresh.setCursor(Qt.PointingHandCursor)
        self.btn_refresh.clicked.connect(self.load_tasks)
        control_layout.addWidget(self.btn_refresh)
        
        main_layout.addLayout(control_layout)

        self.load_tasks()

    def load_tasks(self):
        search_term = self.search_input.text().strip()
        tasks = self.db.get_tech_reports(self.email, search_term)
        self.table.setRowCount(len(tasks))
        
        for row_idx, task in enumerate(tasks):
            item_no = QTableWidgetItem(str(row_idx + 1))
            item_no.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 0, item_no)
            
            id_text = f"{task['id']:03d}"
            item_id = QTableWidgetItem(id_text)
            item_id.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 1, item_id)
            
            self.table.setItem(row_idx, 2, QTableWidgetItem(task['tipe_laporan']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(task['deskripsi']))
            
            status = task['status']
            if status == "Menunggu": status_text = "⏳ Menunggu"
            elif status == "Diproses": status_text = "🔧 Diproses"
            else: status_text = "✅ Selesai"
                
            status_item = QTableWidgetItem(status_text)
            status_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 4, status_item)
            
            self.table.setItem(row_idx, 5, QTableWidgetItem(str(task['tanggal'])))

    def mark_as_done(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Peringatan", "⚠️  Pilih tugas yang ingin diselesaikan dari tabel!")
            return

        report_id = self.table.item(current_row, 1).text()

        konfirmasi = QMessageBox.question(self, "Konfirmasi", 
            "Apakah perbaikan ini benar-benar sudah selesai?", 
            QMessageBox.Yes | QMessageBox.No)
        
        if konfirmasi == QMessageBox.Yes:
            if self.db.complete_report(report_id):
                QMessageBox.information(self, "Sukses", "🎉  Tugas berhasil diselesaikan. Kerja bagus!")
                self.load_tasks()
            else:
                QMessageBox.critical(self, "Error", "❌  Gagal mengupdate status database.")

    def handle_logout(self):
        # IMPORT DIPINDAHKAN KE SINI AGA TIDAK TERJADI CIRCULAR IMPORT
        from views.login_window import LoginWindow
        self.next_window = LoginWindow()
        self.next_window.show()
        self.close()