var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
// koristimo mongoose model koju smo kreirali u folderu model
var BlogEntry = require(__dirname + '/app/model/blogEntry');
var Comment = require(__dirname + '/app/model/comment');


mongoose.connect('mongodb://127.0.0.1/blogApp');


// konfigurisemo bodyParser()
// da bismo mogli da preuzimamo podatke iz POST zahteva
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());
var port = process.env.PORT || 8080; // na kom portu slusa server

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
    if (req.query.err){
      //namerno izazivamo gresku na serveru 
      //da bismo videli kako se greska obradjuje na klijentu
      res.status(status).json({
        message: 'greska',
        error: 500
      });
      return
    }
    if (req.query.title) {
      entry={title: new RegExp(req.query.title, "i")};
    }
    if (req.query.entry){
      entry={entry: new RegExp(req.query.entry,'i')};
    }
    //ukoliko je korisnik prosledio page query parametar
    //preuzimamo paginirane vrednosti na stranicama od po 10 elemenata
    if (req.query.page) {
      //koristimo https://github.com/edwardhotchkiss/mongoose-paginate
      BlogEntry.paginate(entry,{page:req.query.page, limit:10, populate:'comments'}, function(err, data, next) {
        console.log(data);
        res.json(data);
      });
    }
    //ukoliko korisnik nije prosledio page query parametar
    //posaljemo sve vrednosti
    else{
      BlogEntry.find(entry).populate('comments').exec(function(err, data, next) {
        res.json(data);
      });
    }
  })
  .post('/', function(req, res, next) {
    var blogEntry = new BlogEntry(req.body);
    blogEntry.save(function(err, entry) {
      if (err) next(err);

      res.json(entry);

    });
  })
  .put('/:id', function(req, res, next) {
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
  .delete('/:id', function(req, res, next) {
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
.post('/blogEntry/:id',function(req, res, next) {
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

// dodavanje rutera zu blogEntries /api/blogEntries
app.use('/api/blogEntries', blogEntryRouter);
// dodavanje ruter zu komentare /api/blogEntries
app.use('/api/comments', commentRouter);
//klijentsku angular aplikaciju serviramo iz direktorijuma client
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
