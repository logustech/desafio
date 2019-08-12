import pymysql

class Database:
    def __init__(self):
        host = "desafio.logus.tech"
        user = "desafio"
        password = "desafio"
        db = "desafio"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    
    def find_game_by_id(self, id):
        self.cur.execute("SELECT * FROM desafio WHERE id = " + id)
        return self.cur.fetchone()
    
    def events_list(self):
        self.cur.execute("SELECT * FROM desafio")
        result = self.cur.fetchall()
        return result