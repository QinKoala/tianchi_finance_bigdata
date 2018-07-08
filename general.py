# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:15:18 2018

@author: User
"""

import xlrd
from sklearn import linear_model
import numpy as np
import pandas as pd

workbook = xlrd.open_workbook('Income Statement.xls')
booksheet = workbook.sheet_by_index(0)
company = booksheet.col_values(1)
company1 = []
for i in company[1:]:
    if i not in company1:
        company1.append(i)
endtime = booksheet.col_values(4) 

endtime2 = ['2018-03-31','2017-12-31','2017-09-30','2017-06-30','2017-03-31','2016-12-31','2016-09-30','2016-06-30','2016-03-31','2015-12-31','2015-09-30','2015-06-30','2015-03-31','2014-12-31','2014-09-30','2014-06-30','2014-03-31','2013-12-31','2013-09-30','2013-06-30','2013-03-31']
df_revenue = pd.DataFrame(np.arange(73311).reshape((3491,21)),index=company1, columns=endtime2)
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
endtime3 = endtime2*6
col_1 = ['股票代码','营业收入','单季营业收入','投资收益','保险业务收入','货币现金','资产总计','交易性金融资产','保险费现金流','经营现金流','投资收益现金流']
df_timeline = pd.DataFrame(np.arange(806421).reshape((73311,11)),index=endtime3, columns=col_1)
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
endtime5 = ['2018-03','2017-12','2017-09','2017-06','2017-03','2016-12','2016-09','2016-06','2016-03','2015-12','2015-09','2015-06','2015-03','2014-12','2014-09','2014-06','2014-03','2013-12','2013-09','2013-06','2013-03']
endtime6=endtime5*3491
df_rev = pd.DataFrame(np.arange(146622).reshape((73311,2)),index=None, columns=['time','revenue'])
df_rev['time']=endtime6
df_rev['revenue']=lb8
list_b = []
list_c=[]
for x in range(3491):
    df_rev1 = df_rev[21*x-21:21*x].sort(columns = ['time'],axis = 0,ascending = True)
    list_c=[df_rev1,company1[x]]
    list_b.append(list_c)