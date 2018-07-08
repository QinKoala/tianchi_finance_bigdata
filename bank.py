# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:11:25 2018

@author: User
"""

import xlrd
from sklearn import linear_model
import numpy as np
import pandas as pd

workbook = xlrd.open_workbook('Income Statement.xls')
booksheet = workbook.sheet_by_index(2)
company = booksheet.col_values(1)
company1 = []
for i in company[1:]:
    if i not in company1:
        company1.append(i)
endtime = booksheet.col_values(4) 

endtime2 = ['2018-03-31','2017-12-31','2017-09-30','2017-06-30','2017-03-31','2016-12-31','2016-09-30','2016-06-30','2016-03-31','2015-12-31','2015-09-30','2015-06-30','2015-03-31','2014-12-31','2014-09-30','2014-06-30','2014-03-31','2013-12-31','2013-09-30','2013-06-30','2013-03-31']
df_revenue = pd.DataFrame(np.arange(609).reshape((29,21)),index=company1, columns=endtime2)
all_row = []
for r in range(len(company)):
    all_row.append(booksheet.row_values(r))
for i in range(len(all_row)):
    for j in endtime2:
        for k in company1:
            if all_row[i][1] == k and all_row[i][4] == j:
                df_revenue[j][k] = all_row[i][9]
for a in endtime2:
    for b in company1:
        df_revenue[a][b]=float(df_revenue[a][b])
for a in endtime2:
    for b in company1:
        if df_revenue[a][b] < 1000:
            df_revenue[a][b] = max(df_revenue.ix[b])

lb1 = []
lb2 = []
lb3 = []
for i in company1:
    lb1 = [i]
    lb2 = lb1*21
    for j in lb2:
        lb3.append(j)
endtime3 = endtime2*29
col_1 = ['股票代码','营业收入','单季营业收入','营业支出','利息收入','货币现金','同业存款','交易性金融资产','佣金现金流','经营现金流','投资收益现金流']
df_timeline = pd.DataFrame(np.arange(6699).reshape((609,11)),index=endtime3, columns=col_1)
df_timeline['股票代码'] = lb3
lb4 = []
lb6 = []
for a in company1:
    lb6.append(df_revenue.ix[a])
    for b in df_revenue.ix[a]:
        lb4.append(b)
df_timeline['营业收入'] = lb4

lb7 = lb6
for a in range(len(lb6)):
    lb7[a][0]=lb6[a][0]
    lb7[a][1]=lb6[a][1] - lb6[a][2]
    lb7[a][2]=lb6[a][2] - lb6[a][3]
    lb7[a][3]=lb6[a][3] - lb6[a][4]
    lb7[a][4]=lb6[a][4]
    lb7[a][5]=lb6[a][5] - lb6[a][6]
    lb7[a][6]=lb6[a][6] - lb6[a][7]
    lb7[a][7]=lb6[a][7] - lb6[a][8]
    lb7[a][8]=lb6[a][8]
    lb7[a][9]=lb6[a][9] - lb6[a][10]
    lb7[a][10]=lb6[a][10] - lb6[a][11]
    lb7[a][11]=lb6[a][11] - lb6[a][12]
    lb7[a][12]=lb6[a][12]
    lb7[a][13]=lb6[a][13] - lb6[a][14]
    lb7[a][14]=lb6[a][14] - lb6[a][15]
    lb7[a][15]=lb6[a][15] - lb6[a][16]
    lb7[a][16]=lb6[a][16]
    lb7[a][17]=lb6[a][17] - lb6[a][18]
    lb7[a][18]=lb6[a][18] - lb6[a][19]
    lb7[a][19]=lb6[a][19] - lb6[a][20]
    lb7[a][20]=lb6[a][20]
lb8 = []
for a in range(len(lb7)):
    for b in lb7[a]:
        lb8.append(b)
df_timeline['单季营业收入'] = lb8

cogs = [0.0]*609
guanlifei = [0.0]*609
for i in range(len(all_row)):
    for j in range(len(endtime3)):
        if all_row[i][1] == lb3[j] and all_row[i][4] == endtime3[j]:
            cogs[j]=all_row[i][25]
            guanlifei[j]=all_row[i][11]
for a in range(len(cogs)):
    if cogs[a]== 0:
        cogs[a] = cogs[a-4]
for b in range(len(guanlifei)):
    if guanlifei[b]== 0:
        guanlifei[b] = guanlifei[b-4]

cogs1 = cogs
for n in range(152):
    cogs1[4*n-3] = float(cogs[4*n-3])-float(cogs[4*n-2])
    cogs1[4*n-2] = float(cogs[4*n-2])-float(cogs[4*n-1])
    cogs1[4*n-1] = float(cogs[4*n-1])-float(cogs[4*n])
guanlifei1 = guanlifei
for n in range(152):
    guanlifei1[4*n-3] = float(guanlifei[4*n-3])-float(guanlifei[4*n-2])
    guanlifei1[4*n-2] = float(guanlifei[4*n-2])-float(guanlifei[4*n-1])
    guanlifei1[4*n-1] = float(guanlifei[4*n-1])-float(guanlifei[4*n])
    
df_timeline['营业支出'] = cogs1
df_timeline['利息收入'] = guanlifei1

########

workbook_2 = xlrd.open_workbook('Balance Sheet.xls')
booksheet_2 = workbook_2.sheet_by_index(2)
company_2 = booksheet_2.col_values(1)
all_row_2 = []
for r in range(len(company_2)):
    all_row_2.append(booksheet_2.row_values(r))

trad_fa = [0.0]*609
cash_e = [0.0]*609
client_d = [0.0]*609
for i in range(len(all_row_2)):
    for j in range(len(endtime3)):
        if all_row_2[i][1] == lb3[j] and all_row_2[i][4] == endtime3[j]:
            trad_fa[j]=all_row_2[i][13]
            cash_e[j]=all_row_2[i][9]
            client_d[j]=all_row_2[i][10]
for a in range(len(trad_fa)):
    if trad_fa[a]== 0 or trad_fa[a]=='':
        trad_fa[a] = trad_fa[a-4]
for b in range(len(cash_e)):
    if cash_e[b]== 0 or cash_e[b]== '':
        cash_e[b] = cash_e[b-4]
for c in range(len(client_d)):
    if client_d[c]== 0 or client_d[c]== '':
        client_d[c] = client_d[c-4]

trad_fa1 = trad_fa
for n in range(152):
    trad_fa1[4*n-3] = float(trad_fa[4*n-3])-float(trad_fa[4*n-2])
    trad_fa1[4*n-2] = float(trad_fa[4*n-2])-float(trad_fa[4*n-1])
    trad_fa1[4*n-1] = float(trad_fa[4*n-1])-float(trad_fa[4*n])
cash_e1 = cash_e
for n in range(152):
    cash_e1[4*n-3] = float(cash_e[4*n-3])-float(cash_e[4*n-2])
    cash_e1[4*n-2] = float(cash_e[4*n-2])-float(cash_e[4*n-1])
    cash_e1[4*n-1] = float(cash_e[4*n-1])-float(cash_e[4*n])
client_d1 = client_d
for n in range(152):
    client_d1[4*n-3] = float(client_d[4*n-3])-float(client_d[4*n-2])
    client_d1[4*n-2] = float(client_d[4*n-2])-float(client_d[4*n-1])
    client_d1[4*n-1] = float(client_d[4*n-1])-float(client_d[4*n])
    
df_timeline['货币现金'] = cash_e
df_timeline['同业存款'] = client_d
df_timeline['交易性金融资产'] = trad_fa

#########

workbook_3 = xlrd.open_workbook('Cash Flow Statement.xls')
booksheet_3 = workbook_3.sheet_by_index(2)
company_3 = booksheet_3.col_values(1)
all_row_3 = []
for r in range(len(company_3)):
    all_row_3.append(booksheet_3.row_values(r))

invest = [0.0]*609
yongjin = [0.0]*609
cfo = [0.0]*609
for i in range(len(all_row_3)):
    for j in range(len(endtime3)):
        if all_row_3[i][1] == lb3[j] and all_row_3[i][4] == endtime3[j]:
            invest[j]=all_row_3[i][36]
            yongjin[j]=all_row_3[i][15]
            cfo[j]=all_row_3[i][19]
for a in range(len(invest)):
    if invest[a]== 0 or invest[a]=='':
        invest[a] = invest[a-4]
for b in range(len(yongjin)):
    if yongjin[b]== 0 or yongjin[b]== '':
        yongjin[b] = yongjin[b-4]
for c in range(len(cfo)):
    if cfo[c]== 0 or cfo[c]== '':
        cfo[c] = cfo[c-4]

invest1 = invest
for n in range(152):
    invest1[4*n-3] = float(invest[4*n-3])-float(invest[4*n-2])
    invest1[4*n-2] = float(invest[4*n-2])-float(invest[4*n-1])
    invest1[4*n-1] = float(invest[4*n-1])-float(invest[4*n])
yongjin1 = yongjin
for n in range(152):
    yongjin1[4*n-3] = float(yongjin[4*n-3])-float(yongjin[4*n-2])
    yongjin1[4*n-2] = float(yongjin[4*n-2])-float(yongjin[4*n-1])
    yongjin1[4*n-1] = float(yongjin[4*n-1])-float(yongjin[4*n])
cfo1 = cfo
for n in range(152):
    cfo1[4*n-3] = float(cfo[4*n-3])-float(cfo[4*n-2])
    cfo1[4*n-2] = float(cfo[4*n-2])-float(cfo[4*n-1])
    cfo1[4*n-1] = float(cfo[4*n-1])-float(cfo[4*n])
    
df_timeline['佣金现金流'] = yongjin
df_timeline['经营现金流'] = cfo
df_timeline['投资收益现金流'] = invest

df_timeline.to_csv("银行行业清洗数据.csv",index=False,sep=',',encoding = 'utf-8')
df_timeline.to_excel("银行行业清洗数据.xlsx",index=False)

endtime5 = ['2018-03','2017-12','2017-09','2017-06','2017-03','2016-12','2016-09','2016-06','2016-03','2015-12','2015-09','2015-06','2015-03','2014-12','2014-09','2014-06','2014-03','2013-12','2013-09','2013-06','2013-03']
endtime6=endtime5*29
df_rev = pd.DataFrame(np.arange(1218).reshape((609,2)),index=None, columns=['time','revenue'])
df_rev['time']=endtime6
df_rev['revenue']=lb8
list_b = []
list_c=[]
for x in range(29):
    df_rev1 = df_rev[21*x-21:21*x].sort(columns = ['time'],axis = 0,ascending = True)
    list_c=[df_rev1,company1[x]]
    list_b.append(list_c)