// username and password are admin admin

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
// koristimo mongoose model koju smo kreirali u folderu model
var BlogEntry = require(__dirname + '/app/model/blogEntry');
var Comment = require(__dirname + '/app/model/comment');
var User        = require(__dirname + '/app/model/user');
var passport  = require('passport');
var config = require(__dirname+'/config/database'); // get db config file
var jwt = require('jwt-simple');
require(__dirname + '/config/passport')(passport);


mongoose.connect(config.database);


// konfigurisemo bodyParser()
// da bismo mogli da preuzimamo podatke iz POST zahteva
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());
var port = process.env.PORT || 8080; // na kom portu slusa server

// ruter za blogEntries
var userRouter = express.Router(); // koristimo express Router
// kreira novi user account (POST http://localhost:8080/api/signup)
userRouter.post('/signup', function(req, res) {
  if (!req.body.name || !req.body.password) {
    res.json({success: false, msg: 'Please pass name and password.'});
  } else {
    var newUser = new User(req.body);
    // save the user
    newUser.save(function(err) {
      if (err) {
        return res.json({success: false, msg: 'Username already exists.'});
      }
      res.json({success: true, msg: 'Successful created new user.'});
    });
  }
})
.post('/authenticate', function(req, res) {// /api/users/authenticate
  User.findOne({
    name: req.body.name
  }, function(err, user) {
    if (err) throw err;
    
    if (!user) {
      res.send({success: false, msg: 'Authentication failed. User not found.'});
    } else {
      // proveri da li se password poklapa
      user.comparePassword(req.body.password, function (err, isMatch) {
        if (isMatch && !err) {
          // ako je pronadjen user i poklapa se password kreira token
          // da li ceo user treba da bude u tokenu? 
          var token = jwt.encode(user, config.secret);
          // vraca informaciju kao JWT token
          var resObject = { success: true, token: 'JWT ' + token };
          res.json(resObject);
        } else {
          res.send({success: false, msg: 'Authentication failed. Wrong password.'});
        }
      });
    }
  });
})
.get('/memberinfo', passport.authenticate('jwt', { session: false}), function(req, res) {
  var token = getToken(req.headers);
  if (token) {
    var decoded = jwt.decode(token, config.secret);
    User.findOne({
      name: decoded.name
    }, function(err, user) {
      if (err) throw err;
      
      if (!user) {
        return res.status(403).send({success: false, msg: 'Authentication failed. User not found.'});
      } else {
        res.json({success: true, msg: 'Welcome in the member area ' + user.name + '!'});
      }
    });
  } else {
    return res.status(403).send({success: false, msg: 'No token provided.'});
  }
});

var getToken = function (headers) {
  if (headers && headers.authorization) {
    var parted = headers.authorization.split(' ');
    if (parted.length === 2) {
      return parted[1];
    } else {
      return null;
    }
  } else {
    return null;
  }
};

// ruter za blogEntries
var blogEntryRouter = express.Router(); // koristimo express Router

// definisanje ruta za blog
blogEntryRouter
.get('/:id', function(req, res, next) {
  BlogEntry.findOne({
    "_id": req.params.id
  }).populate('comments').exec(function(err, entry) {
      // ako se desila greska predjemo na sledeci middleware (za rukovanje greskama)
      if (err) next(err);
      res.json(entry);
    });
})
.get('/', function(req, res) {
  var entry={};
  if (req.query.title) {
    entry={title: new RegExp(req.query.title, "i")};
  }
  if (req.query.entry){
    entry={entry: new RegExp(req.query.entry,'i')};
  }
  BlogEntry.find(entry).populate('comments').exec(function(err, data, next) {
    res.json(data);
  });
})
.post('/', passport.authenticate('jwt', { session: false}), function(req, res, next) {
  var blogEntry = new BlogEntry(req.body);
  blogEntry.save(function(err, entry) {
    if (err) next(err);

    res.json(entry);

  });
})
.put('/:id', passport.authenticate('jwt', { session: false}), function(req, res, next) {
  var token = getToken(req.headers);
    var decoded = jwt.decode(token, config.secret);
    if(!decoded.role||decoded.role!=='admin'){
      return res.status(403).send({success: false, msg: 'Not allowed.'});    
    }
    BlogEntry.findOne({
      "_id": req.params.id
    }, function(err, blogEntry) {
      if (err) next(err);
      var newEntry = req.body;
      blogEntry.title = newEntry.title;
      blogEntry.description = newEntry.description;
      blogEntry.entry = newEntry.entry;
      blogEntry.save(function(err, blogEntry) {
        if (err) next(err);
        res.json(blogEntry);
      });
    });
})
.delete('/:id', 
  passport.authenticate('jwt', { session: false}), function(req, res, next) {
  var token = getToken(req.headers);
  var decoded = jwt.decode(token, config.secret);
  if(!decoded.role||decoded.role!=='admin'){
      return res.status(403).send({success: false, msg: 'Not allowed.'});    
    }
  BlogEntry.remove({
    "_id": req.params.id
  }, function(err, successIndicator) {
    if (err) next(err);
    res.json(successIndicator);
  });
});

// ruter za comments
var commentRouter = express.Router(); // koristimo express Router

commentRouter
.post('/blogEntry/:id', passport.authenticate('jwt', { session: false}), function(req, res, next) {
  var comment = new Comment(req.body);
  BlogEntry.findOne({"_id":req.params.id},function (err, entry) {
    if(err) next(err);
    comment.save(function (err, comment) {
      if(err) next(err);
      BlogEntry.findByIdAndUpdate(entry._id, {$push:{"comments":comment._id}}, function (err, entry) {
        if(err) next(err);
        res.json(entry);
      });
    });
  });
})
.delete('/:id', function (req, res, next) {
  Comment.remove({"_id":req.params.id},function (err, successIndicator) {
    if(err) next(err);
    res.json(successIndicator);
  });
});

// dodavanje rutera za user /api/user
app.use('/api/users', userRouter);
// dodavanje rutera za blogEntries /api/blogEntries
app.use('/api/blogEntries', blogEntryRouter);
// dodavanje ruter za komentare /api/blogEntries
app.use('/api/comments', commentRouter);
//klijentsku angular aplikaciju serviramo iz direktorijuma client
// app.use('/blog', express.static(__dirname + '/client'));
// app.use('/lib', express.static(__dirname + '/bower_components'));
app.use(express.static(__dirname + '/client'));
app.get('*', (req, resp) => {
  resp.sendFile(__dirname+'/client/index.html');
})


//na kraju dodajemo middleware za obradu gresaka
app.use(function(err, req, res, next) {
  var message = err.message;
  var error = err.error || err;
  var status = err.status || 500;

  res.status(status).json({
    message: message,
    error: error
  });
});


// Pokretanje servera
app.listen(port);


console.log('Server radi na portu ' + port);
