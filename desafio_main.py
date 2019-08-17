from mysql.connector import connection
import requests
import json


class Desafio:
    def __init__(self):
        self.conn = connection.MySQLConnection(user='desafio', password='desafio', host='desafio.logus.tech',
                                               database='desafio')
        self.cursor = self.conn.cursor()

    def enviar(self):
        self.cursor.execute("select * from desafio;")
        lista_de_partidas = [i for i in self.cursor.fetchall()]
        partida = lista_de_partidas[1]
        dados = {
            "data": [{
                "date": partida[4].strftime("%d/%m/%Y %H:%M"),
                "teams": partida[1],
                "away": partida[2],
                "home": partida[3]
            }],
            "email": "andre_al1@live.com"
        }
        headers = {'content-type': 'application/json'}
        url = "http://desafio.logus.tech/desafio"
        postar = requests.post(url=url, data=json.dumps(dados), headers=headers)
        postar.close()
        self.conn.close()
        return postar


if __name__ == "__main__":
    resultado = Desafio()
    print("Retorno: {}".format(resultado.enviar().content))
