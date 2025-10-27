from Guest import *

class HotelAlphabetical:

    _DEFAULT_ROOMS = 4
    _ASCII_OFFSET = ord("A")  # 65
    _DEFAULT_LOAD_THRESHOLD = 0.75
    _RESIZE_BY = 2

    def __init__(self, size:int = _DEFAULT_ROOMS):
        """ Initialize the hotel with a given number of rooms """
        self._size = size
        self._underlying = [None] * size
        self._total_guests = 0
        self._rooms_used = 0
        self._load_factor = 0.0 # fraction of rooms occupied

    def _get_load_factor(self):
        """ Return the current load factor of the hotel """
        return self._rooms_used / self._size

    def _room(self, guest_name: str, size:int) -> int:
        """ Return the room index for a given guest name """
        # Just in case the guest name is illegit, return room 0
        room = 0
        if guest_name is not None:
            # Compute the room index based on the first character of the guest name
            room = ord(guest_name.upper()[0]) % size
        return room
    
    def add(self, guest_name):
        """ Add a guest to the hotel """
        # Assign a room for this guest
        room = self._room(guest_name, self._size)
        # Check that the room index is valid
        if room >= 0 and room < self._size:
            # We have a valid room index and have ensured that the first character
            # of guest name is actually an upper case letter. 
            # Encapsulate the guest in a node
            new_guest = Guest(guest_name)
            # Check load factor and rehash if necessary
            if self._get_load_factor() >= self._DEFAULT_LOAD_THRESHOLD:
                # rehash
                self._rehash()
            # Now check if the room is free
            if self._underlying[room] is None:
                # Room is free place your guest here.
                self._underlying[room] = new_guest
                self._rooms_used += 1
            else:
                # Collision: place the new guest at the head of the linked list
                new_guest.next = self._underlying[room]
                self._underlying[room] = new_guest
        # Increment total guests
        self._total_guests += 1

    def _rehash(self):
        """ Rehash the hotel to a larger size """
        # build a larger hotel
        larger_hotel = HotelAlphabetical(self._RESIZE_BY*self._size)
        # Move guests from current hotel to the larger hotel
        for guest in self:
            larger_hotel.add(guest.name)
        # New hotel is done. We can pass the new hotel's attributes to the
        # current hotel instance using the object's __dict__ attribute. 
        self.__dict__.update(larger_hotel.__dict__)
        # For something less pythonic, we could manually copy each attribute.
        # In this case, we need update only _underlying and _size, since
        # _total_guests and _rooms_used are already correct.


    def __iter__(self):
        """ Iterate over all guests in the hotel """     
        for room in self._underlying:
            occupant = room
            while occupant is not None:
                yield occupant
                occupant = occupant.next    

    def __str__(self) -> str:
        """ String representation of the hotel """
        hotel_string = f"Your hotel has {len(self._underlying)} rooms."
        hotel_string += f"\n{self._rooms_used} room(s) used currently."
        hotel_string += f"\nNumber of guests: {self._total_guests}"
        hotel_string += f"\nCurrent load factor is {self._get_load_factor():.2f}, threshold is {self._DEFAULT_LOAD_THRESHOLD:.2f}"
        for room in range(len(self._underlying)):
            hotel_string += f"\nRoom [{room:03d}]: "
            if self._underlying[room] is not None:
                guest = self._underlying[room]
                while guest is not None:
                    hotel_string += f"{guest.name} --> "
                    guest = guest.next
        return hotel_string