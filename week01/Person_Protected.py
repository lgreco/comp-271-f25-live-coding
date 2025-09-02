class Person:
    def __init__(self, name: str, year_born: int) -> None:
        self.name: str = name
        self.year_born: int = year_born
        self.__ssn: int = -1

    def set_ssn(self, ssn: int) -> None:
        """Method to set the SSN. In reality this method will include code that checks
        the authority of the user/program attempting to modify the SSN.
        """
        self.__ssn = ssn

    def get_ssn(self) -> int:
        """Method to return the value of SSN. In practice this method will include logic
        to determine if the program/user requesting access to this field are
        authorized to do so.
        """
        return self.__ssn

if __name__ == "__main__":
    test = Person("Bob", 1985)
    test.set_ssn(111223333)
    print(test.get_ssn())