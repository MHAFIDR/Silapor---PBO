from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                               QTableWidget, QTableWidgetItem, QComboBox, QMessageBox, 
                               QHeaderView, QLineEdit, QFrame, QGridLayout)
from PySide6.QtCore import Qt
from database.db_manager import DatabaseManager
# HAPUS BARIS INI: from views.login_window import LoginWindow

class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SILAPOR - Dashboard Admin")
        self.resize(1000, 700)
        self.db = DatabaseManager()
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(15)

        # === HEADER & LOGOUT ===
        header_layout = QHBoxLayout()
        title_box = QVBoxLayout()
        title_box.setSpacing(2)
        
        self.title = QLabel("⚙️  Dashboard Administrator")
        self.title.setObjectName("pageTitle")
        title_box.addWidget(self.title)
        
        self.subtitle = QLabel("Kelola seluruh laporan kampus dan tugaskan teknisi dengan bijak")
        self.subtitle.setObjectName("pageSubtitle")
        title_box.addWidget(self.subtitle)
        
        header_layout.addLayout(title_box)
        header_layout.addStretch()
        
        self.btn_logout = QPushButton("🚪  Logout")
        self.btn_logout.setObjectName("dangerBtn")
        self.btn_logout.setCursor(Qt.PointingHandCursor)
        self.btn_logout.clicked.connect(self.handle_logout)
        header_layout.addWidget(self.btn_logout)
        main_layout.addLayout(header_layout)

        # === STATISTIC CARDS ===
        stats_layout = QGridLayout()
        stats_layout.setSpacing(15)
        
        self.card_total = self.create_stat_card("📦  Total Laporan", "0", "totalCard")
        self.card_pending = self.create_stat_card("⏳  Menunggu", "0", "pendingCard")
        self.card_process = self.create_stat_card("🔧  Diproses", "0", "processCard")
        self.card_done = self.create_stat_card("✅  Selesai", "0", "doneCard")
        
        stats_layout.addWidget(self.card_total, 0, 0)
        stats_layout.addWidget(self.card_pending, 0, 1)
        stats_layout.addWidget(self.card_process, 0, 2)
        stats_layout.addWidget(self.card_done, 0, 3)
        main_layout.addLayout(stats_layout)

        # === TABEL ===
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["No.", "ID", "Pelapor", "Tipe Laporan", "Deskripsi", "Status", "Teknisi"])
        self.table.verticalHeader().setVisible(False)
        
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed); self.table.setColumnWidth(0, 50)
        header.setSectionResizeMode(1, QHeaderView.Fixed); self.table.setColumnWidth(1, 80)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Fixed); self.table.setColumnWidth(3, 150)
        header.setSectionResizeMode(4, QHeaderView.Stretch)
        header.setSectionResizeMode(5, QHeaderView.Fixed); self.table.setColumnWidth(5, 140)
        header.setSectionResizeMode(6, QHeaderView.Stretch)
        
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        main_layout.addWidget(self.table)

        # === SEARCH & CONTROL ===
        control_layout = QHBoxLayout()
        control_layout.setSpacing(10)
        
        self.search_input = QLineEdit()
        self.search_input.setObjectName("searchBar")
        self.search_input.setPlaceholderText("🔍 Cari laporan (ID, email, deskripsi, tipe)...")
        self.search_input.textChanged.connect(self.load_data)
        control_layout.addWidget(self.search_input)
        
        lbl = QLabel("👨‍🔧  Teknisi:")
        lbl.setObjectName("fieldLabel")
        control_layout.addWidget(lbl)
        
        self.combo_teknisi = QComboBox()
        self.combo_teknisi.addItems(self.db.get_all_technicians())
        self.combo_teknisi.setMinimumWidth(200)
        control_layout.addWidget(self.combo_teknisi)

        self.btn_tugaskan = QPushButton("📌  Tugaskan")
        self.btn_tugaskan.setObjectName("successBtn")
        self.btn_tugaskan.setCursor(Qt.PointingHandCursor)
        self.btn_tugaskan.clicked.connect(self.assign_task)
        control_layout.addWidget(self.btn_tugaskan)

        self.btn_refresh = QPushButton("🔄")
        self.btn_refresh.setObjectName("secondaryBtn")
        self.btn_refresh.setCursor(Qt.PointingHandCursor)
        self.btn_refresh.clicked.connect(self.load_data)
        control_layout.addWidget(self.btn_refresh)
        
        main_layout.addLayout(control_layout)

        self.load_data()

    def create_stat_card(self, title, value, obj_name):
        card = QFrame()
        card.setObjectName("statCard")
        card.setObjectName(obj_name)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 15, 20, 15)
        
        lbl_title = QLabel(title)
        lbl_title.setObjectName("statTitle")
        layout.addWidget(lbl_title)
        
        lbl_value = QLabel(value)
        lbl_value.setObjectName("statValue")
        layout.addWidget(lbl_value)
        
        return card

    def load_data(self):
        stats = self.db.get_stats()
        self.card_total.findChild(QLabel, "statValue").setText(str(stats['total']))
        self.card_pending.findChild(QLabel, "statValue").setText(str(stats['menunggu']))
        self.card_process.findChild(QLabel, "statValue").setText(str(stats['diproses']))
        self.card_done.findChild(QLabel, "statValue").setText(str(stats['selesai']))
        
        search_term = self.search_input.text().strip()
        reports = self.db.get_all_reports(search_term)
        self.table.setRowCount(len(reports))
        
        for row_idx, report in enumerate(reports):
            item_no = QTableWidgetItem(str(row_idx + 1))
            item_no.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 0, item_no)
            
            id_text = f"{report['id']:03d}"
            item_id = QTableWidgetItem(id_text)
            item_id.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 1, item_id)
            
            self.table.setItem(row_idx, 2, QTableWidgetItem(report['pelapor_email']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(report['tipe_laporan']))
            self.table.setItem(row_idx, 4, QTableWidgetItem(report['deskripsi']))
            
            status = report['status']
            if status == "Menunggu": status_text = "⏳ Menunggu"
            elif status == "Diproses": status_text = "🔧 Diproses"
            else: status_text = "✅ Selesai"
                
            status_item = QTableWidgetItem(status_text)
            status_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_idx, 5, status_item)
            
            tech_text = report['teknisi_email'] if report['teknisi_email'] else "— Belum Ditugaskan —"
            self.table.setItem(row_idx, 6, QTableWidgetItem(tech_text))

    def assign_task(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Peringatan", "⚠️  Pilih salah satu laporan di tabel terlebih dahulu!")
            return

        report_id = self.table.item(current_row, 1).text()
        tech_email = self.combo_teknisi.currentText()

        if self.db.assign_technician(report_id, tech_email):
            QMessageBox.information(self, "Sukses", f"✅  Laporan ID {report_id} berhasil ditugaskan ke {tech_email}.")
            self.load_data()
        else:
            QMessageBox.critical(self, "Error", "❌  Gagal menugaskan teknisi.")

    def handle_logout(self):
        # IMPORT DIPINDAHKAN KE SINI AGA TIDAK TERJADI CIRCULAR IMPORT
        from views.login_window import LoginWindow
        self.next_window = LoginWindow()
        self.next_window.show()
        self.close()