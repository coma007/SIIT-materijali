const MY_KEY = Symbol();
const FOO = Symbol();
const obj = {
    [MY_KEY]: 123,
    [FOO]() {
        return 'bar';
    }
};
console.log(obj[MY_KEY]);//123
console.log(obj[FOO]());//bar

//-----------------------------------
//simboli za predstavljanje koncepata (kao enumeracija)

const COLOR_RED    = Symbol('Red');
const COLOR_ORANGE = Symbol('Orange');
const COLOR_YELLOW = Symbol('Yellow');
const COLOR_GREEN  = Symbol('Green');
const COLOR_BLUE   = Symbol('Blue');
const COLOR_VIOLET = Symbol('Violet');

function getComplement(color) {
    switch (color) {
        case COLOR_RED:
            return COLOR_GREEN;
        case COLOR_ORANGE:
            return COLOR_BLUE;
        case COLOR_YELLOW:
            return COLOR_VIOLET;
        case COLOR_GREEN:
            return COLOR_RED;
        case COLOR_BLUE:
            return COLOR_ORANGE;
        case COLOR_VIOLET:
            return COLOR_YELLOW;
        default:
            throw new Exception('Unknown color: '+color);
    }
}

console.log(getComplement(COLOR_BLUE))