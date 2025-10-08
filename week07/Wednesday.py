class SomeFunnyClassWeWroteInClass:

    """A simple class to demonstrate __str__ and __repr__ methods. 
    
    Special method __str__ is used to find the “informal” or nicely printable string representation of an object.
    This is the method that is called by the built-in str() function and by the print function to compute the string representation of an object.
    
    On the other hand, __repr__ is used to find the “official” string representation of an object.
    This is the method that is called by the built-in repr() function and is used for debugging and development.
    The goal of __repr__ is to be unambiguous and, if possible, match the code necessary to recreate the object.
    """

    def __init__(self, fname, lname):
        """Initialize the object with first and last names."""
        self.fname = fname
        self.lname = lname

    def get_fname(self):
        """Return the first name of the person."""
        return self.fname
    
    def __str__(self):
        """Always implement the __str__ method."""
        return self.get_fname()
    
    def __repr__(self):
        """Nice to have the __repr__ method implemented."""
        # Return the name of the class and the field names and values.
        return f"{self.__class__.__name__}('{self.fname=}', '{self.lname=}')"
    

# Example usage:
test = SomeFunnyClassWeWroteInClass("Gandalf", "The White")

# Demonstrate the difference between __str__ and __repr__

print(str(test)) # Same as print(test)
print(repr(test)) # This forces a more detailed representation