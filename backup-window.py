import sqlite3
try:
    import tkinter
except ImportError: #python2
    import Tkinter as tkinter
from tkinter.ttk import Treeview
from video2 import *


def pop_export():
    #export sql to excel and print a message (pop-up) in case of success or fail
    try:
        sql_to_excel()
        pop = tkinter.Toplevel(mainWindow)
        pop.title("")
        pop.geometry("150x50")
        pop_label = tkinter.Label(pop, text="Exportado com sucesso.")
        pop_label.pack()
    except:
        pop = tkinter.Toplevel(mainWindow)
        pop.title("")
        pop.geometry("150x50")
        pop_label = tkinter.Label(pop, text="ERRO! Falha ao exportar.")
        pop_label.pack()


def check(event):
    #search text and check listbox
    typed = name_box.get()
    if typed == '':
        for i in rows:
            columns_tree_view.insert("", "end", values=i)
    else:
        data = []
        for i in rows:
            if typed.lower() in i.lower():
                data.append(i)
    columns_tree_view.delete(0, END)
    for i in data:
        columns_tree_view.insert("", "end", values=i)


def serch_me():
    sql = "SELECT * FROM contacts"
    cursor.execute(sql)
    rows = cursor.fetchall()
    typed_name = name_box.get()
    typed_email = email_box.get()
    typed_job = jobPost_box.get()
    typed_company =company_box.get()
    if typed_company == '' and typed_job == '' and typed_email == '' and typed_name == '':
        for i in rows:
            columns_tree_view.insert("", "end", values=i)
    else:
        #cursor.execute("SELECT * FROM contacts WHERE name=?", (typed_name,))
        #cursor.execute("SELECT * FROM contacts WHERE name=?, email=?, job=?, company=?", ((typed_name, typed_email, typed_job, typed_company,)))
        cursor.execute("SELECT * FROM contacts WHERE name=?", (typed_name,))
        selected_rows = cursor.fetchall()
        for c in selected_rows:
            columns_tree_view.insert("", "end", values=c)
    name_box.delete(0, "end")
    email_box.delete(0, "end")
    jobPost_box.delete(0, "end")
    company_box.delete(0, "end")


def clean_box():
    name_box.delete(0, "end")
    email_box.delete(0, "end")
    jobPost_box.delete(0, "end")
    company_box.delete(0, "end")
    for record in columns_tree_view.get_children():
        columns_tree_view.delete(record)


def save_bd():
    try:
        conn.commit()
        pop = tkinter.Toplevel(mainWindow)
        pop.title("")
        pop.geometry("150x50")
        pop_label = tkinter.Label(pop, text="Guardado com sucesso.")
        pop_label.pack()
    except:
        pop = tkinter.Toplevel(mainWindow)
        pop.title("")
        pop.geometry("150x50")
        pop_label = tkinter.Label(pop, text="ERRO! Falha ao guardar.")
        pop_label.pack()

def add_new_person():
    con = sqlite3.connect('contacts_rh.db')
    cursor = con.cursor()
    # cursor.execute("Insert INTO contacts(name,email,email_pessoal) values('" + name + "' ,'" + email + "',' " + email_pessoal + "' )")
    cursor.execute(
        f"Insert INTO contacts(name, last_name, full_name,email, email_pessoal, job, company, phone, fix_phone, linkedin, sector, subsector, zone, notes) values('{typed_add_name}', '{typed_add_last_name}', '{typed_add_full_name}', '{typed_add_email}', '{typed_add_email_pessoal}', '{typed_add_job}', '{typed_add_company}', '{typed_add_phone}', '{typed_add_fix_phone}', '{typed_add_linkedin}', '{typed_add_sector}', '{typed_add_subsector}', '{typed_add_zone}', '{typed_add_notes}')")
    con.commit()


def add_window():
    global typed_add_name
    global typed_add_last_name
    global typed_add_full_name
    global typed_add_email
    global typed_add_email_pessoal
    global typed_add_job
    global typed_add_company
    global typed_add_phone
    global typed_add_fix_phone
    global typed_add_linkedin
    global typed_add_sector
    global typed_add_subsector
    global typed_add_zone
    global typed_add_notes
    top = tkinter.Toplevel()
    top.title("Menu Adicionar contacto")
    top.option_add('*Font', 'Times 14')
    top.geometry('1024x768')
    # NAME SEARCHBAR
    add_name_label = tkinter.Label(top, text='Nome').grid(row=1, column=0, padx=(10, 0), sticky="E")
    add_name_box = tkinter.Entry(top, width=50)
    add_name_box.grid(row=1, column=1, sticky="W", padx=(10, 0))
    # LAST NAME
    add_last_name_label = tkinter.Label(top, text='Sobrenome').grid(row=2, column=0, padx=(10, 0), sticky="E")
    add_last_name_box = tkinter.Entry(top, width=50)
    add_last_name_box.grid(row=2, column=1, sticky="W", padx=(10, 0))
    # FULL_NAME
    add_full_name_label = tkinter.Label(top, text='Nome Completo').grid(row=3, column=0, padx=(10, 0), sticky="E")
    add_full_name_box = tkinter.Entry(top, width=50)
    add_full_name_box.grid(row=3, column=1, sticky="W", padx=(10, 0))
    # EMAIL SEARCHBAR
    add_email_label = tkinter.Label(top, text='Email').grid(row=4, column=0, padx=(10, 0), sticky="E")
    add_email_box = tkinter.Entry(top, width=50)
    add_email_box.grid(row=4, column=1, sticky="W", padx=(10, 0))
    # EMAIL_pessoal SEARCHBAR
    add_pessoal_email_label = tkinter.Label(top, text='Email Pessoal').grid(row=5, column=0, padx=(10, 0), sticky="E")
    add_pessoal_email_box = tkinter.Entry(top, width=50)
    add_pessoal_email_box.grid(row=5, column=1, sticky="W", padx=(10, 0))
    # JOB_POST SEARCHBAR
    add_jobPost_label = tkinter.Label(top, text='Função').grid(row=6, column=0, padx=(10, 0), sticky="E")
    add_jobPost_box = tkinter.Entry(top, width=50)
    add_jobPost_box.grid(row=6, column=1, sticky="W", padx=(10, 0))
    # COMPANY SEARCHBAR
    add_company_label = tkinter.Label(top, text='Empresa').grid(row=7, column=0, padx=(10, 10), sticky="E")
    add_company_box = tkinter.Entry(top, width=50)
    add_company_box.grid(row=7, column=1, sticky="W", padx=(10, 0))
    # PHONE
    add_phone_label = tkinter.Label(top, text='Telemovel').grid(row=8, column=0, padx=(10, 10), sticky="E")
    add_phone_box = tkinter.Entry(top, width=50)
    add_phone_box.grid(row=8, column=1, sticky="W", padx=(10, 0))
    # FIX_PHONE
    add_fix_phone_label = tkinter.Label(top, text='Telefone Fixo').grid(row=9, column=0, padx=(10, 10), sticky="E")
    add_fix_phone_box = tkinter.Entry(top, width=50)
    add_fix_phone_box.grid(row=9, column=1, sticky="W", padx=(10, 0))
    # LINKEDIN
    add_linkedin_label = tkinter.Label(top, text='LinkedIN').grid(row=10, column=0, padx=(10, 10), sticky="E")
    add_linkedin_box = tkinter.Entry(top, width=50)
    add_linkedin_box.grid(row=10, column=1, sticky="W", padx=(10, 0))
    # SECTOR
    add_sector_label = tkinter.Label(top, text='Sector').grid(row=11, column=0, padx=(10, 10), sticky="E")
    add_sector_box = tkinter.Entry(top, width=50)
    add_sector_box.grid(row=11, column=1, sticky="W", padx=(10, 0))
    # SUBSECTOR
    add_subsector_label = tkinter.Label(top, text='Subsector').grid(row=12, column=0, padx=(10, 10), sticky="E")
    add_subsector_box = tkinter.Entry(top, width=50)
    add_subsector_box.grid(row=12, column=1, sticky="W", padx=(10, 0))
    # ZONE
    add_zone_label = tkinter.Label(top, text='Zona').grid(row=13, column=0, padx=(10, 10), sticky="E")
    add_zone_box = tkinter.Entry(top, width=50)
    add_zone_box.grid(row=13, column=1, sticky="W", padx=(10, 0))
    # NOTES
    add_notes_label = tkinter.Label(top, text='Notas').grid(row=14, column=0, padx=(10, 10), sticky="E")
    add_notes_box = tkinter.Entry(top, width=50)
    add_notes_box.grid(row=15, column=1, sticky="W", ipadx=150, ipady=150)
    # GET text
    typed_add_name = add_name_box.get()
    typed_add_last_name = add_last_name_box.get()
    typed_add_full_name = add_full_name_box.get()
    typed_add_email = add_email_box.get()
    typed_add_email_pessoal = add_pessoal_email_box.get()
    typed_add_job = add_jobPost_box.get()
    typed_add_company = add_company_box.get()
    typed_add_phone = add_phone_box.get()
    typed_add_fix_phone = add_fix_phone_box.get()
    typed_add_linkedin = add_linkedin_box.get()
    typed_add_sector = add_sector_box.get()
    typed_add_subsector = add_subsector_box.get()
    typed_add_zone = add_zone_box.get()
    typed_add_notes = add_notes_box.get()
    #ADD BUTTON
    add_new_person_button = tkinter.Button(top, text="Adicionar pessoa", command=add_new_person).grid(row=1, column=2)



#INIT Main Window
mainWindow = tkinter.Tk()
mainWindow.title("Contactos pessoais")
mainWindow.option_add('*Font', 'Times 14')
mainWindow.geometry('1024x768')

#CREATE GRIDS
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=20)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=2)
mainWindow.rowconfigure(2, weight=2)
mainWindow.rowconfigure(3, weight=2)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=60)


#NAME SEARCHBAR
name_label = tkinter.Label(mainWindow, text='Nome').grid(row=1, column=0, padx=(10, 0), sticky="E")
#name_box = tkinter.Text(mainWindow, height=1, width=50).grid(row=1, column=1, sticky="W", padx=(10, 0))
name_box = tkinter.Entry(mainWindow, width=50)
name_box.grid(row=1, column=1, sticky="W", padx=(10, 0))

#EMAIL SEARCHBAR
email_label = tkinter.Label(mainWindow, text='Email').grid(row=2, column=0, padx=(10, 0), sticky="E")
#email_box = tkinter.Text(mainWindow, height=1, width=50).grid(row=2, column=1, sticky="W", padx=(10, 0))
email_box = tkinter.Entry(mainWindow, width=50)
email_box.grid(row=2, column=1, sticky="W", padx=(10, 0))

#JOB_POST SEARCHBAR
jobPost_label = tkinter.Label(mainWindow, text='Função').grid(row=3, column=0, padx=(10, 0), sticky="E")
#jobPost_box = tkinter.Text(mainWindow, height=1, width=50).grid(row=3, column=1, sticky="W", padx=(10, 0))
jobPost_box = tkinter.Entry(mainWindow, width=50)
jobPost_box.grid(row=3, column=1, sticky="W", padx=(10, 0))

#COMPANY SEARCHBAR
company_label = tkinter.Label(mainWindow, text='Empresa').grid(row=4, column=0, ipadx=4, padx=(10, 10), sticky="E")
#company_box = tkinter.Text(mainWindow, height=1, width=50).grid(row=4, column=1, sticky="W", padx=(10, 0))
company_box = tkinter.Entry(mainWindow,width=50)
company_box.grid(row=4, column=1, sticky="W", padx=(10, 0))

#RESULTS_Listbox
result_menu = tkinter.Frame(mainWindow)
result_menu.grid(row=6, column=1, ipadx=250, ipady=150)
columns_menu = ['ID', 'Nome', 'Email', 'Email Pessoal', 'Função', 'Empresa', 'LinkedIn', 'Região']
columns_tree_view = Treeview(result_menu, columns=columns_menu, show='headings')
columns_tree_view.column('ID', width=30)
for col in columns_menu[1:]:
    columns_tree_view.column(col, width=90)
    columns_tree_view.heading(col, text=col)
columns_tree_view.bind('<<TreeviewSelect>>')
#columns_tree_view.bind('<<TreeviewSelect>>', ACRESCENTAR A FUNCAO)
columns_tree_view.pack(side='left', fill='y')

result_scroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=memoryview)
result_scroll.grid(row=5, column=3, sticky='W')

#SEARCH BUTTON
search_button = tkinter.Button(mainWindow, text='Procurar', command=serch_me, width=10).grid(row=1, column=3)

#Clean textbox and listbox
clean_button = tkinter.Button(mainWindow, text="Limpar Campos", command=clean_box, width=10).grid(row=2, column=3)

#ADD NEW BD ENTRY
add_button = tkinter.Button(mainWindow, text='Adicionar pessoa', command=add_window, width=15).grid(row=3, column=3)

#EXPORT BUTTON
export_button = tkinter.Button(mainWindow, text="Exportar Excel", command=pop_export, width=15).grid(row=4, column=3)

#commit DB
commit_buton = tkinter.Button(mainWindow, text="Gravar BD", command=save_bd, width=15).grid(row=5, column=3)

mainWindow.mainloop()



#https://www.python4networkengineers.com/posts/python-intermediate/create_a_tkinter_gui_with_sqlite_backend/
#https://www.youtube.com/watch?v=eIuk1oO_JAY
