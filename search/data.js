const elasticsearch = require('elasticsearch');

const client = new elasticsearch.Client({
    hosts:['http://localhost:9200']
});

client.ping({
    requestTimeout: 30000,
}, function(error) {
    if(error) {
        console.error('Elasticsearch cluster is down!');
    }else{
        console.log('Everything is ok');
    }
});

client.indices.create({
    index: 'boles'
}, function(error, response, status) {
    if(error) {
        console.log(error);
    }else{
        console.log("created a next index", response);
    }
});



var JSONStream = require('JSONStream')
var es = require('event-stream')
var fs = require('fs')
var stream = fs.createReadStream('bole.json', {encoding: 'utf8'})
var parser = JSONStream.parse('*')
stream.pipe(parser)
    .pipe(es.mapSync( data => {
        console.log('-------------------')
        console.log(data)
    }))

