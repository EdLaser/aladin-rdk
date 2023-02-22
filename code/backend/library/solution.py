from typing import Dict

class Solution:
    """
    A class representing a solution to a case.

    Attributes:
        case_name (str): The name of the legal case.
        law (str): The law that applies to the case.
        number (int): The amount involved in the case.
        type_of_case (str): The type of the legal case.
        hint (str): A hint or clue related to the case.

    Methods:
        __str__(): Returns a string representation of the Solution object.
        to_dict(): Returns a dictionary representation of the Solution object.
    """

    def __init__(self,case_name="", law="", number=0, type_of_case="", hint="") -> None:
        """
        Initializes a Solution object with the specified attributes.

        Parameters:
            case_name (str): The name of the legal case. Default is an empty string.
            law (str): The law that applies to the case. Default is an empty string.
            number (int): The amount involved in the case. Default is 0.
            type_of_case (str): The type of the legal case. Default is an empty string.
            hint (str): A hint or clue related to the case. Default is an empty string.
        """
        self.case_name = case_name
        self.law = law
        self.number = number
        self.type_of_case = type_of_case
        self.hint = hint

    def __str__(self) -> str:
        """
        Returns a string representation of the Solution object.

        Returns:
            A string representation of the Solution object.
        """
        return f"Casename: {self.case_name} | Law: {self.law} | Amount: {self.number} | Type: {self.type_of_case}."

    def to_dict(self) -> Dict[str, str|int]:
        """
        Returns a dictionary representation of the Solution object.

        Returns:
            A dictionary representation of the Solution object.
        """
        return {"case_name": self.case_name, "law": self.law, "number": self.number, "type_of_case": self.type_of_case, "hint": self.hint}
