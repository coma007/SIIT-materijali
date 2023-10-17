import { TestBed } from '@angular/core/testing';

import { RoleGuard } from './role.service';

describe('RoleService', () => {
	beforeEach(() => TestBed.configureTestingModule({}));

	it('should be created', () => {
		const service: RoleGuard = TestBed.get(RoleGuard);
		expect(service).toBeTruthy();
	});
});
