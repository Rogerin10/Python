#Encuentra el promedio, la suma y la desviacion estandar de un array

import numpy as np
calificaciones =[9, 10, 8, 9, 7]
varianza = np.var(calificaciones, ddof = 1)
print("la varianza es de: ", varianza) #la varianza es de:  1.2999999999999998

desviacion_estandar = np.sqrt(varianza)
print("la desviacion estandar es de: ", desviacion_estandar) #la desviacion estandar es de:  1.1401754250991378
