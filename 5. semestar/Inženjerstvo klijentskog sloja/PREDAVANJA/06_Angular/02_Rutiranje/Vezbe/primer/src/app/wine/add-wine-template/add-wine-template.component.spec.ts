import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddWineTemplateComponent } from './add-wine-template.component';

describe('AddWineTemplateComponent', () => {
  let component: AddWineTemplateComponent;
  let fixture: ComponentFixture<AddWineTemplateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddWineTemplateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddWineTemplateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
