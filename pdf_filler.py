from typing import Optional
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

    # Familiar History
    fill_familiar_history(draw, 'cancer', 'father')
    fill_familiar_history(draw, 'alcoholism', 'father')
    fill_familiar_history(draw, 'arthritis', 'father')
    fill_familiar_history(draw, 'depression', 'father')
    fill_familiar_history(draw, 'diabetes', 'father')
    fill_familiar_history(draw, 'obesity', 'father')
    fill_familiar_history(draw, 'pressure', 'father')
    fill_familiar_history(draw, 'smoking', 'father')
    fill_familiar_history(draw, 'smoking', 'father')
    fill_familiar_history(draw, 'other', 'father', 'bipolarity')

    image.save("chikoo.png")

    return image


def fill_familiar_history(draw: ImageDraw, type: Optional[str] = None, familiar: Optional[str] = None, other: Optional[str] = None):
    """
        Fills with an X the disease that one of the familiars had.

        type: Optional[str] = None by default, represents the type of disease that a familiar had 
        familiar: Optional[str] = None by default, represents the familiar who had a disease
        other: Optional[str] = None by default, represents if a familiar had another kind of disease or hederitary disease
    """
    types = {
        'alcoholism': 450,
        'arthritis': 465,
        'cancer': 480,
        'hearth':495,
        'depression': 510,
        'diabetes': 525,
        'obesity': 540,
        'pressure': 555,
        'smoking': 570,
        'other': 585,
    }

    familiars = {
        'mother': 178,
        'father': 274,
        'brothers': 370,
        'grand_parents': 466,
        'patient_doesnt_know': 620,
    }

    if familiar:
        if other:
            draw.text(
                (familiars[familiar]-40, types[type]),
                other,
                fill=(137, 87, 254),
                font=regular_font
            )
        else:
            draw.text(
                (familiars[familiar], types[type]),
                'X',
                fill=(137, 87, 254), font=regular_font
            )
    return
