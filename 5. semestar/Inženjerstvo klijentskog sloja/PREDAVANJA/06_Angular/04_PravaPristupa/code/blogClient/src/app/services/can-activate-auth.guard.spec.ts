import { TestBed, async, inject } from '@angular/core/testing';

import { CanActivateAuthGuard } from './can-activate-auth.guard';

describe('CanActivateAuthGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CanActivateAuthGuard]
    });
  });

  it('should ...', inject([CanActivateAuthGuard], (guard: CanActivateAuthGuard) => {
    expect(guard).toBeTruthy();
  }));
});
