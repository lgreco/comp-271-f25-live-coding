from Guest import Guest

class HotelAlphabetical:

    _NUMBER_OF_LETTERS = 26
    _ASCII_OFFSET = ord("A")  # 65

    def __init__(self):
        self._underlying = [None] * self._NUMBER_OF_LETTERS
        self._total_guests = 0
        self._rooms_used = 0

    def add(self, guest_name):
        first_letter = guest_name.upper()[0]
        index = ord(first_letter) - self._ASCII_OFFSET
        if index >= 0 and index < self._NUMBER_OF_LETTERS:
            # ensured that the first character of guest name is actually
            # an upper case letter. Encapsulate the guest in a node
            new_guest = Guest(guest_name)
            # Now check is the room at position index is free
            if self._underlying is None:
                # Room is free place your guest here.
                self._underlying[index]
                self._rooms_used += 1
            else:
                new_guest.next = self._underlying[index]
                self._underlying[index] = new_guest
        self._total_guests += 1
