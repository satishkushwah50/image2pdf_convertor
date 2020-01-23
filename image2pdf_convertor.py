#creating pdf 
from PIL import Image
print('convertor works with all types of image format eg. .jpg, .jpeg, .png etc ')
n=input("how many files to convert to pdf: ")
for i in range(int(n)):
	filename=input('enter name of file no '+str(i+1)+' with . extension : ')
	image1 = Image.open(filename)
	im1 = image1.convert('RGB')
	im1.save(filename.split('.')[0]+'.pdf')
	print(filename.split('.')[0]+'.pdf saved in same folder')

input('conversion done successfully, press enter to close program')