import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from 'src/infrastructure/material.module';
import { CreateWineReactiveComponent } from './create-wine-reactive/create-wine-reactive.component';
import { WineDetailsComponent } from './wine-details/wine-details.component';
import { WineComponent } from './wine/wine.component';
import { SharedModule } from '../shared/shared.module';
import { FlexLayoutModule } from '@angular/flex-layout';
import { RouterModule } from '@angular/router';
import { AuthModule } from '../auth/auth.module';

@NgModule({
  declarations: [
    WineComponent,
    WineDetailsComponent,
    CreateWineReactiveComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
    MaterialModule,
    ReactiveFormsModule,
    HttpClientModule,
    SharedModule,
    FlexLayoutModule,
  ],
})
export class WineModule {}
