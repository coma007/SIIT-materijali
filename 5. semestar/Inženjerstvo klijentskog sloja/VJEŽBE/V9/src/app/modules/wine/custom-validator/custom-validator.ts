import { AbstractControl } from '@angular/forms';

export function yearRangeValidator(
  control: AbstractControl
): { [key: string]: boolean } | null {
  if (
    control.value !== undefined &&
    (isNaN(control.value) || control.value < 2000 || control.value > 2030)
  ) {
    return { yearRange: true };
  }
  return null;
}
