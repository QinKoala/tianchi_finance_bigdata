from statsmodels.tsa.arima_model import ARMA
import numpy as np
import pandas as pd
signal = [1,2,3]
dates = pd.date_range('20130101', periods=20)
df = pd.DataFrame(np.arange(20), index=dates, columns=list('A'))
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
    return init_bic, init_p, init_q, init_properModel
print(df)
print(proper_model(df, 7))