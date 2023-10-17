import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WineDetailsComponent } from './wine-details.component';

describe('WineDetailsComponent', () => {
  let component: WineDetailsComponent;
  let fixture: ComponentFixture<WineDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WineDetailsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WineDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
