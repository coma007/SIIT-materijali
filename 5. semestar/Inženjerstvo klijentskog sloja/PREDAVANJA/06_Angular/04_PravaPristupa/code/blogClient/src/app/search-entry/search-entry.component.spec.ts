import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchEntryComponent } from './search-entry.component';

describe('SearchEntryComponent', () => {
  let component: SearchEntryComponent;
  let fixture: ComponentFixture<SearchEntryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchEntryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchEntryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
