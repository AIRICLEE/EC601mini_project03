import wave
import matplotlib.pyplot as plt
import numpy as np
import os
 
filepath = "./audioSource/" 
filename= os.listdir(filepath)  
f = wave.open(filepath+filename[1],'rb')
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

strData = f.readframes(nframes)
waveData = np.fromstring(strData,dtype=np.int16)
waveData = waveData*1.0/(max(abs(waveData)))

# plot the wave
time = np.arange(0,nframes)*(1.0 / framerate)
plt.plot(time,waveData)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("The wave data signal of single channel")
plt.grid('on')
plt.show()