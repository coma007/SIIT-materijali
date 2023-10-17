import { Directive } from '@angular/core';
import { NG_VALIDATORS, Validator, FormControl } from '@angular/forms';
import { validateTestFactory } from '../wine/validators/custom-validator';

@Directive({
	selector: '[appCustomValidator]',
	providers: [{provide: NG_VALIDATORS, useExisting: CustomValidatorDirective, multi: true}]
})
export class CustomValidatorDirective implements Validator {
	private validator;

	constructor() {
		this.validator = validateTestFactory();
	}

	validate(c: FormControl) {
		return this.validator(c);
	}
}
