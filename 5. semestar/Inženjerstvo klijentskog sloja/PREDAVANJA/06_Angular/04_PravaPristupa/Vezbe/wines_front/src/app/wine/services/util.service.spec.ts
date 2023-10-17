import { TestBed } from '@angular/core/testing';

import { UtilService } from './util.service';

describe('UtilService', () => {
	beforeEach(() => TestBed.configureTestingModule({}));

	it('should be created', () => {
		const service: UtilService = TestBed.get(UtilService);
		expect(service).toBeTruthy();
	});
});
