from datetime import date


class PersonalData:
    """
    Represents a data object with the following properties:

    Attributes:
        direct_fillment (bool): True if the form is being directly filled, False otherwise.
        name_of_filler_person (str): The name of the person who's filling the form.
        name (str): The name of the person for whom the form is being filled.
        age (int): The age of the person for whom the form is being filled.
        sex (bool): True for male, False for female.
        last_name (str): The last name of the person for whom the form is being filled.
        birth_date (date): The birth date of the person for whom the form is being filled.
        place_of_birth (str): The place of birth of the person for whom the form is being filled.
        adress (str): The address of the person for whom the form is being filled.
        pc (str): The postal code of the person for whom the form is being filled.
        phone_number (str): The phone number of the person for whom the form is being filled.
        work_status (bool): True if the person is currently working, False otherwise.
    """
    def __init__(self, 
                 direct_fillment: bool, 
                 name_of_filler_person: str,
                 name: str,
                 age: int, 
                 sex: bool, 
                 last_name: str, 
                 birth_date: date,
                 place_of_birth: str, 
                 adress: str, 
                 personal_id: str, 
                 phone_number: str,
                 work_status: bool):
        self.direct_fillment = direct_fillment
        self.name_of_filler_person = name_of_filler_person
        self.name = name
        self.age = age
        self.sex = sex
        self.last_name = last_name
        self.birth_date = birth_date
        self.place_of_birth = place_of_birth
        self.adress = adress
        self.personal_id = personal_id
        self.phone_number = phone_number
        self.work_status = work_status
