from PIL import Image, ImageDraw, ImageFont

image = Image.open("labrador.jpg")
draw = ImageDraw.Draw(image)

# Define the position and text
position = (10, 10)
text = "Labrador Golden Retriever"

# Draw the text on the image
draw.text(position, text, fill=(255,255,255))
image.show()
