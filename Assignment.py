import pandas as pd

googlesheetsID = '1rxZwyZp9tsDTd_Q82LdO22XdjqZr14vNvbNKAY7jQYU'
worksheetname = 'Mar-2016'
URL = 'https://docs.google.com/spreadsheets/d/{0}/edit#gid=407992186'.format(
googlesheetsID,
worksheetname
)

df = pd.read_csv(URL)
print(df)

# https://docs.google.com/spreadsheets/d/{0}/edit?usp=sharing