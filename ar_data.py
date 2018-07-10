# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:35:53 2018

@author: User
"""


import xlrd
import numpy as np
import pandas as pd
import warnings
import csv
from statsmodels.tsa.arima_model import ARMA
warnings.filterwarnings("ignore")
workbook = xlrd.open_workbook('Income Statement.xls')
def generateAR(index, outputname):
    booksheet = workbook.sheet_by_index(index)
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
        if cogs[a]== 0 or cogs[a] == '':
            cogs[a] = cogs[a-4]
    cogs1 = cogs
    for n in range(1,int(21*len(company1)/4)+1):
        cogs1[4*n-3] = float(cogs[4*n-3])-float(cogs[4*n-2])
        cogs1[4*n-2] = float(cogs[4*n-2])-float(cogs[4*n-1])
        cogs1[4*n-1] = float(cogs[4*n-1])-float(cogs[4*n])

    cogs2=[float(i) for i in cogs1]
    endtime5 = ['2018-03','2017-12','2017-09','2017-06','2017-03','2016-12','2016-09','2016-06','2016-03','2015-12','2015-09','2015-06','2015-03','2014-12','2014-09','2014-06','2014-03','2013-12','2013-09','2013-06','2013-03']
    endtime6=endtime5*len(company1)
    c = len(company1)*21
    df_rev = pd.DataFrame(np.arange(2*c).reshape((c,2)),index=None, columns=['time','revenue'])
    df_rev['time']=endtime6
    df_rev['revenue']=cogs2
    list_b = []
    list_c=[]
    for x in range(1,len(company1)+1):
        df_rev1 = df_rev[21*x-21:21*x]#.sort(columns = ['time'],axis = 0,ascending = True)
        list_c=[df_rev1,company1[x-1]]
        list_b.append(list_c)
    def proper_model(data_ts, maxLag):
        init_bic = 0x7ffffff
        init_p = 0
        init_q = 0
        init_properModel = None
        for p in np.arange(maxLag):
            for q in np.arange(maxLag):
                model = ARMA(data_ts, order=(p, q))
                try:
                    results_ARMA = model.fit(disp=-1, method='css')
                except:
                    continue
                bic = results_ARMA.bic
                if bic < init_bic:
                    init_p = p
                    init_q = q
                    init_properModel = results_ARMA
                    init_bic = bic
        return init_p
    with open(outputname,"w", encoding='utf8',newline='') as f:
        writer = csv.writer(f)
        for i in list_b:
            data = i[0]['revenue']
            if not i[0].empty:
                res_p = proper_model(data, 5)
                out = []
                out.append(i[1])
                out.append(res_p)
                writer.writerow(out)
    print(outputname)
    print('Success')
generateAR(0, 'AR_general.csv')
