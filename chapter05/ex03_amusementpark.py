import numpy as np
import numpy_financial as npf

loss = [-750, -250]
profit = [100] * 18
cf = loss + profit

print(cf)

cashflow = np.array(cf)
npv = npf.npv(0.045, cashflow) # DeprecationWarning: numpy.npv is deprecated and will be removed from NumPy 1.20. Use numpy_financial.npv instead
print('순현재가치:', npv)
irr = npf.irr(cashflow) # DeprecationWarning: numpy.irr is deprecated and will be removed from NumPy 1.20. Use numpy_financial.irr instead
print('내부수익률:', irr)
