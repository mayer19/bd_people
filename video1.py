#https://www.youtube.com/watch?v=71zkSuzkJrw
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

file = "BD_test.xlsx"
output = "table_output.xlsx"
#Excel to sqlite3
engine = create_engine('sqlite:///contacts_rh.db', echo=False)
df = pd.read_excel(file)
df.to_sql('contacts', engine, if_exists='replace', index=False)
# sqlite3 to excel
results = engine.execute('SELECT * FROM contacts')
final = pd.DataFrame(results, columns=df.columns)
final.to_excel(output, index=False)



conn = sqlite3.connect('contacts_rh.db')
cursor = conn.cursor()
#cursor.execute("ALTER TABLE contacts(ontacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, last_name TEXT,full_name TEXT, email TEXT, email_pessoal TEXT, job TEXT, company TEXT, phone TEXT, fix_phone TEXT, linkedin TEXT,  sector TEXT, subsector TEXT, zone TEXT, notes TEXT")
cursor.execute("INSERT INTO contacts(name, phone, email) VALUES('abbb', '890743', 'tim@email.com')")

for row in cursor.execute("SELECT * FROM contacts"):
    print(row)