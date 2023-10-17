import { AbstractControl, ValidatorFn } from '@angular/forms';

export function validateTestFactory(): ValidatorFn {
	return (c: AbstractControl) => {
		const isValid = c.value === 'Stefan';

		if (isValid) {
			return null;
		} else {
			return {
				testError: {
					valid: false
				}
			};
		}
	};
}
