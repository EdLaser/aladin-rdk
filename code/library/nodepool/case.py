class Case:
    def __init__(self, name="", subject="", verb="", object="") -> None:
        self.name = name
        self.subject = subject
        self.verb = verb
        self.object = object

    def __str__(self) -> str:
        return f"Name of case: {self.name}\n \
            Subject: {self.subject}\n \
            Verb: {self.verb}\n \
            Object: {self.object}\n"

    def set_name(self, name: str) -> str:
        '''
        Set name of the case.

        Returns:
            self.name (str): Name of the case.
        '''
        self.name = name
        return self.name

    def set_subject(self, subject: str) -> str:
        '''Set subject of the case.

        Returns:
                self.subject (str): Subject of the case.
        '''
        self.subject = subject
        return self.subject

    def set_verb(self, verb: str) -> str:
        '''Set verb of the case.
                
        Returns:
                self.verb (str): Verb of the case.
        '''
        self.verb = verb
        return self.verb

    def set_object(self, object: str) -> str:
        '''Set object of the case.
                
        Returns:
                self.object (str): Object of the case.
        '''
        self.object = object
        return self.object
