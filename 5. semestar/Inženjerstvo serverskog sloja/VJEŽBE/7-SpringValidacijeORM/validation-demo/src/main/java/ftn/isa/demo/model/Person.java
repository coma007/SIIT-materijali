package ftn.isa.demo.model;

import ftn.isa.demo.validation.CustomConstraint;

import javax.validation.constraints.*;
import java.util.Date;

public class Person {

    private int id;

    @NotNull
    private String name;

    @NotEmpty
    private String surname;

    @Email(regexp = "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$")
    private String email;

    @CustomConstraint(message = "JMBG mora da sadrzi tacno 13 cifara")
    private String jmbg;

    @Min(value = 18)
    private int age;

    @Past     // proverava da li je datum u proslosti
    private Date dateOfBirth;

    public Person(int id, String name, String surname, String email, String jmbg, int age, Date dateOfBirth) {
        this.id = id;
        this.name = name;
        this.surname = surname;
        this.email = email;
        this.jmbg = jmbg;
        this.age = age;
        this.dateOfBirth = dateOfBirth;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setJmbg(String jmbg) {
        this.jmbg = jmbg;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setDateOfBirth(Date dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getSurname() {
        return surname;
    }

    public String getEmail() {
        return email;
    }

    public String getJmbg() {
        return jmbg;
    }

    public int getAge() {
        return age;
    }

    public Date getDateOfBirth() {
        return dateOfBirth;
    }
}
