import { Directive } from '@angular/core';
import { NG_VALIDATORS, Validator, FormControl } from '@angular/forms';
import { validateStefanNameFactory } from '../wine/validators/custom-validator';

@Directive({
  selector: '[appStefanNameValidator]',
  providers: [{provide: NG_VALIDATORS, useExisting: StefanNameValidatorDirective, multi: true}]
})
export class StefanNameValidatorDirective implements Validator {
  private validator

  constructor() {
    this.validator = validateStefanNameFactory()
  }

  validate(c: FormControl) {
    return this.validator(c);
  }

}
