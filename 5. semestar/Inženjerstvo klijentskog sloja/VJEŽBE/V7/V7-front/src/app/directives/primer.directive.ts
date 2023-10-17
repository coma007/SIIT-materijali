import { Directive, ElementRef, HostListener } from '@angular/core';

@Directive({
  selector: '[appPrimer]',
})
export class PrimerDirective {
  constructor(private el: ElementRef) {}

  @HostListener('mouseenter') mouseEneter() {
    this.el.nativeElement.style.backgroundColor = 'red';
  }

  @HostListener('mouseleave') mouseLeave() {
    this.el.nativeElement.style.backgroundColor = 'transparent';
  }
}
