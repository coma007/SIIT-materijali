import { TestBed } from '@angular/core/testing';

import { LoginGuard } from './login.service';

describe('LoginService', () => {
	beforeEach(() => TestBed.configureTestingModule({}));

	it('should be created', () => {
		const service: LoginGuard = TestBed.get(LoginGuard);
		expect(service).toBeTruthy();
	});
});
