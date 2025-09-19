class Station:

    def __init__(self, name: str) -> None:
        self.name = name
        self.next = None

    # ------ Mutators ------

    def set_next(self, station) -> None:
        self.next = station

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    # ------ Accessors ------

    def get_next(self):
        return self.next

    def get_name(self):
        return self.name
    
    def has_next(self) -> bool:
        return self.next != None
        