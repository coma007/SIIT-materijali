import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'test',
})
export class TestPipe implements PipeTransform {
  transform(value: any, ...args: any[]): any {
    const obj: any = JSON.parse(value);

    if (obj.name && obj.name.length === 7) {
      return 'Testni pajp';
    }
    return null;
  }
}
