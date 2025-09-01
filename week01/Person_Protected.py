class Person:
    def __init__(self, name: str, year_born: int) -> None:
        self.name: str = name
        self.year_born: int = year_born
        self.__ssn: int = -1

if __name__ == "__main__":
    pass