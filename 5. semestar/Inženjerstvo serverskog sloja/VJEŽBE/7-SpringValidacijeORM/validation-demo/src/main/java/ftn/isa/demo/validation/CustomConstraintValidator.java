package ftn.isa.demo.validation;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;

public class CustomConstraintValidator implements ConstraintValidator<CustomConstraint, String> {
    /*
        poziva se svaki put pre upotrebe instance validatora
         */
    @Override
    public void initialize(CustomConstraint string) {

    }

    /*
    vrsi validaciju custom polja koje je anotirano
     */
    @Override
    public boolean isValid(String customField, ConstraintValidatorContext ctx) {

        if (customField == null) {
            return false;
        }
        return customField.matches("[0-9]{13}");
    }

}
