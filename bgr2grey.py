import cv2
image=cv2.imread("c.jpeg")
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 350,350)
cv2.imshow('Original',image)


grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Greyscale', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Greyscale', 350,350)
cv2.imshow('Greyscale',grey_image)
#cv2.imwrite("01.jpg",grey_image)


cv2.waitKey(0)

cv2.destroyAllWindows()
