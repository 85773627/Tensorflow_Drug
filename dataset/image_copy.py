from PIL import Image
img = Image.open('Drugimages/drug1.jpg')
xsize = 130
ysize = 130
for i  in range(1, 1000):
    print i
    img2 = img.resize((xsize, ysize))
    img2 = img2.rotate(i-1)
    img2.save('Drugimages/drug'+str(i)+'.jpg')
