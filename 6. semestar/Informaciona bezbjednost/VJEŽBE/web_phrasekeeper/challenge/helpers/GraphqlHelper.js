const JWTHelper = require('./JWTHelper');
const {
    GraphQLObjectType,
    GraphQLSchema,
    GraphQLNonNull,
    GraphQLID,
    GraphQLString,
    GraphQLList,
    GraphQLError
} = require('graphql');

const response = data => ({ message: data });

const PhraseSchema = new GraphQLObjectType({
    name: 'Phrases',
    fields: {
        id:         { type: GraphQLID },
        owner:      { type: GraphQLString },
        type:       { type: GraphQLString },
        address:    { type: GraphQLString },
        username:   { type: GraphQLString },
        password:   { type: GraphQLString },
        note:       { type: GraphQLString }
    }
});

const ResponseType = new GraphQLObjectType({
    name: 'Response',
    fields: {
        message:         { type: GraphQLString },
        token:           { type: GraphQLString }
    }
});

const queryType = new GraphQLObjectType({
    name: 'Query',
    fields: {
        getPhraseList: {
            type: new GraphQLList(PhraseSchema),
            resolve: async (root, args, request) => {
                return new Promise((resolve, reject) => {
                    if (!request.user) return reject(new GraphQLError('Authentication required!'));

                    db.getPhraseList(request.user.username)
                        .then(rows => resolve(rows))
                        .catch(err => reject(new GraphQLError(err)))
                });
            }
        }
    }
});

const mutationType = new GraphQLObjectType({
    name: 'Mutation',
    fields: {
        RegisterUser: {
            type: ResponseType,
            args: {
                email: { type: new GraphQLNonNull(GraphQLString) },
                username: { type: new GraphQLNonNull(GraphQLString) },
                password: { type: new GraphQLNonNull(GraphQLString) }
            },
            resolve: async (root, args, request) => {
                return new Promise((resolve, reject) => {
                    db.registerUser(args.email, args.username, args.password)
                        .then(() => resolve(response("User registered successfully!")))
                        .catch(err => reject(new GraphQLError(err)));
                });
            }
        },

        LoginUser: {
            type: ResponseType,
            args: {
                username: { type: new GraphQLNonNull(GraphQLString) },
                password: { type: new GraphQLNonNull(GraphQLString) }
            },
            resolve: async (root, args, request) => {
                return new Promise((resolve, reject) => {
                    db.loginUser(args.username, args.password)
                        .then(async (user) => {
                            if (user.length) {
                                let token = await JWTHelper.sign( user[0] );
                                resolve({
                                    message: "User logged in successfully!",
                                    token: token
                                });
                            };
                            reject(new Error("Username or password is invalid!"));
                        })
                        .catch(err => reject(new GraphQLError(err)));
                });
            }
        },

        UpdatePassword: {
            type: ResponseType,
            args: {
                username: { type: new GraphQLNonNull(GraphQLString) },
                password: { type: new GraphQLNonNull(GraphQLString) }
            },
            resolve: async (root, args, request) => {
                return new Promise((resolve, reject) => {
                    if (!request.user) return reject(new GraphQLError('Authentication required!'));

                    db.updatePassword(args.username, args.password)
                        .then(() => resolve(response("Password updated successfully!")))
                        .catch(err => reject(new GraphQLError(err)));
                });
            }
        },

        AddPhrase: {
            type: ResponseType,
            args: {
                recType: { type: new GraphQLNonNull(GraphQLString) },
                recAddr: { type: new GraphQLNonNull(GraphQLString) },
                recUser: { type: new GraphQLNonNull(GraphQLString) },
                recPass: { type: new GraphQLNonNull(GraphQLString) },
                recNote: { type: new GraphQLNonNull(GraphQLString) },
            },
            resolve: async (root, args, request) => {
                return new Promise((resolve, reject) => {
                    if (!request.user) return reject(new GraphQLError('Authentication required!'));

                    db.addPhrase(request.user.username, args)
                        .then(() => resolve(response("Phrase added successfully!")))
                        .catch(err => reject(new GraphQLError(err)));
                });
            }
        },
    }
});

module.exports = new GraphQLSchema({
    query: queryType,
    mutation: mutationType
});
