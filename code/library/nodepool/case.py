class Case:
    def __init__(self, name, subject, verb, object) -> None:
        self.name = name
        self.subject = subject
        self.verb = verb
        self.object = object

    def __str__(self) -> str:
        return f"Name of case: {self.name}\n \
            Subject: {self.subject}\n \
            Verb: {self.verb}\n \
            Object: {self.object}\n"
