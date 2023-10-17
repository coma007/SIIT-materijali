import { Comment } from "../model/comment";
import { BlogEntry } from "../model/blogEntry";

//rekurzivno trazenje komentara u stablu
function searchComment(text:string, comment:Comment){
    //ako ima trazen tekst, prnadjen je
    if(comment.text.indexOf(text)!=-1) return true;
    //ako nema tekst i list je vrati se korak nazad
    else if(!comment.comments||comment.comments.length==0) return false;
    else{
        //ako ima komentare, rekurzivno pregledaj njih
        for(let c of comment.comments){
            //ako je pronadjen, prekini rekurziju
            if(searchComment(text, c)) return true;    
        }
        //ako je prosla cela rekurzija, vrati se korak nazad
        return false;
    }
}

function searchComments(text:string, comments:Comment[]):boolean{
    if(!comments||comments.length==0) return false;
    for(let c of comments){
        if(searchComment(text, c)) return true;
    }
    return false;
}

let searchEntry = function(text:string, entry:BlogEntry){
        if(entry.description.indexOf(text)!=-1) return true;
        else if(entry.title.indexOf(text)!=-1) return true;
        else if(entry.entry.indexOf(text)!=-1) return true;
        else if(searchComments(text, entry.comments)) return true;
        else return false;
}

export default searchEntry;