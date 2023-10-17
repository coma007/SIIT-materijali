import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateWineComponent } from './create-wine.component';

describe('CreateWineComponent', () => {
  let component: CreateWineComponent;
  let fixture: ComponentFixture<CreateWineComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CreateWineComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(CreateWineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
