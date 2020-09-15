import numpy as np
import numpy_financial as npf

cf = np.array([-400, -200, 300, 300, 300, 300])
print(cf)

print(npf.irr(cf))
