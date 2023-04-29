from typing import Optional, Dict
from PIL import Image, ImageDraw, ImageFont

# Fonts
FONT_REGULAR = ImageFont.truetype('./static/Inter-Regular.ttf', 14)
FONT_BOLD = ImageFont.truetype('./static/Inter-Bold.ttf', 20)
IMAGE_PATH = "./static/img/Document_Format.png"
FOOD_CONVERSION = {'milk': 0, 'meat': 1,
                   'eggs': 2, 'vegetables': 3, 'cereals': 4}
NON_PATHOLOGICAL_X_POSITIONS = {0: 173, 1: 270, 2: 367, 3: 456, 4: 615}
NON_PATHOLOGICAL_Y_POSITIONS = {
    'physical_activity': 816,
    'tabaco': 920,
    'alcohol': 1016,
    'drugs': 1120
}


class ChikooDocument:
    """
    A class to create a ChikooDocument image based on given data, foods_per_week, family_history, and activities.

    Attributes:
        image (Image): The base image for the document format.
        draw (ImageDraw): The drawing context for the image.
        regular_font (ImageFont): The regular font for drawing text.
        bold_font (ImageFont): The bold font for drawing text.
        data (Dict): A dictionary containing personal data.
        family_history (Dict): A dictionary containing family history data.
        foods_per_week (Dict): A dictionary containing foods consumed per week data.
        activities (Dict): A dictionary containing activities data.
        food_conversion (Dict): A dictionary for converting food names to their respective y_positions.
        non_pathological_x_positions (Dict): A dictionary containing x_positions for non-pathological data.
        non_pathological_y_positions (Dict): A dictionary containing y_positions for non-pathological data.

    Methods:
        _form_fillment_status(): Fills the form fillment status on the document.
        _fill_personal_data(): Fills the personal data section on the document.
        _set_family_history_row(disease: str, familiar: str): Fills a specific row for the family history section.
        _fill_family_history(): Fills the family history section on the document.
        _fill_non_pathologic_row(): Fills the non-pathologic row on the document.
        _fill_food(): Fills the food section on the document.
        create_document(): Generates the ChikooDocument image based on the input data.
    """

    def __init__(self, data: Dict, foods_per_week: Dict, family_history: Dict, activities: Dict) -> None:
        self.image = Image.open("./static/img/Document_Format.png")
        self.draw = ImageDraw.Draw(self.image)
        self.regular_font = FONT_REGULAR
        self.bold_font = FONT_BOLD
        self.data = data
        self.family_history = family_history
        self.foods_per_week = foods_per_week
        self.activities = activities
        self.non_pathological_x_positions = NON_PATHOLOGICAL_X_POSITIONS
        self.non_pathological_y_positions = NON_PATHOLOGICAL_Y_POSITIONS
        self.food_conversion = FOOD_CONVERSION

    def _form_fillment_status(self) -> None:
        """
        Fills the form fillment status on the document based on the 'direct_fillment' field in the data dictionary.
        """

        if self.data['direct_fillment']:
            self.draw.rectangle((48, 137, 58, 147), fill=(0, 0, 0))
        else:
            self.draw.rectangle((114, 137, 124, 147), fill=(0, 0, 0))
            self.draw.text((521, 126), self.data["name"], fill=(0, 0, 0), font=self.regular_font)

    def _fill_personal_data(self) -> None:
        """
        Fills the personal data section on the document using the values from the data dictionary.
        """
        text_positions = [
            (120, 196, "name"),
            (135, 227, "last_name"),
            (120, 266, "birth_date"),
            (120, 301, "adress"),
            (168, 342, "phone_number"),
            (537, 196, "sex"),
            (537, 227, "age"),
            (386, 266, "place_of_birth"),
            (525, 301, "pc"),
            (558, 342, "work_status"),
        ]
        for x, y, field in text_positions:
            self.draw.text((x, y), self.data[field], fill=(0, 0, 0), font=self.regular_font)


    def _set_family_history_row(self, disease: str, familiar: str) -> None:
        """
        Fills a specific row for the family history section on the document based on the given disease and familiar.

        Args:
            disease (str): The disease to be filled in the family history section.
            familiar (str): The familiar relationship associated with the disease.
        """
        
        types = {
            "alcoholism": 450,
            "arthritis": 465,
            "cancer": 480,
            "hearth": 495,
            "depression": 510,
            "diabetes": 525,
            "obesity": 540,
            "pressure": 555,
            "smoking": 570,
            "other": 585,
        }

        familiars = {
            "mother": 178,
            "father": 274,
            "brothers": 370,
            "grand_parents": 466,
            "patient_doesnt_know": 620,
        }

        self.draw.text(
            (familiars[familiar], types[disease]),
            "X",
            fill=(137, 87,254), font=self.regular_font
        )
        
    def _fill_family_history(self) -> None:
        """
        Fills the family history section on the document using the values from the family_history dictionary.
        """
        for disease, familiar in self.family_history.items():
            self._set_family_history_row(disease, familiar)

    def _fill_non_pathologic_row(self) -> None:
        """
        Fills the non-pathologic row on the document using the values from the activities dictionary.
        """
        for activity, times_per_week in self.activities.items():
            self.draw.text(
                (self.non_pathological_x_positions[times_per_week],
                self.non_pathological_y_positions[activity]),
                str(times_per_week),
                fill=(137, 87, 254),
                font=self.regular_font
            )

    def _fill_food(self) -> None:
        """
        Fills the food section on the document using the values from the foods_per_week dictionary.
        """
        for food, times_per_week in self.foods_per_week.items():
            print(food, times_per_week)
            self.draw.text(
                (self.non_pathological_x_positions[self.food_conversion[food]],
                716),
                str(times_per_week),
                fill=(137, 87, 254),
                font=self.regular_font
            )

    def create_document(self) -> Image:
        """
        Generates the ChikooDocument image based on the input data by calling the private methods for filling
        different sections of the document.

        Returns:
            Image: The generated ChikooDocument image.
        """
        self._form_fillment_status()
        self._fill_personal_data()
        self._fill_family_history()
        self._fill_non_pathologic_row()
        self._fill_food()
        self.image.save("chikoo.png")
        
        return self.image

