import { TestBed } from '@angular/core/testing';

import { WineService } from './wine.service';

describe('WineService', () => {
	beforeEach(() => TestBed.configureTestingModule({}));

	it('should be created', () => {
		const service: WineService = TestBed.get(WineService);
		expect(service).toBeTruthy();
	});
});
