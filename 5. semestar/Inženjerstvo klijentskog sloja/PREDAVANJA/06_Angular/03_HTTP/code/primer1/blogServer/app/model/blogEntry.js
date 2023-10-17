var mongoose = require('mongoose');
var mongoosePaginate = require('mongoose-paginate');
var Schema = mongoose.Schema;

// kreiramo novu shemu
var blogEntrySchema = new Schema({
  title: {
    type: String,
    required: true,
    unique: true
  },
  description: String,
  entry: {
    type: String,
    required: true
  },
  createdAt: Date,
  updatedAt: Date,
  // napomena! komentari su u ovom primeru implementirani kao reference zbog ilustracije rada sa referencama
  // u realnom sluacju bolje bi bilo implementirati ih kao poddokumente
  comments: [{ type: Schema.Types.ObjectId, ref: 'Comment' }]
});

// prilikom snimanja se postavi datum
blogEntrySchema.pre('save', function(next) {
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

//koristimo plugin za paginaciju
blogEntrySchema.plugin(mongoosePaginate);

// od sheme kreiramo model koji cemo koristiti
var BlogEntry = mongoose.model('BlogEntry', blogEntrySchema);

// publikujemo kreirani model
module.exports = BlogEntry;
