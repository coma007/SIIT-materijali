import { Comment } from "./comment";

export interface BlogEntry{
    title:string;
    description:string;
    entry:string;
    comments?:Comment[];
    date?:Date;
}