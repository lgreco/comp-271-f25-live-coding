public class PersonImplementation {
    public static void main(String[] args) {
        PersonExposed person1 = new PersonExposed("Alice", 1990);
        PersonProtected person2 = new PersonProtected("Bob", 1985);
        person1.ssn = 111223333;
        person2.ssn = 111223333; // program wont even compile!
    }
}