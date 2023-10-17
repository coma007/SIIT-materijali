import { Injectable } from '@angular/core';
import { BlogEntry } from '../model/blogEntry';

@Injectable()
export class SharedBlogEntryService {

  blogEntry:BlogEntry;

  constructor() { }

}
