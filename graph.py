import numpy as np
import pylab as pl
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 , 16, 17, 18, 19, 20, 21, 22, 23]
y = [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 6, 0, 1, 1, 0, 0, 0, 1, 0, 1, 3, 3, 2, 2]
pl.ylabel('Nuemro de mascotas')
pl.xlabel('Anios de vida')
pl.plot(x, y)
pl.savefig('temp1.png')
pl.show()
