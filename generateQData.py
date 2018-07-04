import xlrd
import xlwt
import csv
data=xlrd.open_workbook('cash.xls')
table=data.sheets()[0]
data_rows=[]
data_row=[]
new_data_rows=[]
new_data_row=[]
nex_data_row=[]
last_valid_row=[]
theType = ''
for rownum in range(table.nrows):
    data_row.extend(table.row_values(rownum))
    data_rows.append(data_row)
    data_row=[]
for rownum in range(table.nrows):
    data_row = data_rows[rownum]
    if rownum == 0:
        continue
    if rownum != table.nrows-1 :
        nex_data_row = data_rows[rownum+1]
    theType = data_row[6]
    if theType == 'Q1':
        if theType != nex_data_row[6]:
            new_data_rows.append(data_row)
            last_valid_row=data_row
    else :
        if theType != nex_data_row[6]:
            for colnum in range(table.ncols):
                if colnum > 8 :
                    if colnum != table.ncols:
                        if last_valid_row[colnum] != "" and data_row[colnum] != "":
                            new_data_row.append(float(data_row[colnum]) - float(last_valid_row[colnum]))
                        else:
                            new_data_row.append(data_row[colnum])
                else:
                    new_data_row.append(data_row[colnum])
            new_data_rows.append(new_data_row)
            new_data_row=[]
with open("output.csv","w", encoding='utf8',newline='') as f:
    writer = csv.writer(f)
    for item in new_data_rows:
        writer.writerow(item)
