import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule }   from '@angular/forms';

import { AppComponent } from './app.component';
import { CommentComponent } from './comment/comment.component';
import { CommentListComponent } from './comment-list/comment-list.component';
import { BlogEntryComponent } from './blog-entry/blog-entry.component';
import { BlogEntryListComponent } from './blog-entry-list/blog-entry-list.component';
import { BlogEntryFormComponent } from './blog-entry-form/blog-entry-form.component';
import { SearchEntryComponent } from './search-entry/search-entry.component';
import { EmphasizeDirective } from './directives/emphasize/emphasize.directive';
import { TitlePipe } from './pipes/title.pipe';
import { RouterModule, Routes } from '@angular/router';
import { MainPageComponent } from './pages/main-page/main-page.component';
import { BlogEntryPageComponent } from './pages/blog-entry-page/blog-entry-page.component';
import { NotFoundPageComponent } from './pages/not-found-page/not-found-page.component';
import { SharedBlogEntryService } from './services/shared-blog-entry.service';
import { BlogEntryDetailsComponent } from './blog-entry/blog-entry-details.component';
import { APP_BASE_HREF } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { BlogEntryService } from './services/blog-entry/blog-entry.service';
import { CommentFormComponent } from './comment-form/comment-form.component';
import { CommentService } from './services/comment/comment.service';

const appRoutes: Routes = [
  { path: 'main', component: MainPageComponent },
  { path: 'entry/:id',      component: BlogEntryPageComponent },
  { path: '',
    redirectTo: 'main',
    pathMatch: 'full'
  },
  { path: '**', component: NotFoundPageComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    CommentComponent,
    CommentListComponent,
    BlogEntryComponent,
    BlogEntryListComponent,
    BlogEntryFormComponent,
    SearchEntryComponent,
    EmphasizeDirective,
    TitlePipe,
    MainPageComponent,
    BlogEntryPageComponent,
    NotFoundPageComponent,
    BlogEntryDetailsComponent,
    CommentFormComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    ),
    HttpClientModule
  ],
  providers: [
    SharedBlogEntryService,
    BlogEntryService,
    CommentService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
