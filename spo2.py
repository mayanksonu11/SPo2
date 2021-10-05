#!/usr/bin/env python3.7.5
import cv2
import numpy as np
import time

def average(image):
	width = image.shape[1]
	height = image.shape[0]
	sum =0
	for i in range(0,height):
		for j in range(0,width):
			sum = sum +image[i][j]
	return sum/(width*height)

def stddev(image, mean):
	width = image.shape[1]
	height = image.shape[0]
	sum =0
	for i in range(0,height):
		for j in range(0,width):
			sum = sum + (image[i][j]-mean)**2
	sum = sum/(width*height)
	return np.sqrt(sum)		


average_red = []
std_red = []
average_blue = []
std_blue = []
spo2= []

image_name = "sample.jpg"
image = cv2.imread(image_name)
(B, G, R) = cv2.split(image)
mean = average(B)
std = stddev(B,mean)
average_blue.append(mean)
std_blue.append(std)
mean = average(R)
std = stddev(R,mean)
average_red.append(mean)
std_red.append(std)
print(image_name, "Under Processing")

for i in range(0,len(std_blue)):
	spo2.append(100-5*(std_red[i]/average_red[i])/(std_blue[i]/average_blue[i]))

print(sum(spo2)/len(spo2))
