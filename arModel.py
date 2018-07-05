from statsmodels.tsa.ar_model import AR
import numpy as np
import pandas as pd
signal = [1,2,3]
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame([1,2,3,4,5,6], index=dates, columns=list('A'))
ar_mod = AR(df, freq='D')
ar_res = ar_mod.fit(2)

res = ar_res.predict('2013-01-04', '2013-01-10')
print(res)