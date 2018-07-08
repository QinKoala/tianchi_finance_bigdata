from statsmodels.tsa.arima_model import ARMA
import numpy as np
import pandas as pd
import csv

signal = [1,2,3]
dates = pd.date_range('2005-03', periods=20, freq='Q')
datas = []
data = []
df = pd.DataFrame(np.arange(20), index=dates, columns=list('A'))
for i in range(20):
    data.append(df)
    data.append(str(i))
    datas.append(data)
    data = []
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
with open('ARres.csv',"w", encoding='utf8',newline='') as f:
    writer = csv.writer(f)
    for i in datas:
        res_p = proper_model(i[0], 10)
        out = []
        out.append(i[1])
        out.append(res_p)
        writer.writerow(out)