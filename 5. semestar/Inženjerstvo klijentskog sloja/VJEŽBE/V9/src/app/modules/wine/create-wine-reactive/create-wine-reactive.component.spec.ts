import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CreateWineReactiveComponent } from './create-wine-reactive.component';

describe('CreateWineReactiveComponent', () => {
  let component: CreateWineReactiveComponent;
  let fixture: ComponentFixture<CreateWineReactiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CreateWineReactiveComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(CreateWineReactiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
