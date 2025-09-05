from datetime import datetime # for age computations

class Person:
    def __init__(self, name: str, year_born: int) -> None:
        self.name: str = name
        self.year_born: int = year_born
        self.__ssn: int = -1

    def __str__(self):
        """String representation for the object."""
        return f"Person: [{self.name}, age {datetime.now().year-self.year_born}]"

    def __lt__(self, other) -> bool:
        """Establishes a natural ordering between Person objects based on age.
        In this context, less means that the invoking person (self) is born
        on a later year than the referenced person (other)"""
        return self.year_born > other.year_born
            
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
    # print(test.get_ssn())

    person1 = Person("Gandalf", 1000)
    person2 = Person("Smeagol", 1500)

    if person1 < person2:
        print(f"{person1} is younger than {person2}")
    else:
        print(f"{person1} is at least as old as {person2}")