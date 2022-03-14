import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import cv2 as cv

##ENTER FILENAME HERE
filename = "33f"
img = cv.imread(f"{filename}.jpg")
cells = img[:,:,1]

##CREATING AX
fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)
ax.imshow(cells)
lower_init =50
axlower = plt.axes([0.3, 0.15, 0.63,0.025])
lower_slider = Slider(
    ax=axlower,
    label="Lower Threshold",
    valmin=0,
    valmax=256,
    valinit=lower_init,
    #orientation="horizontal"
)
upper_init = 100
axupper = plt.axes([0.3, 0.25, 0.63,0.025])
upper_slider = Slider(
    ax=axupper,
    label="Upper Threshold",
    valmin=0,
    valmax=256,
    valinit=upper_init,
    #orientation="horizontal"
)

def update(val):
    ax.clear()
    mask = cv.inRange(cells,lower_slider.val,upper_slider.val)
    ax.imshow(mask,cmap="gray")
lower_slider.on_changed(update)
upper_slider.on_changed(update)
plt.show()