import sqlite3


def createBD():
        ''' create a database connection to file
        '''
        con = sqlite3.connect('contacts_rh.db')

        cursor = con.cursor()

        #create table
        #experimentar trocar text por nvarchar
        cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, last_name TEXT,full_name TEXT, email TEXT, email_pessoal TEXT, job TEXT, company TEXT, phone TEXT, fix_phone TEXT, linkedin TEXT,  sector TEXT, subsector TEXT, zone TEXT, notes TEXT )''')

        #save the changes
        con.commit()

        #close connection (commit alway before close
        con.close()


def add_contact(id='', name='', last_name='',full_name='',email='',email_pessoal='',job='',company='',phone='',fix_phone='',linkedin='',sector='',subsector='',zone='',notes=''):
#def add_contact(*args):
        #insert a row of data
        con = sqlite3.connect('contacts_rh.db')
        cursor = con.cursor()
        #cursor.execute("Insert INTO contacts(name,email,email_pessoal) values('" + name + "' ,'" + email + "',' " + email_pessoal + "' )")
        cursor.execute(f"Insert INTO contacts(name, last_name, full_name,email, email_pessoal, job, company, phone, fix_phone, linkedin, sector, subsector, zone, notes) values('{name}', '{last_name}', '{full_name}', '{email}', '{email_pessoal}', '{job}', '{company}', '{phone}', '{fix_phone}', '{linkedin}', '{sector}', '{subsector}', '{zone}', '{notes}')")
        con.commit()
        con.close()


def show_table():
        con = sqlite3.connect('contacts_rh.db')
        cursor = con.cursor()
        for row in cursor.execute('SELECT * FROM contacts ORDER BY id'):
                print(row)

#https://pynative.com/python-sqlite-insert-into-table/
#createBD()
add_contact(name="rerew", email="mmail", email_pessoal="@mail")
add_contact(name="rerfsdfasew", email="mmail", email_pessoal="@mail")
add_contact(name="fds", email="mmail", email_pessoal="@mail")
add_contact(name='bbdsak')
show_table()

#USAR ESTE SCRIPT