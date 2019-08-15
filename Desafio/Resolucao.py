import pymysql
import json
import datetime
import requests
import time

# Conectando
import simplejson as simplejson

db = pymysql.connect(host="desafio.logus.tech", user="desafio", passwd="desafio", db="desafio")
#db = pymysql.connections.Connection (host="desafio.logus.tech", user="desafio", port = 3306) # descobrir tabela

# Cria um cursor
#cursor = db.cursor()

# Executa o SQL
#cursor.execute("SHOW DATABASES") # mostrar databases para pegar a tabela desafio
#cursor.execute("SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'desafio'") #pegar o nome das colunas

cursor2 = db.cursor()
cursor2.execute("SELECT  date , teams, away, home FROM desafio")

#cursor.execute("SHOW TABLES") #mostrar tabelas

resultado1 = cursor2.fetchall()

listaTuplas = list((resultado1)) #lista[tuplas]
resultado2 = list()

for l in listaTuplas: #lista de tuplas para dicionario
    temp = dict()
    temp = {"date": l[0].strftime('%d/%m/%Y, %H:%M'),"teams":l[1],"away":l[2],"home":l[3]}
    resultado2.append(temp)

email = {"email": "carlosamtoni@gmail.com"} # adicionar email

fim = {"data": resultado2} #concatenar

fim.update(email) #concatenar

r = requests.post("http://desafio.logus.tech/desafio", data=json.dumps(fim, ensure_ascii=False)) #POST