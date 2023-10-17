import { TestBed, inject } from '@angular/core/testing';

import { SharedBlogEntryService } from './shared-blog-entry.service';

describe('SharedBlogEntryService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SharedBlogEntryService]
    });
  });

  it('should be created', inject([SharedBlogEntryService], (service: SharedBlogEntryService) => {
    expect(service).toBeTruthy();
  }));
});
