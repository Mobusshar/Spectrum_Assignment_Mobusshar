import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk

#root = Tk()
#frame = Frame(root)
#frame.pack()

#root.mainloop()

conn = sqlite3.connect('spectrum.db')

c = conn.cursor()

c.execute("""SELECT * FROM march""")
print(c.fetchall())

conn.commit()

conn.close()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("sample__AttendanceLog__2016").sheet1

# data = sheet.get_all_records()
# print(data)

pp = pprint.PrettyPrinter()


cells = sheet.cell(2,4).value
c = str(cells)
print (c)
print (type(c))
#cell_range = sheet.range('A1:B4')
#print (cell_range)

#count = sheet.row_count
#print(count)

#c = sheet.col_count
#print(c)
view_row = input()
view_col = input()
cells = sheet.cell(view_row,view_col).value
view = str(cells)
print (view)


conn = sqlite3.connect('spectrum.db')

c = conn.cursor()

c.execute("""SELECT * FROM march""")
rr = c.fetchall()
total = c.rowcount

master = Tk()
#master.title("Welcome to Mobusshar app")
#x = view
#master.minsize(width=400, height=400)
#w = Label(master, text=x) 
#w.pack() 

frm = Frame(master)
frm.pack(side=tk.LEFT, padx=20)

tv = ttk.Treeview(frm, columns=(1,2,3,4,5,6,7), show="headings")
tv.pack()

tv.heading(1, text="Name")
tv.heading(2, text="Status")
tv.heading(3, text="Name1")
tv.heading(4, text="Name2")
tv.heading(5, text="Name3")
tv.heading(6, text="Name4")
tv.heading(7, text="Name5")

for i in rr:
    tv.insert('','end', values=i)

master.title("Mobusshar App")
master.geometry("650x650")
master.resizable(True, True)
master.mainloop()
#mainloop()




#window = Tk()

#window.title("Welcome to Mobusshar app")

#window.mainloop()

#val4 = 47
#val3 = 8
#val1 = 46
#val2 = 1


#for i in range (val2,val3):
#    cells = sheet.cell(val1,val2).value
#    c = str(cells)
#    print (c)
#    if val2 == 1:
#        val5 = c
#    elif val2 ==2:
#        val6 = c
#    elif val2 ==3:
#        val7 = c
#    elif val2 ==4:
#        val8 = c
#    elif val2 ==5:
#        val9 = c
#    elif val2 ==6:
#        val10 = c
#    elif val2 ==7:
#        val11 = c
#    else:
#        print("none")
#    val2 = 1 + val2

#for running a query in each cell
#conn = sqlite3.connect('spectrum.db')
#q = conn.cursor()
#q.execute("INSERT INTO march (date, status, name1, name2, name3, name4, name5) VALUES (?,?,?,?,?,?,?)", (val5, val6, val7, val8, val9, val10, val11))
#conn.commit()
#conn.close()