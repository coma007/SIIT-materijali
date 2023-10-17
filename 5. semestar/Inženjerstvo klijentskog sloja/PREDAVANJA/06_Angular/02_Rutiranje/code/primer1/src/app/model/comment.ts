export interface Comment{
    text:string;
    signedBy?:string;
    comments?:Comment[];
}