import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BlogEntryFormComponent } from './blog-entry-form.component';

describe('BlogEntryFormComponent', () => {
  let component: BlogEntryFormComponent;
  let fixture: ComponentFixture<BlogEntryFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BlogEntryFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BlogEntryFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
