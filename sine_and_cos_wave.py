import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')  #to set white grid

time = np.arange(-6.3,6.4,0.1) 

ampl1 = np.sin(time) 
ampl2 = np.cos(time)

fig = plt.figure(figsize=(12,6))
ax = fig.add_axes([0.7,0.7,0.7,0.7])

ax.plot(time,ampl1,label='SINE WAVE')
ax.plot(time,ampl2,label='COSINE WAVE')
ax.legend(loc=0)