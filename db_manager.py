import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self):
        self.host = "localhost"
        self.user = "root" 
        self.password = "SandiBaru123" 
        self.database = "kampus_report_db"

    def get_connection(self):
        try:
            return mysql.connector.connect(
                host=self.host, user=self.user, password=self.password, database=self.database
            )
        except Error as e:
            print(f"Database Error: {e}")
            return None

    def check_login(self, email, password):
        connection = self.get_connection()
        if not connection: return None
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT role FROM users WHERE email = %s AND password = %s", (email, password))
            user_data = cursor.fetchone()
            return user_data['role'] if user_data else None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def add_report(self, email, tipe, deskripsi):
        connection = self.get_connection()
        if not connection: return False
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO reports (pelapor_email, tipe_laporan, deskripsi) VALUES (%s, %s, %s)", 
                           (email, tipe, deskripsi))
            connection.commit()
            return True
        except Error as e:
            print(f"Error Add Report: {e}")
            return False
        finally:
            if connection.is_connected(): cursor.close(); connection.close()

    # --- FITUR BARU: STATISTIK UNTUK ADMIN ---
    def get_stats(self):
        connection = self.get_connection()
        if not connection: return {'total': 0, 'menunggu': 0, 'diproses': 0, 'selesai': 0}
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT COUNT(*) as total FROM reports")
            total = cursor.fetchone()['total']
            cursor.execute("SELECT COUNT(*) as val FROM reports WHERE status = 'Menunggu'")
            menunggu = cursor.fetchone()['val']
            cursor.execute("SELECT COUNT(*) as val FROM reports WHERE status = 'Diproses'")
            diproses = cursor.fetchone()['val']
            cursor.execute("SELECT COUNT(*) as val FROM reports WHERE status = 'Selesai'")
            selesai = cursor.fetchone()['val']
            return {'total': total, 'menunggu': menunggu, 'diproses': diproses, 'selesai': selesai}
        finally:
            if connection.is_connected(): cursor.close(); connection.close()

    # --- FITUR BARU: SEARCH ADMIN ---
    def get_all_reports(self, search_term=""):
        connection = self.get_connection()
        if not connection: return []
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT * FROM reports 
                WHERE pelapor_email LIKE %s OR deskripsi LIKE %s OR tipe_laporan LIKE %s 
                ORDER BY tanggal DESC
            """
            wildcard = f"%{search_term}%"
            cursor.execute(query, (wildcard, wildcard, wildcard))
            return cursor.fetchall()
        finally:
            if connection.is_connected(): cursor.close(); connection.close()

    def get_all_technicians(self):
        connection = self.get_connection()
        if not connection: return []
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT email FROM users WHERE role = 'teknisi'")
            return [row['email'] for row in cursor.fetchall()]
        finally:
            if connection.is_connected(): cursor.close(); connection.close()

    def assign_technician(self, report_id, tech_email):
        connection = self.get_connection()
        if not connection: return False
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE reports SET teknisi_email = %s, status = 'Diproses' WHERE id = %s", 
                           (tech_email, report_id))
            connection.commit()
            return True
        finally:
            if connection.is_connected(): cursor.close(); connection.close()

    # --- FITUR BARU: SEARCH TEKNISI ---
    def get_tech_reports(self, tech_email, search_term=""):
        connection = self.get_connection()
        if not connection: return []
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT * FROM reports 
                WHERE teknisi_email = %s AND status != 'Selesai' 
                AND (deskripsi LIKE %s OR tipe_laporan LIKE %s)
                ORDER BY tanggal DESC
            """
            wildcard = f"%{search_term}%"
            cursor.execute(query, (tech_email, wildcard, wildcard))
            return cursor.fetchall()
        finally:
            if connection.is_connected(): cursor.close(); connection.close()

    def complete_report(self, report_id):
        connection = self.get_connection()
        if not connection: return False
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE reports SET status = 'Selesai' WHERE id = %s", (report_id,))
            connection.commit()
            return True
        finally:
            if connection.is_connected(): cursor.close(); connection.close()