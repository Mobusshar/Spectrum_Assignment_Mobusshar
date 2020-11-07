import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("sample__AttendanceLog__2016").sheet1

data = sheet.get_all_records()

row = sheet.row_values(4)



print(row)

f = open("Spectrum.txt", "w")
f.write(str(row))
f.close()