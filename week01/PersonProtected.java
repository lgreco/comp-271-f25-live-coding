public class PersonProtected {
    private String name;
    private int yearBorn;
    private int ssn;

    /** Full constructor */
    public PersonProtected(String name, int yearBorn) {
        this.name = name;
        this.yearBorn = yearBorn;
    }

    /**
     * Method to set the SSN. In reality this method will include code that checks
     * the authority of the user/program attempting to modify the SSN.
     */
    public void setSsn(int ssn) {
        this.ssn = ssn;
    }

    /**
     * Method to return the value of SSN. In practice this method will include logic
     * to determine if the program/user requesting access to this field are
     * authorized to do so.
     */
    public int getSsn() {
        return ssn;
    }
}