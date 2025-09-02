from Person_Protected import Person
person1 = Person("Alice", 1990)
print(person1.__ssn) # Will cause error; comment out after demo
print(person1._Person__ssn) # Will print -1
person1.__ssn = 111223333 # Has no effect:
print(person1._Person__ssn) # Still prints -1
person1._Person__ssn = 111223333 # This works
print(person1._Person__ssn) # Now prints 111223333