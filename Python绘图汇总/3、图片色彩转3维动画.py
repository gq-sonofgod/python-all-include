from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
from PIL import Image
#import matplotlib.animation as animation 
import numpy as np 
 
img = Image.open('test.jpg')
grayImg = img.convert('L')
width, height = grayImg.size
X, Y = np.meshgrid(np.arange(0,width), np.arange(0,height))
# print(X)
Z = np.array(grayImg)
print("1")
fig = plt.figure() 
print("2")
ax = fig.gca(projection='3d')
print("3")
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap='viridis')
print("4")
transition = lambda x,N: (1+np.sin(-0.5*np.pi+2*np.pi*x / (1.0*N)))/2.0
print("5")
for i in range (40):
	horiAngle=45+50*transition(i,40)
	vertAngle=50+43*transition(i,40)
	
	ax.view_init(vertAngle,horiAngle)
	filename='animFram/'+str('%03d'%i)+'.png'
	plt.savefig(filename, dpi=96)