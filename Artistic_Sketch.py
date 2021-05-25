import cv2
from PIL import Image
import os

#Define the Image
image = Image.open('C:/Users/PC/Documents/RG.jpg')
print(image.size)

#Resize Image
resized_image = image.resize((400, 400))
resized_image.save('resized_image.jpg')
os.getcwd()

print(resized_image.size)

#Read Image
img = cv2.imread('C:/Users/PC/resized_image.jpg')

#Image Preprocessing
grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert Pixels
inverted = cv2.bitwise_not(grayed)

#Add Blurriness
#Blurs an image using a Gaussian filter. This will give the sketch effect to the final artwork
blurred = cv2.GaussianBlur(inverted, (19,19 ), sigmaX=0, sigmaY=0)

#Blending the Artwork
def blend(x, y):
    return cv2.divide(x, 255 - y, scale=256)

#call the function by passing in the images that we want to blend
final_result = blend(grayed, blurred)

#Export the Result
cv2.imwrite("my_artwork.jpg", final_result)
os.getcwd()
