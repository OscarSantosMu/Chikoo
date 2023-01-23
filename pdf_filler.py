from PIL import Image, ImageDraw, ImageFont

# Fonts
regular_font = ImageFont.truetype('./Inter-Regular.ttf', 14)
bold_font = ImageFont.truetype('./Inter-Bold.ttf', 20)


def fill_pdf(data: dict) -> Image:
    """
        Fills the Chikoo_Document_Format image with the data of the user 
        Returns: Image class with the user's data 
    """
    image = Image.open("Document_Format.png")
    draw = ImageDraw.Draw(image)

    # Form Fillment Status
    if data['direct_fillment']:
        draw.rectangle((48, 137, 58, 147), fill=(0, 0, 0), outline=(0, 0, 0))
    else:
        draw.rectangle((114, 137, 124, 147), fill=(0, 0, 0), outline=(0, 0, 0))
        draw.text((521, 126), data['name'], fill=(0, 0, 0), font=regular_font)

    # Personal Data
    draw.text((120, 196), data['name'], fill=(0, 0, 0), font=regular_font)
    draw.text((135, 227), data['last_name'], fill=(0, 0, 0), font=regular_font)
    draw.text((120, 266), data['birth_date'],fill=(0, 0, 0), font=regular_font)
    draw.text((120, 301), data['adress'], fill=(0, 0, 0), font=regular_font)
    draw.text((168, 342), data['phone_number'],fill=(0, 0, 0), font=regular_font)
    draw.text((537, 196), data['sex'], fill=(0, 0, 0), font=regular_font)
    draw.text((537, 227), data['age'], fill=(0, 0, 0), font=regular_font)
    draw.text((386, 266), data['place_of_birth'],fill=(0, 0, 0), font=regular_font)
    draw.text((525, 301), data['pc'], fill=(0, 0, 0), font=regular_font)
    draw.text((558, 342), data['work_status'],fill=(0, 0, 0), font=regular_font)

    image.save("chikoo.png")

    return image
