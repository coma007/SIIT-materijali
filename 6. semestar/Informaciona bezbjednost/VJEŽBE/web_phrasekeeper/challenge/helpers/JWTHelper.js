const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const SECRET = crypto.randomBytes(69).toString('hex');

module.exports = {
    async sign(data) {
        return jwt.sign(data, SECRET, {
            algorithm: 'HS256'
        });
    },
    async verify(token) {
        return jwt.verify(token, SECRET, {
            algorithm: 'HS256'
        });
    }
};