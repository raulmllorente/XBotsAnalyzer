import sqlite3
import pandas as pd
import openpyxl

db = sqlite3.connect("Databases/twitter.db")

cur = db.cursor()

cuentasTw = """SELECT * FROM cuentasTw"""
notas = """SELECT * FROM notas"""

dfCuentasTw = pd.read_sql_query(cuentasTw, db)
dfNotas = pd.read_sql_query(notas, db)

writer = pd.ExcelWriter('Resultados/AnalisisCuentas.xlsx')
dfCuentasTw.to_excel(writer, sheet_name='CuentasTw')
dfNotas.to_excel(writer, sheet_name='Notas')
writer.save()