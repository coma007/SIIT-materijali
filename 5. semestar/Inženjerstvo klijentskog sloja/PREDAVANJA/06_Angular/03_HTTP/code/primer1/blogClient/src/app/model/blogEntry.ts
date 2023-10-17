import { Comment } from "./comment";

export interface BlogEntry{
    _id?:any;
    title:string;
    description:string;
    entry:string;
    comments?:Comment[];
    date?:Date;
}