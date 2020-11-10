import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import sqlite3
from Tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Spectrum')
root.geometry("400x400")

conn = sqlite3.connect('spectrum.db')

c = conn.cursor()

c.execute("""SELECT * FROM march""")

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

count = sheet.row_count
print(count)

c = sheet.col_count
print(c)
val4 = 47
val3 = 8
val1 = 1
val2 = 1


for i in range (val2,val3):
    cells = sheet.cell(val1,val2).value
    c = str(cells)
    print (c)
    val2 = 1 + val2