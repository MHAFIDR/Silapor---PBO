# styles/theme.py
MODERN_QSS = """
/* ============================================
   1. GLOBAL SETTINGS - Typography & Base
   ============================================ */
* {
    font-family: 'Segoe UI', 'Inter', 'Helvetica Neue', 'Arial', sans-serif;
    font-size: 10pt;
    color: #1E293B;
}

QMainWindow, QWidget {
    background-color: #F1F5F9;
}

/* ============================================
   2. LOGIN WINDOW - Deep Dark Glassmorphism
   ============================================ */
QWidget#loginContainer {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #020617, stop:0.5 #1E1B4B, stop:1 #312E81);
}

QFrame#loginCard {
    background-color: rgba(255, 255, 255, 0.96);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.8);
}

QLabel#loginIcon { 
    font-size: 48pt; 
    qproperty-alignment: AlignCenter; 
}
QLabel#loginTitle { 
    color: #0F172A; 
    font-size: 24pt; 
    font-weight: 900; 
    letter-spacing: 2px; 
    qproperty-alignment: AlignCenter; 
}
QLabel#loginSubtitle { 
    color: #64748B; 
    font-size: 10pt; 
    font-weight: 500;
    qproperty-alignment: AlignCenter; 
    padding-bottom: 15px; 
}
QLabel#loginFooter { 
    color: rgba(255, 255, 255, 150); 
    font-size: 8pt; 
    letter-spacing: 1px;
    qproperty-alignment: AlignCenter; 
}

/* ============================================
   3. INPUT FIELDS - Glowing Focus & Sleek
   ============================================ */
QLineEdit, QTextEdit, QComboBox {
    background-color: #F8FAFC;
    border: 2px solid #E2E8F0;
    border-radius: 12px;
    padding: 12px 16px;
    color: #0F172A;
    selection-background-color: #6366F1;
    selection-color: white;
}

/* Efet Glow saat diklik */
QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
    border: 2px solid #6366F1;
    background-color: #FFFFFF;
}

QLineEdit::placeholder, QTextEdit::placeholder {
    color: #94A3B8;
    font-style: italic;
}

QComboBox::drop-down {
    border: none;
    width: 40px;
    border-top-right-radius: 12px;
    border-bottom-right-radius: 12px;
}
QComboBox::down-arrow {
    image: none;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 7px solid #6366F1;
    margin-right: 15px;
}
QComboBox QAbstractItemView {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    selection-background-color: #6366F1;
    selection-color: white;
    outline: none;
    padding: 8px;
}

/* Search Bar Spesific */
QLineEdit#searchBar {
    background-color: #FFFFFF;
    padding: 12px 16px 12px 40px;
    border: 2px solid #E2E8F0;
    border-radius: 20px;
    font-weight: 500;
}
QLineEdit#searchBar:focus {
    border: 2px solid #8B5CF6;
}

/* ============================================
   4. BUTTONS - 3D Tactile Gradient
   ============================================ */
QPushButton {
    background-color: #6366F1;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 18px;
    font-weight: bold;
}

QPushButton:hover { background-color: #4F46E5; }
QPushButton:pressed { background-color: #4338CA; }

QPushButton#secondaryBtn {
    background-color: #F1F5F9;
    color: #475569;
    border: 1px solid #E2E8F0;
}
QPushButton#secondaryBtn:hover { background-color: #E2E8F0; }

QPushButton#successBtn {
    background-color: #10B981;
    border-bottom: 3px solid #047857;
}
QPushButton#successBtn:hover { background-color: #059669; }
QPushButton#successBtn:pressed { 
    background-color: #047857; 
    border-bottom: 1px solid #047857;
    margin-top: 2px;
}

QPushButton#dangerBtn {
    background-color: #EF4444;
    border-bottom: 3px solid #B91C1C;
}
QPushButton#dangerBtn:hover { background-color: #DC2626; }
QPushButton#dangerBtn:pressed { 
    background-color: #B91C1C; 
    border-bottom: 1px solid #B91C1C;
    margin-top: 2px;
}

QPushButton#loginBtn {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1 #8B5CF6);
    font-size: 12pt;
    padding: 16px 18px;
    border-radius: 14px;
    border-bottom: 4px solid #4338CA;
}
QPushButton#loginBtn:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4F46E5, stop:1 #7C3AED);
}
QPushButton#loginBtn:pressed {
    border-bottom: 1px solid #4338CA;
    margin-top: 3px;
}

/* ============================================
   5. LABELS - Typography
   ============================================ */
QLabel#pageTitle { 
    font-size: 18pt; 
    font-weight: 800; 
    color: #0F172A; 
    padding: 4px 0 0px 0; 
}
QLabel#pageSubtitle { 
    color: #64748B; 
    font-size: 10pt; 
    padding-bottom: 12px; 
}
QLabel#welcomeLabel {
    font-size: 11pt; 
    color: #4F46E5; 
    font-weight: bold;
    background-color: #EEF2FF; 
    padding: 10px 16px; 
    border-radius: 10px; 
    border: 1px solid #C7D2FE;
}
QLabel#fieldLabel { 
    color: #475569; 
    font-size: 9pt; 
    font-weight: bold; 
    padding-top: 10px; 
}

/* ============================================
   6. STATISTIC CARDS - Glowing Borders
   ============================================ */
QFrame#statCard {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 15px;
}
QFrame#statCard#totalCard { 
    border-top: 4px solid #6366F1; 
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #EEF2FF);
}
QFrame#statCard#pendingCard { 
    border-top: 4px solid #F59E0B; 
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #FFFBEB);
}
QFrame#statCard#processCard { 
    border-top: 4px solid #3B82F6; 
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #EFF6FF);
}
QFrame#statCard#doneCard { 
    border-top: 4px solid #10B981; 
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #ECFDF5);
}

QLabel#statTitle { font-size: 9pt; color: #64748B; font-weight: bold; letter-spacing: 1px; }
QLabel#statValue { font-size: 28pt; font-weight: 900; color: #0F172A; padding-top: 5px; }

/* ============================================
   7. TABLE - Premium Dashboard Style
   ============================================ */
QTableWidget {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    border-top: 0px;
    gridline-color: #F8FAFC;
    outline: none;
    selection-background-color: #EEF2FF;
    selection-color: #4F46E5;
    alternate-background-color: #FAFBFF;
}

QTableWidget::item {
    padding: 14px 10px;
    border-bottom: 1px solid #F1F5F9;
    color: #334155;
}

QTableWidget::item:selected {
    background-color: #EEF2FF;
    color: #4F46E5;
    font-weight: bold;
}

QTableWidget::item:hover {
    background-color: #F8FAFC;
    color: #1E293B;
}

QHeaderView::section {
    background-color: #1E293B;
    color: #F8FAFC;
    padding: 16px 10px;
    border: none;
    font-weight: 800;
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 1px;
}

QHeaderView::section:first { border-top-left-radius: 16px; }
QHeaderView::section:last { border-top-right-radius: 16px; }

QTableCornerButton::section {
    background-color: #1E293B;
    border: none;
    border-top-left-radius: 16px;
}

/* ============================================
   8. MISC, DIALOGS & SCROLLBARS
   ============================================ */
QMessageBox {
    background-color: #FFFFFF;
}
QMessageBox QLabel {
    color: #1E293B;
    font-size: 10pt;
    min-width: 280px;
    padding: 20px;
}
QMessageBox QPushButton {
    min-width: 90px;
    padding: 10px 18px;
    border-radius: 10px;
    font-weight: bold;
}

QScrollBar:vertical {
    background: #F1F5F9; 
    width: 10px; 
    margin: 16px 4px 16px 0; 
    border-radius: 5px;
}
QScrollBar::handle:vertical {
    background: #CBD5E1; 
    border-radius: 5px; 
    min-height: 40px;
}
QScrollBar::handle:vertical:hover { background: #94A3B8; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; height: 0; }

QFrame#card {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 20px;
}
"""