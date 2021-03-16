import openpyxl

wb = openpyxl.load_workbook(input('어떤 파일을 실행할까요?')) 
sheet1 = wb.active 

colname = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in alphabets:
    for y in alphabets:
        colname.append(x+y)
for x in alphabets:
    for y in alphabets:
        for z in alphabets:
            colname.append(x+y+z)

for i in colname:
  for row in range(2,52):
    if sheet1[i+str(row)].value == None:
        break
    print(sheet1[i+str(row)].value)
