import { Injectable } from '@angular/core';

@Injectable()
export class JwtUtilsService {

  constructor() { }

  getRoles(token: string) {
    let jwtData = token.split('.')[1];
    let decodedJwtJsonData = window.atob(jwtData);
    let decodedJwtData = JSON.parse(decodedJwtJsonData);

    return [decodedJwtData.role];
  }

}
