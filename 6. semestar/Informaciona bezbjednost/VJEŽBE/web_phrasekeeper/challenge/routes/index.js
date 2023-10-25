const express          = require('express');
const router           = express.Router();
const { graphqlHTTP }  = require('express-graphql');
const { execSync }     = require('child_process');
const { existsSync }   = require('fs');
const AuthMiddleware   = require('../middleware/AuthMiddleware');
const GraphqlSchema    = require('../helpers/GraphqlHelper');

const response = data => ({ message: data });

router.get('/', (req, res) => {
    return res.render('login.html');
});

router.get('/register', (req, res) => {
    return res.render('register.html');
});

router.use('/graphql', AuthMiddleware, graphqlHTTP({
    schema: GraphqlSchema,
    graphiql: false
}));

router.get('/dashboard', AuthMiddleware, async (req, res, next) => {
    return res.render('dashboard.html', {user: req.user});
});

router.get('/settings', AuthMiddleware, async (req, res, next) => {
    if (!req.user.is_admin) return res.redirect('/dashboard');

    return res.render('settings.html', {user: req.user});
});

router.get('/admin/export', AuthMiddleware, async (req, res, next) => {
    if (!req.user.is_admin) return res.redirect('/dashboard');

    const { filename } = req.query;

    if (filename) {
        try {
            execSync(`mysqldump -h 127.0.0.1 -uphrasekeeper -pphrasekeeper --add-drop-table phrasekeeper > /opt/exports/${filename}.sql`);

            if (existsSync(`/opt/exports/${filename}.sql`)) {
                return res.download(`/opt/exports/${filename}.sql`, `${filename}.sql`);
            }
        }
        catch (e) {
            return res.status(500).send(response('Something went wrong!'));
        }
    }

    res.status(401).send(response('Missing required parameters!'));
});

router.get('/logout', (req, res) => {
    res.clearCookie('session');
    return res.redirect('/');
});

module.exports = () => {
    return router;
};