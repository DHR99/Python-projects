import sqlite3


class DataBase:

	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY, Title VARCHAR(100), Author VARCHAR(20), Year INTEGER, ISBN INTEGER)")
		self.conn.commit()


	def insert(self, title, author, year, isbn):
		self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
		self.conn.commit()
		


	def view_all(self):
		self.cur.execute("SELECT * FROM book")
		rows = self.cur.fetchall()
		return rows


	def search(self, title="", author="", year="", isbn=""):
		self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
		rows = self.cur.fetchall()
		return rows


	def delete(self, id):
		self.cur.execute("DELETE FROM book WHERE id=?", (id,))
		conn.commit()


	def update(self, id, title, author, year, isbn):
		self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE ID=?", (title, author, year, isbn, id))
		self.conn.commit()


    def __del__(self): # delete instance when the script is exited
        self.conn.close()


	

