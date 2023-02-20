class Case:
    """
    A class that represents a case.

    Parameters:
        name (str): The name of the case.
        subject (str): The subject of the case.
        verb (str): The verb of the case.
        object (str): The object of the case.
        number (int): The amount given in the case.

    Methods:
        __init__(self, name="", subject="", verb="", object="", number=0) -> None:
            Initializes a new instance of the Case class.

        __str__(self) -> str:
            Returns a string representation of the case.

        __repr__(self) -> str:
            Returns a string representation of the case.

        __eq__(self, other) -> bool:
            Compares two instances of the Case class for equality.

        set_name(self, name: str) -> str:
            Sets the name of the case.

        set_subject(self, subject: str) -> str:
            Sets the subject of the case.

        set_verb(self, verb: str) -> str:
            Sets the verb of the case.

        set_object(self, object: str) -> str:
            Sets the object of the case.

        set_number(self, number: int) -> int:
            Sets the amount given in the case.

        to_dict(self) -> Dict:
            Converts the case to a dictionary.
    """

    def __init__(self, name="", subject="", verb="", object="", number=0) -> None:
        """
        Initializes a new Case object with the given parameters.

        Parameters:
            name (str): Name of the case.
            subject (str): Subject of the case.
            verb (str): Verb of the case.
            object (str): Object of the case.
            number (int): Amount given in the case.
        """
        self.name = name
        self.subject = subject
        self.verb = verb
        self.object = object
        self.number = number

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the Case object.
        """
        return f"Name of case: {self.name} Subject: {self.subject} Verb: {self.verb} Object: {self.object} Number: {self.number}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Case object.
        """
        return f"Name of case: {self.name} Subject: {self.subject} Verb: {self.verb} Object: {self.object} Number: {self.number}"

    def __eq__(self, other) -> bool:
        """
        Compares the Case object with another object to check if they are equal.

        Parameters:
            other (Case): The other Case object to compare.

        Returns:
            bool: True if the two objects have the same name, False otherwise.
        """
        return self.name == other.name 

    def set_name(self, name: str) -> str:
        """
        Sets the name of the Case object.

        Parameters:
            name (str): The new name of the Case object.

        Returns:
            str: The updated name of the Case object.
        """
        self.name = name
        return self.name

    def set_subject(self, subject: str) -> str:
        """
        Sets the subject of the Case object.

        Parameters:
            subject (str): The new subject of the Case object.

        Returns:
            str: The updated subject of the Case object.
        """
        self.subject = subject
        return self.subject

    def set_verb(self, verb: str) -> str:
        """
        Sets the verb of the Case object.

        Parameters:
            verb (str): The new verb of the Case object.

        Returns:
            str: The updated verb of the Case object.
        """
        self.verb = verb
        return self.verb

    def set_object(self, object: str) -> str:
        """
        Sets the object of the Case object.

        Parameters:
            object (str): The new object of the Case object.

        Returns:
            str: The updated object of the Case object.
        """
        self.object = object
        return self.object

    def set_number(self, number: int) -> int:
        """
        Sets the amount of the Case object.

        Parameters:
            number (int): The new amount of the Case object.

        Returns:
            int: The updated amount of the Case object.
        """
        self.number = number
        return self.number

    def to_dict(self):
        """
        Returns a dictionary representation of the Case object.
        """
        return {"name": self.name, "subject": self.subject, "verb": self.verb, "object": self.object, "number": self.number}
