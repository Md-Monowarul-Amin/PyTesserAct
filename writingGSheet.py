import gspread
from oauth2client.service_account import ServiceAccountCredentials


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive	',
]

creds = ServiceAccountCredentials.from_json_keyfile_name("/home/saraj/Desktop/OCR/SecretKey.json", scopes)

file = gspread.authorize(creds)

workbook = file.open("CoT Sheet")
bcs_sheet = workbook.get_worksheet(0)


text_file = open("/home/saraj/Desktop/TextBooks/TextFiles/BCS/BCS.txt", "r")

for i in range(361, 410):
    line = text_file.readline()
    bcs_sheet.update_acell('A' + str(i+1), line)
#print(bcs_sheet.cell(col=1, row=1).value)



"""
Docs: https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/
video: https://www.youtube.com/watch?v=hyUw-koO2DA
"""