from typing import Dict

class Solution:
    def __init__(self,case_name="", law="", number=0, type_of_case="", hint="") -> None:
        self.case_name = case_name
        self.law = law
        self.number = number
        self.type_of_case = type_of_case
        self.hint = hint

    def __str__(self) -> str:
        return f"Casename: {self.case_name} | Law: {self.law} | Amount: {self.number}."

    def to_dict(self) -> Dict[str, str|int]:
        return {"case_name": self.case_name, "law": self.law, "number": self.number, "type_of_case": self.type_of_case, "hint": self.hint}
