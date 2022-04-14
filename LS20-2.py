
import pandas as pd
import numpy as np
import matplotlib

returns = pd.read_csv("/data/Portfolios_Formed_on_ME_monthly_EW.csv",
                     header=0, index_col=0, parse_dates=True,na_values=-99.99


returns

columns = ["Lo 20", "Hi 20"]
returns = returns[columns]
returns.columns = ['SmallCap20', 'LargeCap20']
returns.head()

returns.plot.line()

returns.std()

returns = returns/100
returns

returns.columns = ['SmallCap20', 'LargeCap20']
returns.head()

returns.plot.line()


n_months = returns.shape[0]
return_per_month = (returns+1).prod()**(1/n_months) - 1
return_per_month

annualized_vol = returns.std()*np.sqrt(12)
annualized_vol

annualzied_returns = (return_per_month+1)**12 -1
annualzied_returns

