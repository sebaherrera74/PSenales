

# Importar NumPy para esta sesión
import numpy as np
from scipy import linalg
A =np.matrix ([[ 1.  ,    1.  ,    1.5  ,   1.  ,    2.25  ,  1.5  ],
     [ 1.  ,    1.  ,    2.   ,   1.  ,    4.    ,   2.  ],
     [ 1.  ,    1.  ,    2.5  ,   1.  ,    6.25  ,  2.5  ],
     [ 1.  ,    1.5 ,    1.5  ,   2.25,    2.25  ,  2.25 ],
     [ 1.  ,    1.5 ,    2.   ,   2.25,    4.    ,  3.   ],
     [ 1.  ,    1.5 ,    2.5  ,   2.25,    6.25  ,  3.75 ],
     [ 1.  ,    2.  ,    1.5  ,   4.  ,    2.25  ,  3.   ],
     [ 1.  ,    2.  ,    2.   ,   4.  ,    4.    ,  4.   ],
     [ 1.  ,    2.  ,    2.5  ,   4.  ,    6.25  ,  5.   ]])

B=np.matrix([ 10, 10,10,6.81,4.3,0,2.00,0,-2])


print(A)
print(B)
AA=np.linalg.pinv(A)
print(AA)

x = AA * B

print("Solución del sistema:")
print(x)





