import { Directive } from '@angular/core';
import { ElementRef } from '@angular/core';
import { HostListener } from '@angular/core';
import { Input } from '@angular/core';

@Directive({
  selector: '[app-emphasize]'
})
export class EmphasizeDirective {

  @Input('app-emphasize') selector: string;

  @Input() color: string;
  
  @HostListener('mouseenter') enter(){
    this.el.nativeElement.querySelectorAll(this.selector).forEach(element => {
      element.style.backgroundColor = this.color;
    });
  }

  @HostListener('mouseleave') leave(){
    this.el.nativeElement.querySelectorAll(this.selector).forEach(element => {
      element.style.backgroundColor = null;
    });
  }

  constructor(private el: ElementRef) {
  }

}
