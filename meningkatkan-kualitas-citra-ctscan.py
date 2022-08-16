import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# baca citra dalam mode grayscale
img = cv.imread('covid_image.png', cv.IMREAD_GRAYSCALE)
mask = cv.imread('mask.png', cv.IMREAD_GRAYSCALE)

# operasi bitwise_and
img_bitwise = cv.bitwise_and(img,img,mask=mask)

# filter
img_noiseRemov = cv.medianBlur(img_bitwise,5)

# plotting histogram
plt.subplot(2, 1, 1)
plt.hist(img_noiseRemov.ravel(),256,[0,256])
plt.xlim([0,256])
plt.show()

# perbaiki contras citra
hist,bins = np.histogram(img_noiseRemov.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img_contras = cdf[img_noiseRemov]
plt.subplot(2, 1, 2)
plt.hist(img_contras.ravel(),256,[0,256])
plt.xlim([0,256])
plt.show()

# threshold
ret,img_th = cv.threshold(img_contras,175,255,cv.THRESH_BINARY)

# menampilkan citra hasil
cv.imshow('final', img_th)

# menyimpan citra
cv.imwrite('res_bitwise.jpg',img_bitwise)
cv.imwrite('res_noise_removal.jpg',img_noiseRemov)
cv.imwrite('res_contras.jpg',img_contras)
cv.imwrite('final.jpg',img_th)

cv.waitKey(0)
cv.destroyAllWindows()