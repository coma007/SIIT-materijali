var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// kreiramo novu shemu
var commentSchema = new Schema({
  signedBy: String,
  text: {
    type: String,
    required: true
  },
  createdAt: Date,
  updatedAt: Date
});
//mozemo da napravimo rekurzivnu shemu, pa da komentari imaju svoje podkomentare
commentSchema.add({comments:[commentSchema]});

// prilikom snimanja se postavi datum
commentSchema.pre('save', function(next) {
  // preuzmemo trenutni datum
  var currentDate = new Date();

  // postavimo trenutni datum poslednju izmenu
  this.updatedAt = currentDate;

  // ako nije postavljena vrednost za createdAt, postavimo je
  if (!this.createdAt)
    this.createdAt = currentDate;

  // predjemo na sledecu funckiju u lancu
  next();
});

// od sheme kreiramo model koji cemo koristiti
var Comment = mongoose.model('Comment', commentSchema);

// publikujemo kreirani model
module.exports = Comment;
