const JWTHelper = require('../helpers/JWTHelper');

module.exports = async (req, res, next) => {
	try{
		if (req.cookies.session === undefined) {
            if (req.baseUrl === '/graphql') return next();
			if (!req.is('application/json')) return res.redirect('/');
			return res.status(401).json({ status: 'unauthorized', message: 'Authentication required!' });
		}
		return JWTHelper.verify(req.cookies.session)
			.then(user => {
				req.user = user;
				next();
			})
			.catch((e) => {
                if (req.baseUrl === '/graphql') return next();
				res.redirect('/logout');
			});
	} catch(e) {
		console.log(e);
		return res.redirect('/logout');
	}
}