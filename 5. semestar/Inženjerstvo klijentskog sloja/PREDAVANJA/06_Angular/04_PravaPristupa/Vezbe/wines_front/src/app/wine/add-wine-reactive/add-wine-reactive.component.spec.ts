import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddWineReactiveComponent } from './add-wine-reactive.component';

describe('AddWineReactiveComponent', () => {
	let component: AddWineReactiveComponent;
	let fixture: ComponentFixture<AddWineReactiveComponent>;

	beforeEach(async(() => {
		TestBed.configureTestingModule({
			declarations: [ AddWineReactiveComponent ]
		})
		.compileComponents();
	}));

	beforeEach(() => {
		fixture = TestBed.createComponent(AddWineReactiveComponent);
		component = fixture.componentInstance;
		fixture.detectChanges();
	});

	it('should create', () => {
		expect(component).toBeTruthy();
	});
});
