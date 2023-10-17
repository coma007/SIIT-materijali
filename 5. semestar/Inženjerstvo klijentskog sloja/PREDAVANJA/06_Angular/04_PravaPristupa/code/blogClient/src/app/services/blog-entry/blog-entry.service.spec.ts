import { TestBed, inject } from '@angular/core/testing';

import { BlogEntryService } from './blog-entry.service';

describe('BlogEntryService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [BlogEntryService]
    });
  });

  it('should be created', inject([BlogEntryService], (service: BlogEntryService) => {
    expect(service).toBeTruthy();
  }));
});
