import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BlogEntryPageComponent } from './blog-entry-page.component';

describe('BlogEntryPageComponent', () => {
  let component: BlogEntryPageComponent;
  let fixture: ComponentFixture<BlogEntryPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BlogEntryPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BlogEntryPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
