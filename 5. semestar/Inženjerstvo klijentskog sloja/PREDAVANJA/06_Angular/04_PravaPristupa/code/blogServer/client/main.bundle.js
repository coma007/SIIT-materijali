webpackJsonp(["main"],{

/***/ "../../../../../src/$$_lazy_route_resource lazy recursive":
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncatched exception popping up in devtools
	return Promise.resolve().then(function() {
		throw new Error("Cannot find module '" + req + "'.");
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "../../../../../src/$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "../../../../../src/app/app.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/app.component.html":
/***/ (function(module, exports) {

module.exports = "<div class=\"container\">\n  <!-- Static navbar -->\n  <nav class=\"navbar navbar-default\">\n    <div class=\"container-fluid\">\n      <div id=\"navbar\" class=\"navbar-collapse collapse\">\n        <ul class=\"nav navbar-nav navbar-right\">\n          <li>\n            <a *ngIf=\"!loggedIn()\" (click)=\"login()\">login</a>\n          </li>\n          <li>\n            <a *ngIf=\"loggedIn()\" (click)=\"logout()\">logout</a>\n          </li>\n        </ul>\n      </div>\n      <!--/.nav-collapse -->\n    </div>\n    <!--/.container-fluid -->\n  </nav>\n  <router-outlet></router-outlet>\n</div>"

/***/ }),

/***/ "../../../../../src/app/app.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__services_authentication_service_service__ = __webpack_require__("../../../../../src/app/services/authentication-service.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_router__ = __webpack_require__("../../../router/esm5/router.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var AppComponent = (function () {
    function AppComponent(authService, router) {
        this.authService = authService;
        this.router = router;
    }
    AppComponent.prototype.ngOnInit = function () {
    };
    AppComponent.prototype.loggedIn = function () {
        return this.authService.isLoggedIn();
    };
    AppComponent.prototype.login = function () {
        this.router.navigate(['login']);
    };
    AppComponent.prototype.logout = function () {
        this.authService.logout();
        this.router.navigate(['main']);
    };
    AppComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-root',
            template: __webpack_require__("../../../../../src/app/app.component.html"),
            styles: [__webpack_require__("../../../../../src/app/app.component.css")]
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__services_authentication_service_service__["a" /* AuthenticationService */],
            __WEBPACK_IMPORTED_MODULE_2__angular_router__["b" /* Router */]])
    ], AppComponent);
    return AppComponent;
}());



/***/ }),

/***/ "../../../../../src/app/app.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__ = __webpack_require__("../../../platform-browser/esm5/platform-browser.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_forms__ = __webpack_require__("../../../forms/esm5/forms.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__app_component__ = __webpack_require__("../../../../../src/app/app.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__comment_comment_component__ = __webpack_require__("../../../../../src/app/comment/comment.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__comment_list_comment_list_component__ = __webpack_require__("../../../../../src/app/comment-list/comment-list.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__blog_entry_blog_entry_component__ = __webpack_require__("../../../../../src/app/blog-entry/blog-entry.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__blog_entry_list_blog_entry_list_component__ = __webpack_require__("../../../../../src/app/blog-entry-list/blog-entry-list.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__blog_entry_form_blog_entry_form_component__ = __webpack_require__("../../../../../src/app/blog-entry-form/blog-entry-form.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__search_entry_search_entry_component__ = __webpack_require__("../../../../../src/app/search-entry/search-entry.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__directives_emphasize_emphasize_directive__ = __webpack_require__("../../../../../src/app/directives/emphasize/emphasize.directive.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__pipes_title_pipe__ = __webpack_require__("../../../../../src/app/pipes/title.pipe.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__angular_router__ = __webpack_require__("../../../router/esm5/router.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__pages_main_page_main_page_component__ = __webpack_require__("../../../../../src/app/pages/main-page/main-page.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__pages_blog_entry_page_blog_entry_page_component__ = __webpack_require__("../../../../../src/app/pages/blog-entry-page/blog-entry-page.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__pages_not_found_page_not_found_page_component__ = __webpack_require__("../../../../../src/app/pages/not-found-page/not-found-page.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__services_shared_blog_entry_service__ = __webpack_require__("../../../../../src/app/services/shared-blog-entry.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__blog_entry_blog_entry_details_component__ = __webpack_require__("../../../../../src/app/blog-entry/blog-entry-details.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_18__angular_common_http__ = __webpack_require__("../../../common/esm5/http.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_19__services_blog_entry_blog_entry_service__ = __webpack_require__("../../../../../src/app/services/blog-entry/blog-entry.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_20__comment_form_comment_form_component__ = __webpack_require__("../../../../../src/app/comment-form/comment-form.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_21__services_comment_comment_service__ = __webpack_require__("../../../../../src/app/services/comment/comment.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_22__login_login_component__ = __webpack_require__("../../../../../src/app/login/login.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_23__services_authentication_service_service__ = __webpack_require__("../../../../../src/app/services/authentication-service.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_24__services_can_activate_auth_guard__ = __webpack_require__("../../../../../src/app/services/can-activate-auth.guard.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_25__services_jwt_utils_service__ = __webpack_require__("../../../../../src/app/services/jwt-utils.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_26__services_token_interceptor_service__ = __webpack_require__("../../../../../src/app/services/token-interceptor.service.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};




























var appRoutes = [
    { path: 'main', component: __WEBPACK_IMPORTED_MODULE_13__pages_main_page_main_page_component__["a" /* MainPageComponent */] },
    { path: 'entry/:id', component: __WEBPACK_IMPORTED_MODULE_14__pages_blog_entry_page_blog_entry_page_component__["a" /* BlogEntryPageComponent */], canActivate: [__WEBPACK_IMPORTED_MODULE_24__services_can_activate_auth_guard__["a" /* CanActivateAuthGuard */]] },
    { path: 'login', component: __WEBPACK_IMPORTED_MODULE_22__login_login_component__["a" /* LoginComponent */] },
    { path: '',
        redirectTo: 'main',
        pathMatch: 'full'
    },
    { path: '**', component: __WEBPACK_IMPORTED_MODULE_15__pages_not_found_page_not_found_page_component__["a" /* NotFoundPageComponent */] }
];
var AppModule = (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_1__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_3__app_component__["a" /* AppComponent */],
                __WEBPACK_IMPORTED_MODULE_4__comment_comment_component__["a" /* CommentComponent */],
                __WEBPACK_IMPORTED_MODULE_5__comment_list_comment_list_component__["a" /* CommentListComponent */],
                __WEBPACK_IMPORTED_MODULE_6__blog_entry_blog_entry_component__["a" /* BlogEntryComponent */],
                __WEBPACK_IMPORTED_MODULE_7__blog_entry_list_blog_entry_list_component__["a" /* BlogEntryListComponent */],
                __WEBPACK_IMPORTED_MODULE_8__blog_entry_form_blog_entry_form_component__["a" /* BlogEntryFormComponent */],
                __WEBPACK_IMPORTED_MODULE_9__search_entry_search_entry_component__["a" /* SearchEntryComponent */],
                __WEBPACK_IMPORTED_MODULE_10__directives_emphasize_emphasize_directive__["a" /* EmphasizeDirective */],
                __WEBPACK_IMPORTED_MODULE_11__pipes_title_pipe__["a" /* TitlePipe */],
                __WEBPACK_IMPORTED_MODULE_13__pages_main_page_main_page_component__["a" /* MainPageComponent */],
                __WEBPACK_IMPORTED_MODULE_14__pages_blog_entry_page_blog_entry_page_component__["a" /* BlogEntryPageComponent */],
                __WEBPACK_IMPORTED_MODULE_15__pages_not_found_page_not_found_page_component__["a" /* NotFoundPageComponent */],
                __WEBPACK_IMPORTED_MODULE_17__blog_entry_blog_entry_details_component__["a" /* BlogEntryDetailsComponent */],
                __WEBPACK_IMPORTED_MODULE_20__comment_form_comment_form_component__["a" /* CommentFormComponent */],
                __WEBPACK_IMPORTED_MODULE_22__login_login_component__["a" /* LoginComponent */]
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__["a" /* BrowserModule */],
                __WEBPACK_IMPORTED_MODULE_2__angular_forms__["a" /* FormsModule */],
                __WEBPACK_IMPORTED_MODULE_12__angular_router__["c" /* RouterModule */].forRoot(appRoutes, { enableTracing: true } // <-- debugging purposes only
                ),
                __WEBPACK_IMPORTED_MODULE_18__angular_common_http__["c" /* HttpClientModule */]
            ],
            providers: [
                __WEBPACK_IMPORTED_MODULE_16__services_shared_blog_entry_service__["a" /* SharedBlogEntryService */],
                __WEBPACK_IMPORTED_MODULE_19__services_blog_entry_blog_entry_service__["a" /* BlogEntryService */],
                __WEBPACK_IMPORTED_MODULE_21__services_comment_comment_service__["a" /* CommentService */],
                __WEBPACK_IMPORTED_MODULE_23__services_authentication_service_service__["a" /* AuthenticationService */],
                __WEBPACK_IMPORTED_MODULE_24__services_can_activate_auth_guard__["a" /* CanActivateAuthGuard */],
                __WEBPACK_IMPORTED_MODULE_25__services_jwt_utils_service__["a" /* JwtUtilsService */],
                {
                    provide: __WEBPACK_IMPORTED_MODULE_18__angular_common_http__["a" /* HTTP_INTERCEPTORS */],
                    useClass: __WEBPACK_IMPORTED_MODULE_26__services_token_interceptor_service__["a" /* TokenInterceptorService */],
                    multi: true
                },
            ],
            bootstrap: [__WEBPACK_IMPORTED_MODULE_3__app_component__["a" /* AppComponent */]]
        })
    ], AppModule);
    return AppModule;
}());



/***/ }),

/***/ "../../../../../src/app/blog-entry-form/blog-entry-form.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/blog-entry-form/blog-entry-form.component.html":
/***/ (function(module, exports) {

module.exports = "<h3>New entry</h3>\n<form class=\"form\" (ngSubmit)=\"save()\">\n  <div class=\"form-group\">\n    <label for=\"title\">title:</label>\n    <input class=\"form-control\" id=\"title\" name=\"title\" [(ngModel)]=\"newBlogEntry.title\"/>\n  </div>\n  <div class=\"form-group\">\n    <label for=\"entry\">entry:</label>\n    <textarea class=\"form-control\" id=\"entry\" name=\"entry\" [(ngModel)]=\"newBlogEntry.entry\"></textarea>\n  </div>\n  <input class=\"btn btn-primary pull-right\" type=\"submit\" value=\"save\"/>\n</form>"

/***/ }),

/***/ "../../../../../src/app/blog-entry-form/blog-entry-form.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BlogEntryFormComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var BlogEntryFormComponent = (function () {
    // username:string = '';
    function BlogEntryFormComponent() {
        this.saveBlogEntryEvent = new __WEBPACK_IMPORTED_MODULE_0__angular_core__["v" /* EventEmitter */]();
    }
    BlogEntryFormComponent.prototype.ngOnInit = function () {
        this.newBlogEntry = {
            title: '',
            description: '',
            entry: '',
            comments: []
        };
    };
    BlogEntryFormComponent.prototype.save = function () {
        this.newBlogEntry.date = new Date();
        this.saveBlogEntryEvent.emit(this.newBlogEntry);
        this.newBlogEntry = {
            title: '',
            description: '',
            entry: '',
            comments: []
        };
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["P" /* Output */])(),
        __metadata("design:type", Object)
    ], BlogEntryFormComponent.prototype, "saveBlogEntryEvent", void 0);
    BlogEntryFormComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-blog-entry-form',
            template: __webpack_require__("../../../../../src/app/blog-entry-form/blog-entry-form.component.html"),
            styles: [__webpack_require__("../../../../../src/app/blog-entry-form/blog-entry-form.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], BlogEntryFormComponent);
    return BlogEntryFormComponent;
}());



/***/ }),

/***/ "../../../../../src/app/blog-entry-list/blog-entry-list.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/blog-entry-list/blog-entry-list.component.html":
/***/ (function(module, exports) {

module.exports = "<ul class=\"list-unstyled\">\n  <li *ngFor=\"let blogEntry of blogEntries | async;\">\n    <app-blog-entry [showComments]=\"false\" [blogEntry]=\"blogEntry\"></app-blog-entry>\n    <button *ngIf=\"isLoggedIn()\" class=\"btn btn-default\" (click)=\"details(blogEntry)\">details</button>\n    <button *ngIf=\"isLoggedIn()\" class=\"btn btn-danger\" (click)=\"delete(blogEntry._id)\">delete</button>\n  </li>\n</ul>"

/***/ }),

/***/ "../../../../../src/app/blog-entry-list/blog-entry-list.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BlogEntryListComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__services_shared_blog_entry_service__ = __webpack_require__("../../../../../src/app/services/shared-blog-entry.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_router__ = __webpack_require__("../../../router/esm5/router.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__services_authentication_service_service__ = __webpack_require__("../../../../../src/app/services/authentication-service.service.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};







var BlogEntryListComponent = (function () {
    function BlogEntryListComponent(sharedBlogEntryService, router, authService) {
        this.sharedBlogEntryService = sharedBlogEntryService;
        this.router = router;
        this.authService = authService;
        this.deleteBlogEntry = new __WEBPACK_IMPORTED_MODULE_0__angular_core__["v" /* EventEmitter */]();
    }
    BlogEntryListComponent.prototype.ngOnInit = function () {
    };
    BlogEntryListComponent.prototype.details = function (blogEntry) {
        this.router.navigate(['/entry/', blogEntry._id]);
    };
    BlogEntryListComponent.prototype.delete = function (id) {
        this.deleteBlogEntry.emit(id);
    };
    BlogEntryListComponent.prototype.isLoggedIn = function () {
        return this.authService.isLoggedIn();
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["D" /* Input */])(),
        __metadata("design:type", Array)
    ], BlogEntryListComponent.prototype, "blogEntries", void 0);
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["P" /* Output */])(),
        __metadata("design:type", __WEBPACK_IMPORTED_MODULE_0__angular_core__["v" /* EventEmitter */])
    ], BlogEntryListComponent.prototype, "deleteBlogEntry", void 0);
    BlogEntryListComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-blog-entry-list',
            template: __webpack_require__("../../../../../src/app/blog-entry-list/blog-entry-list.component.html"),
            styles: [__webpack_require__("../../../../../src/app/blog-entry-list/blog-entry-list.component.css")]
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__services_shared_blog_entry_service__["a" /* SharedBlogEntryService */],
            __WEBPACK_IMPORTED_MODULE_2__angular_router__["b" /* Router */],
            __WEBPACK_IMPORTED_MODULE_3__services_authentication_service_service__["a" /* AuthenticationService */]])
    ], BlogEntryListComponent);
    return BlogEntryListComponent;
}());



/***/ }),

/***/ "../../../../../src/app/blog-entry/blog-entry-details.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BlogEntryDetailsComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__blog_entry_component__ = __webpack_require__("../../../../../src/app/blog-entry/blog-entry.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_router__ = __webpack_require__("../../../router/esm5/router.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__services_blog_entry_blog_entry_service__ = __webpack_require__("../../../../../src/app/services/blog-entry/blog-entry.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__services_comment_comment_service__ = __webpack_require__("../../../../../src/app/services/comment/comment.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__services_authentication_service_service__ = __webpack_require__("../../../../../src/app/services/authentication-service.service.ts");
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};






var BlogEntryDetailsComponent = (function (_super) {
    __extends(BlogEntryDetailsComponent, _super);
    //kompomente BlogEntry i BlogEntryDetails komuniciraju kroz servis
    function BlogEntryDetailsComponent(blogEntryService, commentService, route, authService) {
        var _this = _super.call(this) || this;
        _this.blogEntryService = blogEntryService;
        _this.commentService = commentService;
        _this.route = route;
        _this.authService = authService;
        return _this;
    }
    BlogEntryDetailsComponent.prototype.ngOnInit = function () {
        var _this = this;
        // this.blogEntry = this.sharedBlogEntryService.blogEntry;
        this.sub = this.route.params.subscribe(function (params) {
            // postavljanje observable narusilo bi api nasledjene klase
            // zbog toga je observabla razresena i postavljena vrednost 
            // blogEntry$ = this.blogEntryService.get(+params['id']); 
            _this.id = params['id'];
            _this.loadData();
        });
    };
    BlogEntryDetailsComponent.prototype.loadData = function () {
        var _this = this;
        this.blogEntryService.get(this.id).subscribe(function (data) {
            _this.blogEntry = data;
        });
    };
    BlogEntryDetailsComponent.prototype.saveComment = function (comment) {
        var _this = this;
        comment.signedBy = this.authService.getCurrentUser().username;
        this.commentService.save(comment, this.id).subscribe(function (data) {
            _this.loadData();
        });
    };
    BlogEntryDetailsComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-blog-entry-details',
            template: __webpack_require__("../../../../../src/app/blog-entry/blog-entry.component.html"),
            styles: [__webpack_require__("../../../../../src/app/blog-entry/blog-entry.component.css")]
        })
        //posto su veoma slicne BlogEntry i BlogEntryDetails recikliraju isti templejt
        //BlogEntryDetails nasledjuje BlogEntry i time preuzima i njene impute
        ,
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_3__services_blog_entry_blog_entry_service__["a" /* BlogEntryService */],
            __WEBPACK_IMPORTED_MODULE_4__services_comment_comment_service__["a" /* CommentService */],
            __WEBPACK_IMPORTED_MODULE_2__angular_router__["a" /* ActivatedRoute */],
            __WEBPACK_IMPORTED_MODULE_5__services_authentication_service_service__["a" /* AuthenticationService */]])
    ], BlogEntryDetailsComponent);
    return BlogEntryDetailsComponent;
}(__WEBPACK_IMPORTED_MODULE_1__blog_entry_component__["a" /* BlogEntryComponent */]));



/***/ }),

/***/ "../../../../../src/app/blog-entry/blog-entry.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/blog-entry/blog-entry.component.html":
/***/ (function(module, exports) {

module.exports = "<div class=\"row\">\n    <div class=\"col-md-8\" *ngIf=\"blogEntry\" [app-emphasize]=\"'.title, .entry'\" [color]=\"'#e6ffff'\">\n        <h3 class=\"title\"> \n            {{blogEntry.title | title}}\n        </h3>\n        <div *ngIf=\"blogEntry.createdAt\">{{blogEntry.createdAt | date:\"dd.MM.yy hh:mm:ss\"}}</div>\n        <div *ngIf=\"blogEntry.updatedAt\">{{blogEntry.updatedAt | date:\"dd.MM.yy hh:mm:ss\"}}</div>\n        <div class=\"entry\">{{blogEntry.entry}}</div>\n        <app-comment-list *ngIf=\"showComments\" [comments]=\"blogEntry.comments\"></app-comment-list>\n    </div>\n    <div class=\"col-md-4\">\n        <app-comment-form (saveComment)=\"saveComment($event)\" *ngIf=\"showComments\"></app-comment-form>\n    </div>\n</div>"

/***/ }),

/***/ "../../../../../src/app/blog-entry/blog-entry.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BlogEntryComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var BlogEntryComponent = (function () {
    function BlogEntryComponent() {
    }
    BlogEntryComponent.prototype.ngOnInit = function () {
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["D" /* Input */])(),
        __metadata("design:type", Object)
    ], BlogEntryComponent.prototype, "blogEntry", void 0);
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["D" /* Input */])(),
        __metadata("design:type", Boolean)
    ], BlogEntryComponent.prototype, "showComments", void 0);
    BlogEntryComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-blog-entry',
            template: __webpack_require__("../../../../../src/app/blog-entry/blog-entry.component.html"),
            styles: [__webpack_require__("../../../../../src/app/blog-entry/blog-entry.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], BlogEntryComponent);
    return BlogEntryComponent;
}());



/***/ }),

/***/ "../../../../../src/app/comment-form/comment-form.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/comment-form/comment-form.component.html":
/***/ (function(module, exports) {

module.exports = "<h3>Comment</h3>\n<form class=\"form\" (ngSubmit)=\"save()\">\n  <!-- <div class=\"form-group\">\n    <label for=\"singedBy\">your name:</label>\n    <input class=\"form-control\" id=\"signedBy\" name=\"signedBy\" [(ngModel)]=\"comment.signedBy\"/>\n  </div> -->\n  <div class=\"form-group\">\n    <label for=\"comment\">comment:</label>\n    <textarea class=\"form-control\" id=\"title\" name=\"title\" [(ngModel)]=\"comment.text\"></textarea>\n  </div>\n  <input class=\"btn btn-primary pull-right\" type=\"submit\" value=\"submit comment\"/>\n</form>"

/***/ }),

/***/ "../../../../../src/app/comment-form/comment-form.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return CommentFormComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var CommentFormComponent = (function () {
    function CommentFormComponent() {
        this.saveComment = new __WEBPACK_IMPORTED_MODULE_0__angular_core__["v" /* EventEmitter */]();
    }
    CommentFormComponent.prototype.ngOnInit = function () {
        this.comment = {
            text: ''
        };
    };
    CommentFormComponent.prototype.save = function () {
        this.saveComment.emit(this.comment);
        this.comment = {
            text: ''
        };
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["P" /* Output */])(),
        __metadata("design:type", __WEBPACK_IMPORTED_MODULE_0__angular_core__["v" /* EventEmitter */])
    ], CommentFormComponent.prototype, "saveComment", void 0);
    CommentFormComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-comment-form',
            template: __webpack_require__("../../../../../src/app/comment-form/comment-form.component.html"),
            styles: [__webpack_require__("../../../../../src/app/comment-form/comment-form.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], CommentFormComponent);
    return CommentFormComponent;
}());



/***/ }),

/***/ "../../../../../src/app/comment-list/comment-list.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/comment-list/comment-list.component.html":
/***/ (function(module, exports) {

module.exports = "<ul>\n  <li *ngFor=\"let comment of comments; let i = index\">\n    <app-comment [comment]=\"comment\"></app-comment>\n  </li>\n</ul>\n"

/***/ }),

/***/ "../../../../../src/app/comment-list/comment-list.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return CommentListComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var CommentListComponent = (function () {
    function CommentListComponent() {
    }
    CommentListComponent.prototype.ngOnInit = function () {
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["D" /* Input */])(),
        __metadata("design:type", Array)
    ], CommentListComponent.prototype, "comments", void 0);
    CommentListComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-comment-list',
            template: __webpack_require__("../../../../../src/app/comment-list/comment-list.component.html"),
            styles: [__webpack_require__("../../../../../src/app/comment-list/comment-list.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], CommentListComponent);
    return CommentListComponent;
}());



/***/ }),

/***/ "../../../../../src/app/comment/comment.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/comment/comment.component.html":
/***/ (function(module, exports) {

module.exports = "<div [app-emphasize]=\"'.comment'\" [color]=\"'#f2f2f2'\">\n    <div>\n        <b>{{comment.signedBy}}</b>\n    </div>\n    <div class=\"comment\">{{comment.text}}</div>\n</div>\n<ng-template [ngIf]=\"comment.comments\">\n    <app-comment-list [comments]=\"comment.comments\"></app-comment-list>\n</ng-template>\n<!-- <app-comment-list *ngIf=\"comment.comments\" [comments]=\"comment.comments\"></app-comment-list> -->"

/***/ }),

/***/ "../../../../../src/app/comment/comment.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return CommentComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var CommentComponent = (function () {
    function CommentComponent() {
    }
    CommentComponent.prototype.ngOnInit = function () {
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["D" /* Input */])(),
        __metadata("design:type", Object)
    ], CommentComponent.prototype, "comment", void 0);
    CommentComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-comment',
            template: __webpack_require__("../../../../../src/app/comment/comment.component.html"),
            styles: [__webpack_require__("../../../../../src/app/comment/comment.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], CommentComponent);
    return CommentComponent;
}());



/***/ }),

/***/ "../../../../../src/app/directives/emphasize/emphasize.directive.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return EmphasizeDirective; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var EmphasizeDirective = (function () {
    function EmphasizeDirective(el) {
        this.el = el;
    }
    EmphasizeDirective.prototype.enter = function () {
        var _this = this;
        this.el.nativeElement.querySelectorAll(this.selector).forEach(function (element) {
            element.style.backgroundColor = _this.color;
        });
    };
    EmphasizeDirective.prototype.leave = function () {
        this.el.nativeElement.querySelectorAll(this.selector).forEach(function (element) {
            element.style.backgroundColor = null;
        });
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["D" /* Input */])('app-emphasize'),
        __metadata("design:type", String)
    ], EmphasizeDirective.prototype, "selector", void 0);
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["D" /* Input */])(),
        __metadata("design:type", String)
    ], EmphasizeDirective.prototype, "color", void 0);
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["y" /* HostListener */])('mouseenter'),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", []),
        __metadata("design:returntype", void 0)
    ], EmphasizeDirective.prototype, "enter", null);
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["y" /* HostListener */])('mouseleave'),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", []),
        __metadata("design:returntype", void 0)
    ], EmphasizeDirective.prototype, "leave", null);
    EmphasizeDirective = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["s" /* Directive */])({
            selector: '[app-emphasize]'
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_0__angular_core__["t" /* ElementRef */]])
    ], EmphasizeDirective);
    return EmphasizeDirective;
}());



/***/ }),

/***/ "../../../../../src/app/login/login.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/login/login.component.html":
/***/ (function(module, exports) {

module.exports = "<div class=\"container\">\r\n  <div class=\"row\">\r\n    <div class=\"col-md-3\"></div>\r\n    <div class=\"col-md-6\">\r\n      <form class=\"form-signin\" (ngSubmit)=\"login()\">\r\n        <h2 class=\"form-signin-heading\">Please sign in</h2>\r\n        <label for=\"username\" class=\"sr-only\">Username</label>\r\n        <input type=\"text\" id=\"username\" class=\"form-control\" name=\"name\" [(ngModel)]=\"user.name\" placeholder=\"Username\"\r\n          required autofocus>\r\n        <label for=\"inputPassword\" class=\"sr-only\">Password</label>\r\n        <input type=\"password\" id=\"inputPassword\" class=\"form-control\" name=\"password\" [(ngModel)]=\"user.password\" placeholder=\"Password\"\r\n          required>\r\n        <button class=\"btn btn-primary btn-block\" type=\"submit\">Sign in</button>\r\n      </form>\r\n      <div *ngIf=wrongUsernameOrPass class=\"alert alert-warning box-msg\" role=\"alert\">\r\n        Wrong username or password.\r\n      </div>\r\n    </div>\r\n    <div class=\"col-md-3\"></div>\r\n  </div>\r\n</div>"

/***/ }),

/***/ "../../../../../src/app/login/login.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return LoginComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_rxjs_Observable__ = __webpack_require__("../../../../rxjs/_esm5/Observable.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_router__ = __webpack_require__("../../../router/esm5/router.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__services_authentication_service_service__ = __webpack_require__("../../../../../src/app/services/authentication-service.service.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var LoginComponent = (function () {
    function LoginComponent(authenticationService, router) {
        this.authenticationService = authenticationService;
        this.router = router;
        this.user = {};
        this.wrongUsernameOrPass = false;
    }
    LoginComponent.prototype.ngOnInit = function () {
    };
    LoginComponent.prototype.login = function () {
        var _this = this;
        this.authenticationService.login(this.user.name, this.user.password).subscribe(function (loggedIn) {
            if (loggedIn) {
                _this.router.navigate(['/main']);
            }
        }, function (err) {
            if (err.toString() === 'Ilegal login') {
                _this.wrongUsernameOrPass = true;
                console.log(err);
            }
            else {
                __WEBPACK_IMPORTED_MODULE_1_rxjs_Observable__["a" /* Observable */].throw(err);
            }
        });
    };
    LoginComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-login',
            template: __webpack_require__("../../../../../src/app/login/login.component.html"),
            styles: [__webpack_require__("../../../../../src/app/login/login.component.css")],
            encapsulation: __WEBPACK_IMPORTED_MODULE_0__angular_core__["_10" /* ViewEncapsulation */].None
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_3__services_authentication_service_service__["a" /* AuthenticationService */],
            __WEBPACK_IMPORTED_MODULE_2__angular_router__["b" /* Router */]])
    ], LoginComponent);
    return LoginComponent;
}());



/***/ }),

/***/ "../../../../../src/app/pages/blog-entry-page/blog-entry-page.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/pages/blog-entry-page/blog-entry-page.component.html":
/***/ (function(module, exports) {

module.exports = "<app-blog-entry-details [showComments]=\"true\"></app-blog-entry-details>"

/***/ }),

/***/ "../../../../../src/app/pages/blog-entry-page/blog-entry-page.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BlogEntryPageComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var BlogEntryPageComponent = (function () {
    function BlogEntryPageComponent() {
    }
    BlogEntryPageComponent.prototype.ngOnInit = function () {
    };
    BlogEntryPageComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-blog-entry-page',
            template: __webpack_require__("../../../../../src/app/pages/blog-entry-page/blog-entry-page.component.html"),
            styles: [__webpack_require__("../../../../../src/app/pages/blog-entry-page/blog-entry-page.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], BlogEntryPageComponent);
    return BlogEntryPageComponent;
}());



/***/ }),

/***/ "../../../../../src/app/pages/main-page/main-page.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/pages/main-page/main-page.component.html":
/***/ (function(module, exports) {

module.exports = "<div class=\"row\">\n  <div class=\"col-md-8\">\n    <app-blog-entry-list (deleteBlogEntry)=\"delete($event)\" [blogEntries]=\"blogEntries\"></app-blog-entry-list>\n  </div>\n  <div *ngIf=\"isLoggedIn()\" class=\"col-md-4\">\n    <app-search-entry (filterEntriesEvent)=\"filter($event)\"></app-search-entry>\n    <app-blog-entry-form (saveBlogEntryEvent)=\"saveBlogEntry($event)\"></app-blog-entry-form>\n  </div>\n</div>\n"

/***/ }),

/***/ "../../../../../src/app/pages/main-page/main-page.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return MainPageComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__services_blog_entry_blog_entry_service__ = __webpack_require__("../../../../../src/app/services/blog-entry/blog-entry.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__services_authentication_service_service__ = __webpack_require__("../../../../../src/app/services/authentication-service.service.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var MainPageComponent = (function () {
    function MainPageComponent(blogEntryService, authService) {
        this.blogEntryService = blogEntryService;
        this.authService = authService;
    }
    MainPageComponent.prototype.ngOnInit = function () {
        this.blogEntries = this.blogEntryService.getAll();
    };
    MainPageComponent.prototype.saveBlogEntry = function (blogEntry) {
        var _this = this;
        this.blogEntryService.save(blogEntry).subscribe(function (data) {
            _this.filter('');
        });
        // this.blogEntriesBckup.push(blogEntry);
        // this.blogEntries = _.cloneDeep(this.blogEntriesBckup);
    };
    MainPageComponent.prototype.filter = function (text) {
        this.blogEntries = this.blogEntryService.filter(text);
    };
    MainPageComponent.prototype.delete = function (id) {
        var _this = this;
        console.log(id);
        this.blogEntryService.delete(id).subscribe(function (data) {
            return _this.filter('');
        });
    };
    MainPageComponent.prototype.isLoggedIn = function () {
        return this.authService.isLoggedIn();
    };
    MainPageComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-main-page',
            template: __webpack_require__("../../../../../src/app/pages/main-page/main-page.component.html"),
            styles: [__webpack_require__("../../../../../src/app/pages/main-page/main-page.component.css")]
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__services_blog_entry_blog_entry_service__["a" /* BlogEntryService */],
            __WEBPACK_IMPORTED_MODULE_2__services_authentication_service_service__["a" /* AuthenticationService */]])
    ], MainPageComponent);
    return MainPageComponent;
}());



/***/ }),

/***/ "../../../../../src/app/pages/not-found-page/not-found-page.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/pages/not-found-page/not-found-page.component.html":
/***/ (function(module, exports) {

module.exports = "<h1>\n  Page not found!\n</h1>\n"

/***/ }),

/***/ "../../../../../src/app/pages/not-found-page/not-found-page.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return NotFoundPageComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var NotFoundPageComponent = (function () {
    function NotFoundPageComponent() {
    }
    NotFoundPageComponent.prototype.ngOnInit = function () {
    };
    NotFoundPageComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-not-found-page',
            template: __webpack_require__("../../../../../src/app/pages/not-found-page/not-found-page.component.html"),
            styles: [__webpack_require__("../../../../../src/app/pages/not-found-page/not-found-page.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], NotFoundPageComponent);
    return NotFoundPageComponent;
}());



/***/ }),

/***/ "../../../../../src/app/pipes/title.pipe.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return TitlePipe; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};

var TitlePipe = (function () {
    function TitlePipe() {
    }
    TitlePipe.prototype.transform = function (value, args) {
        return value.replace(/\b\w/g, function (l) { return l.toUpperCase(); });
    };
    TitlePipe = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["T" /* Pipe */])({
            name: 'title'
        })
    ], TitlePipe);
    return TitlePipe;
}());



/***/ }),

/***/ "../../../../../src/app/search-entry/search-entry.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/search-entry/search-entry.component.html":
/***/ (function(module, exports) {

module.exports = "<h3>Filter entries</h3>\n<form class=\"form\" (ngSubmit)=\"filter()\">\n  <div class=\"form-group\">\n    <input class=\"form-control\" name=\"search-entry\" type=\"text\" [(ngModel)]=\"filterText\" />\n  </div>\n  <input type=\"button\" class=\"btn btn-default pull-right\" value=\"reset\" (click)=\"reset()\" />\n  <input type=\"submit\" class=\"btn btn-primary pull-right\" value=\"search\" />\n</form>"

/***/ }),

/***/ "../../../../../src/app/search-entry/search-entry.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SearchEntryComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var SearchEntryComponent = (function () {
    function SearchEntryComponent() {
        this.filterEntriesEvent = new __WEBPACK_IMPORTED_MODULE_0__angular_core__["v" /* EventEmitter */]();
    }
    SearchEntryComponent.prototype.ngOnInit = function () {
        this.filterText = '';
    };
    SearchEntryComponent.prototype.filter = function () {
        this.filterEntriesEvent.emit(this.filterText);
    };
    SearchEntryComponent.prototype.reset = function () {
        this.filterText = '';
        this.filter();
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["P" /* Output */])(),
        __metadata("design:type", __WEBPACK_IMPORTED_MODULE_0__angular_core__["v" /* EventEmitter */])
    ], SearchEntryComponent.prototype, "filterEntriesEvent", void 0);
    SearchEntryComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-search-entry',
            template: __webpack_require__("../../../../../src/app/search-entry/search-entry.component.html"),
            styles: [__webpack_require__("../../../../../src/app/search-entry/search-entry.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], SearchEntryComponent);
    return SearchEntryComponent;
}());



/***/ }),

/***/ "../../../../../src/app/services/authentication-service.service.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AuthenticationService; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_rxjs_Rx__ = __webpack_require__("../../../../rxjs/_esm5/Rx.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_common_http__ = __webpack_require__("../../../common/esm5/http.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__jwt_utils_service__ = __webpack_require__("../../../../../src/app/services/jwt-utils.service.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var AuthenticationService = (function () {
    function AuthenticationService(http, jwtUtilsService) {
        this.http = http;
        this.jwtUtilsService = jwtUtilsService;
        this.loginPath = '/api/users/authenticate';
    }
    AuthenticationService.prototype.login = function (name, password) {
        var _this = this;
        var headers = new __WEBPACK_IMPORTED_MODULE_2__angular_common_http__["d" /* HttpHeaders */]({ 'Content-Type': 'application/json' });
        return this.http.post(this.loginPath, JSON.stringify({ name: name, password: password }), { headers: headers })
            .map(function (res) {
            var token = res && res['token'];
            if (token) {
                localStorage.setItem('currentUser', JSON.stringify({
                    username: name,
                    roles: _this.jwtUtilsService.getRoles(token),
                    token: token.split(' ')[1]
                }));
                return true;
            }
            else {
                return false;
            }
        })
            .catch(function (error) {
            if (error.status === 400) {
                return __WEBPACK_IMPORTED_MODULE_1_rxjs_Rx__["a" /* Observable */].throw('Ilegal login');
            }
            else {
                return __WEBPACK_IMPORTED_MODULE_1_rxjs_Rx__["a" /* Observable */].throw(error.json().error || 'Server error');
            }
        });
    };
    AuthenticationService.prototype.getToken = function () {
        var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        var token = currentUser && currentUser.token;
        return token ? token : "";
    };
    AuthenticationService.prototype.logout = function () {
        localStorage.removeItem('currentUser');
    };
    AuthenticationService.prototype.isLoggedIn = function () {
        if (this.getToken() != '')
            return true;
        else
            return false;
    };
    AuthenticationService.prototype.getCurrentUser = function () {
        if (localStorage.currentUser) {
            return JSON.parse(localStorage.currentUser);
        }
        else {
            return undefined;
        }
    };
    AuthenticationService = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_2__angular_common_http__["b" /* HttpClient */], __WEBPACK_IMPORTED_MODULE_3__jwt_utils_service__["a" /* JwtUtilsService */]])
    ], AuthenticationService);
    return AuthenticationService;
}());



/***/ }),

/***/ "../../../../../src/app/services/blog-entry/blog-entry.service.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BlogEntryService; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_common_http__ = __webpack_require__("../../../common/esm5/http.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var BlogEntryService = (function () {
    function BlogEntryService(http) {
        this.http = http;
        this.path = "/api/blogEntries";
    }
    BlogEntryService.prototype.getAll = function () {
        return this.http.get(this.path);
    };
    BlogEntryService.prototype.filter = function (entryText) {
        var params = new __WEBPACK_IMPORTED_MODULE_1__angular_common_http__["e" /* HttpParams */]().set('entry', entryText);
        // let params:HttpParams = new HttpParams();
        // params = params.append('entry',entryText);
        // params = params.append('bla','blabla');
        return this.http.get(this.path, { params: params });
    };
    BlogEntryService.prototype.get = function (id) {
        // const params: HttpParams = new HttpParams().set('_id',id);
        return this.http.get(this.path + ("/" + id));
    };
    BlogEntryService.prototype.save = function (blogEntry) {
        return this.http.post(this.path, blogEntry);
    };
    BlogEntryService.prototype.delete = function (id) {
        return this.http.delete(this.path + ("/" + id));
    };
    BlogEntryService = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__angular_common_http__["b" /* HttpClient */]])
    ], BlogEntryService);
    return BlogEntryService;
}());



/***/ }),

/***/ "../../../../../src/app/services/can-activate-auth.guard.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return CanActivateAuthGuard; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__authentication_service_service__ = __webpack_require__("../../../../../src/app/services/authentication-service.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_router__ = __webpack_require__("../../../router/esm5/router.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var CanActivateAuthGuard = (function () {
    function CanActivateAuthGuard(authenticationService, router) {
        this.authenticationService = authenticationService;
        this.router = router;
    }
    CanActivateAuthGuard.prototype.canActivate = function (next, state) {
        if (this.authenticationService.isLoggedIn()) {
            return true;
        }
        else {
            this.router.navigate(['/main']);
            return false;
        }
    };
    CanActivateAuthGuard = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__authentication_service_service__["a" /* AuthenticationService */], __WEBPACK_IMPORTED_MODULE_2__angular_router__["b" /* Router */]])
    ], CanActivateAuthGuard);
    return CanActivateAuthGuard;
}());



/***/ }),

/***/ "../../../../../src/app/services/comment/comment.service.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return CommentService; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_common_http__ = __webpack_require__("../../../common/esm5/http.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var CommentService = (function () {
    function CommentService(http) {
        this.http = http;
        this.path = "/api/comments";
    }
    CommentService.prototype.save = function (comment, blogEntryId) {
        return this.http.post(this.path + ("/blogEntry/" + blogEntryId), comment);
    };
    CommentService = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__angular_common_http__["b" /* HttpClient */]])
    ], CommentService);
    return CommentService;
}());



/***/ }),

/***/ "../../../../../src/app/services/jwt-utils.service.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return JwtUtilsService; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var JwtUtilsService = (function () {
    function JwtUtilsService() {
    }
    JwtUtilsService.prototype.getRoles = function (token) {
        var jwtData = token.split('.')[1];
        var decodedJwtJsonData = window.atob(jwtData);
        var decodedJwtData = JSON.parse(decodedJwtJsonData);
        return [decodedJwtData.role];
    };
    JwtUtilsService = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [])
    ], JwtUtilsService);
    return JwtUtilsService;
}());



/***/ }),

/***/ "../../../../../src/app/services/shared-blog-entry.service.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SharedBlogEntryService; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var SharedBlogEntryService = (function () {
    function SharedBlogEntryService() {
    }
    SharedBlogEntryService = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [])
    ], SharedBlogEntryService);
    return SharedBlogEntryService;
}());



/***/ }),

/***/ "../../../../../src/app/services/token-interceptor.service.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return TokenInterceptorService; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__authentication_service_service__ = __webpack_require__("../../../../../src/app/services/authentication-service.service.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var TokenInterceptorService = (function () {
    function TokenInterceptorService(inj) {
        this.inj = inj;
    }
    TokenInterceptorService.prototype.intercept = function (request, next) {
        var authenticationService = this.inj.get(__WEBPACK_IMPORTED_MODULE_1__authentication_service_service__["a" /* AuthenticationService */]);
        request = request.clone({
            setHeaders: {
                'Authorization': "JWT " + authenticationService.getToken()
            }
        });
        return next.handle(request);
    };
    TokenInterceptorService = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_0__angular_core__["C" /* Injector */]])
    ], TokenInterceptorService);
    return TokenInterceptorService;
}());



/***/ }),

/***/ "../../../../../src/environments/environment.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return environment; });
// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.
var environment = {
    production: false
};


/***/ }),

/***/ "../../../../../src/main.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__ = __webpack_require__("../../../platform-browser-dynamic/esm5/platform-browser-dynamic.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__app_app_module__ = __webpack_require__("../../../../../src/app/app.module.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__environments_environment__ = __webpack_require__("../../../../../src/environments/environment.ts");




if (__WEBPACK_IMPORTED_MODULE_3__environments_environment__["a" /* environment */].production) {
    Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["_13" /* enableProdMode */])();
}
Object(__WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__["a" /* platformBrowserDynamic */])().bootstrapModule(__WEBPACK_IMPORTED_MODULE_2__app_app_module__["a" /* AppModule */])
    .catch(function (err) { return console.log(err); });


/***/ }),

/***/ 0:
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__("../../../../../src/main.ts");


/***/ })

},[0]);
//# sourceMappingURL=main.bundle.js.map