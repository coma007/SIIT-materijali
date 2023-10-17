let uuid = require('uuid'); 

type UUID = string;
type UUIDGenerator = () => string;
type UUIDOrGenerator = UUID | UUIDGenerator;

let generateUUID: (() => UUID) = () => uuid.v4(); 

function getUUID(uuidOrGen: UUIDOrGenerator): UUID{
    if(typeof uuidOrGen === 'string'){
        return uuidOrGen;
    }
    else{
        return uuidOrGen();
    }
}

console.log(getUUID(generateUUID));