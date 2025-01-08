# python images folder main save then open
from PIL import Image
img=Image.open('images/images.jpg')
width=600
height=500
img=img.resize((width,height),Image.Resampling.LANCZOS)
img.save('girl.jpg')
img.show()

