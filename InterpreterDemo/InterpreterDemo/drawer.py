#encoding=utf-8

import matplotlib.pyplot as pl
#import matplotlib.pylab as pl
import numpy as np

pl.figure(1,figsize=(8,6))
ax1=pl.subplot(211)
x=np.linspace(0,7,100)
pl.sca(ax1)
plot1=pl.plot(x,np.sin(x),label='sin')
plot2=pl.plot(x,np.cos(x),label='cos')
pl.legend()
#pl.show()

pl.figure(2)
pl.title('W=BMI*H*H')
pl.xlabel('Height')
pl.ylabel('Weight')
pl.xlim(1.4,2.0)
pl.ylim(40,100)
pl.plot([1.5,1.7,1.6],[60,70,60])

pl.show()