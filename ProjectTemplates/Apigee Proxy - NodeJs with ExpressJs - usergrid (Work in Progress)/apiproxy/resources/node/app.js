// Require express (http://expressjs.com/api.html)
var express = require('express');
//var config  = require('./config') //uncomment if needed

// Start 
var app = express(express.logger());

// Configurations via middleware
app.use(express.json());
app.use(express.urlencoded());

/*API definition : The template follows the RV API design pattern.
Change it to suit your needs.*/

//1) Get all resources
app.get('/RESOURCE',function(req, res) {
	//handle the request & set the response
});

//2) Get a single resource
app.get('/RESOURCE/:id',function(req, res) {
	//handle the request & set the response
	var id = req.params.id;
});

//3) Create a new resource
app.post('/RESOURCE',function(req, res) {
	//handle the request & set the response
	var body = req.body;

});

//4) Update an existing resource
app.put('/RESOURCE/:id',function(req, res) {
	//handle the request & set the response
	var id = req.params.id;

});

//5) Delete an existing resource
app.del('/RESOURCE/:id',function(req, res) {
	//handle the request & set the response
	var id = req.params.id;

});


//Port number the app will go live on
app.listen(8888); //change PORT number if something is already running on 
console.log('RESOURCE app running on 8888');