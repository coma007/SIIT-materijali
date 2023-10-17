import { TestBed, inject } from '@angular/core/testing';

import { JwtUtilsService } from './jwt-utils.service';

describe('JwtUtilsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [JwtUtilsService]
    });
  });

  it('should be created', inject([JwtUtilsService], (service: JwtUtilsService) => {
    expect(service).toBeTruthy();
  }));
});
