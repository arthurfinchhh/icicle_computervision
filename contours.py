import cv2 as cv
import csv
import numpy as np
import matplotlib.pyplot as plt

im = cv.imread('   .jpg')
gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
(thresh, bw) = cv.threshold(gray, 87, 256, cv.THRESH_BINARY)

center = (960,540)
scale = 0.5
angle = 90

M = cv.getRotationMatrix2D(center, angle, scale)
rotated = cv.warpAffine(bw, M, (1080,1920)) #adjusted for new webcam, old = 720, 1280

imdraw = cv.selectROI(bw)

cropped = im[int(imdraw[1]):int(imdraw[1]+imdraw[3]), int(imdraw[0]):int(imdraw[0]+imdraw[2])]

cont = cv.Canny(cropped, 255, 255/3) #adjusted for new webcam, old = 1280, 720
contours, heirarchy = cv.findContours(cont, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)


working = np.zeros(0)
xvals = np.zeros(0)
yvals = np.zeros(0)

print(len(contours))


for i in range(len(contours)):
    working = contours[i]
    xvals = np.append(xvals, working[:,:,0])
    yvals = np.append(yvals, working[:,:,1])

plt.scatter(xvals,yvals)
plt.show()


with open('xycord.csv', 'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(xvals)
    writer.writerow(yvals)



for i in range(len(contours)):
   arc = cv.arcLength(contours[i],False)
   main = np.amax(arc)

    # if arc > 1000:
    #     plt.plot
print(main)

#cv.imshow('contours', main)
cv.waitKey(0)
cv.destroyAllWindows()
