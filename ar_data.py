# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:35:53 2018

@author: User
"""

import xlrd
from sklearn import linear_model
import numpy as np
import pandas as pd

workbook = xlrd.open_workbook('Income Statement.xls')
booksheet = workbook.sheet_by_index(1)
company = booksheet.col_values(1)
company1 = []
for i in company[1:]:
    if i not in company1:
        company1.append(i)
endtime = booksheet.col_values(5) 

endtime2 = ['2018-03-31','2017-12-31','2017-09-30','2017-06-30','2017-03-31','2016-12-31','2016-09-30','2016-06-30','2016-03-31','2015-12-31','2015-09-30','2015-06-30','2015-03-31','2014-12-31','2014-09-30','2014-06-30','2014-03-31','2013-12-31','2013-09-30','2013-06-30','2013-03-31']
all_row=[]
for r in range(len(company)):
    all_row.append(booksheet.row_values(r))


lb1 = []
lb2 = []
lb3 = []
for i in company1:
    lb1 = [i]
    lb2 = lb1*21
    for j in lb2:
        lb3.append(j)
endtime3 = endtime2*len(company1)

cogs = [0.0]*21*len(company1)
for i in range(len(all_row)):
    for j in range(len(endtime3)):
        if all_row[i][1] == lb3[j] and all_row[i][5] == endtime3[j]:
            cogs[j]=all_row[i][9]
for a in range(len(cogs)):
    if cogs[a]== 0:
        cogs[a] = cogs[a-4]
cogs1 = cogs
for n in range(1,int(21*len(company1)/4)+1):
    cogs1[4*n-3] = float(cogs[4*n-3])-float(cogs[4*n-2])
    cogs1[4*n-2] = float(cogs[4*n-2])-float(cogs[4*n-1])
    cogs1[4*n-1] = float(cogs[4*n-1])-float(cogs[4*n])


endtime5 = ['2018-03','2017-12','2017-09','2017-06','2017-03','2016-12','2016-09','2016-06','2016-03','2015-12','2015-09','2015-06','2015-03','2014-12','2014-09','2014-06','2014-03','2013-12','2013-09','2013-06','2013-03']
endtime6=endtime5*len(company1)
c = len(company1)*21
df_rev = pd.DataFrame(np.arange(2*c).reshape((c,2)),index=None, columns=['time','revenue'])
df_rev['time']=endtime6
df_rev['revenue']=cogs1
list_b = []
list_c=[]
for x in range(1,len(company1)+1):
    df_rev1 = df_rev[21*x-21:21*x]#.sort(columns = ['time'],axis = 0,ascending = True)
    list_c=[df_rev1,company1[x-1]]
    list_b.append(list_c)