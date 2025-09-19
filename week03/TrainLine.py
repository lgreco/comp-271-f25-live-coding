class TrainLine:

    def __init__(self, name):
        self.name = name
        self.head = None

    # ------ accessors and mutators ------
    def get_name(self) -> str:
        return self.name

    def is_empty(self) -> bool:
        return self.head == None

    # ------ add a new station ------

    def add_station(self, new_station):
        if self.head == None:
            # Line is empty; new station becomes the head of the line
            self.head = new_station
        else:
            # traverse the line to find its last station
            current_station = self.head
            while current_station.has_next():
                current_station = current_station.get_next()
            # When this loop ends it's because cursor.has_next is False,
            # therefore we are standing at the end of the line
            current_station.set_next(new_station)
    
    