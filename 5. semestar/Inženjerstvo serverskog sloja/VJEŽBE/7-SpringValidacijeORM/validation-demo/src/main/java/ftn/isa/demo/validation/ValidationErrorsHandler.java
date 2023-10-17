package ftn.isa.demo.validation;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.List;

/*
globalna komponenta za obradu gresaka
 */
@RestControllerAdvice
public class ValidationErrorsHandler {

    @ExceptionHandler({MethodArgumentNotValidException.class})
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    protected ResponseEntity<String> handleConstraintViolationException(MethodArgumentNotValidException e) {
        List<ObjectError> errorList = e.getBindingResult().getAllErrors();
        StringBuilder sb = new StringBuilder("Request finished with validation errors: \n");

        for (ObjectError error : errorList ) {
            FieldError fe = (FieldError) error;
            sb.append(fe.getField() + " - ");
            sb.append(error.getDefaultMessage()+ "\n\n");
        }

        return new ResponseEntity<>(sb.toString(), HttpStatus.BAD_REQUEST);
    }
}
