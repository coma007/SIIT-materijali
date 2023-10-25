const mysql  = require('mysql')

class Database {

	constructor() {
		this.connection = mysql.createConnection({
			host: '127.0.0.1',
			user: 'phrasekeeper',
			password: 'phrasekeeper',
			database: 'phrasekeeper'
		});
	}

	async connect() {
		return new Promise((resolve, reject)=> {
			this.connection.connect((err)=> {
				if(err)
					reject(err)
				resolve()
			});
		})
	}

    async registerUser(email, username, password) {
		return new Promise(async (resolve, reject) => {
			let stmt = `INSERT INTO users(email, username, password) VALUES(?, ?, ?)`;
			this.connection.query(
                stmt,
                [
                    String(email),
                    String(username),
                    String(password)
                ],
                (err, _) => {
                    if(err)
                        reject(err);
                    resolve()
			    }
            )
		});
	}

    async loginUser(username, password) {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT username, is_admin FROM users WHERE username = ? and password = ?`;
			this.connection.query(
                stmt,
                [
                    String(username),
                    String(password)
                ],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        resolve(JSON.parse(JSON.stringify(result)))
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async updatePassword(username, password) {
        return new Promise(async (resolve, reject) => {
            let stmt = `UPDATE users SET password = ? WHERE username = ?`;
            this.connection.query(
                stmt,
                [
                    String(password),
                    String(username)
                ],
                (err, _) => {
                    if(err)
                        reject(err)
                    resolve();
			    }
            )
        });
    }

    async getPhraseList(username) {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT * FROM saved_passwords WHERE owner = ?`;
			this.connection.query(
                stmt,
                [
                    String(username)
                ],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        resolve(JSON.parse(JSON.stringify(result)))
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async addPhrase(owner, args) {
        return new Promise(async (resolve, reject) => {
            let stmt = `INSERT INTO saved_passwords (owner, type, address, username, password, note) VALUES (?, ?, ?, ?, ?, ?)`;
            this.connection.query(
                stmt,
                [
                    String(owner),
                    String(args.recType),
                    String(args.recAddr),
                    String(args.recUser),
                    String(args.recPass),
                    String(args.recNote)
                ],
                (err, _) => {
                    if(err)
                        reject(err)
                    resolve();
			    }
            )
        });
    }

}

module.exports = Database;