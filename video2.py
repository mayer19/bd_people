#https://www.youtube.com/watch?v=6ArtqEmw49g
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

file = "BD_test.xlsx"
output = "table_output.xlsx"

df = pd.read_excel('BD_test.xlsx', header=0)
#conn = sqlite3.connect('D:\Python\BD_people\contacts_rh.db')
conn = sqlite3.connect('contacts_rh.db')
cursor = conn.cursor()

def excle_to_sql():
        df.to_sql('contacts', con=conn, if_exists='replace', index=False,
                  dtype= {'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                          'name': 'TEXT',
                          'last_name': 'TEXT',
                          'full_name': 'TEXT',
                          'email': 'TEXT',
                          'email_pessoal': 'TEXT',
                          'job': 'TEXT',
                          'company': 'TEXT',
                          'phone': 'TEXT',
                          'fix_phone': 'TEXT',
                          'linkedin': 'TEXT',
                          'sector': 'TEXT',
                          'subsector': 'TEXT',
                          'zone': 'TEXT',
                          'notes': 'TEXT'})


def sql_to_excel():
        engine = create_engine('sqlite:///contacts_rh.db', echo=False)
        results = engine.execute('SELECT * FROM contacts')
        final = pd.DataFrame(results, columns=df.columns)
        final.to_excel(output, index=False)



def show_table():
        for row in cursor.execute("SELECT * FROM contacts"):
                print(row)


def add_contact(name='', last_name='',full_name='',email='',email_pessoal='',job='',company='',phone='',fix_phone='',linkedin='',sector='', subsector='',zone='',notes=''):
        con = sqlite3.connect('contacts_rh.db')
        cursor = con.cursor()
        #cursor.execute("Insert INTO contacts(name,email,email_pessoal) values('" + name + "' ,'" + email + "',' " + email_pessoal + "' )")
        cursor.execute(f"Insert INTO contacts(name, last_name, full_name,email, email_pessoal, job, company, phone, fix_phone, linkedin, sector, subsector, zone, notes) values('{name}', '{last_name}', '{full_name}', '{email}', '{email_pessoal}', '{job}', '{company}', '{phone}', '{fix_phone}', '{linkedin}', '{sector}', '{subsector}', '{zone}', '{notes}')")
        con.commit()
        con.close()

#excle_to_sql()
#add_contact(name='ana', phone='87546', company='zzzz')
#conn.commit()
#sql_to_excel()
#show_table()


