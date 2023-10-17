import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { AuthenticationService } from './services/authentication-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  constructor(private authService: AuthenticationService,
              private router: Router){
    
  }

  ngOnInit() {
  }
  
  loggedIn():boolean{
    return this.authService.isLoggedIn();
  }

  login():void{
    this.router.navigate(['login']);
  }

  logout():void{
    this.authService.logout();
    this.router.navigate(['main']);
  }
}
