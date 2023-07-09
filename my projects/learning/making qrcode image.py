import qrcode

data = "Lorem ipsum"

img = qrcode.make(data)

img.save("C:/Users/Kaziu/Desktop/Python/my projects/learning/learning data/myqrcode.png")