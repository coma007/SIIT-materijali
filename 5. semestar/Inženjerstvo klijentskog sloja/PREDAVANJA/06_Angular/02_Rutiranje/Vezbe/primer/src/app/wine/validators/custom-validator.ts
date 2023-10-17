import { AbstractControl, ValidatorFn } from '@angular/forms';

// validation function
export function validateStefanNameFactory() : ValidatorFn {
  return (c: AbstractControl) => {
    
        let isValid = c.value === 'Stefan';

        if(isValid) {
            return null;
        } else {
            return {
                stefanName: {
                    valid: false
                }
            };
        }
    }
}
