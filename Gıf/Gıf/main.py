from PIL import Image


filenames = ['images.jpeg','images2.jpg']
images =[]

for filename in filenames:
    images.append(Image.open(filename))

images[0].save('images.gif',
               save_all=True,
               append_images=images[1:],
               duration=500,
               loop=0)