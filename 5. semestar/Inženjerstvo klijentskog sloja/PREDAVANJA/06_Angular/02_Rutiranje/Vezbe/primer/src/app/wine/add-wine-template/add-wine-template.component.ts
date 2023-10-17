import { Component, OnInit } from '@angular/core';
import { WineService } from '../services/wine.service';
import { Router, ActivatedRoute } from '@angular/router';
import { Wine } from '../model/wine.model';

@Component({
  selector: 'app-add-wine-template',
  templateUrl: './add-wine-template.component.html',
  styleUrls: ['./add-wine-template.component.css']
})
export class AddWineTemplateComponent implements OnInit {
  private wine = {};

  constructor(
    private wineService: WineService,
    private router: Router,
    private route: ActivatedRoute
    
  ) { }

  ngOnInit() {
  }

  onSubmit(){
    this.wineService.add(this.wine as Wine);  		
    this.router.navigate(['wines']);
	}
}
