//index.js
// 需要Elasticsearch librray
const elasticsearch = require('elasticsearch');
// 实例化一个elasticsearch客户端
const client = new elasticsearch.Client({
   hosts: [ 'http://localhost:9200']
});
//require Express
const express = require( 'express' );
// 实例化一个表达式的实例并将其保存在一个名为app的常量中
const app     = express();
// 引入body-parser库。将用于解析主体请求
const bodyParser = require('body-parser')
//require the path library
const path    = require( 'path' );

// ping客户端以确保Elasticsearch已启动
client.ping({
     requestTimeout: 30000,
 }, function(error) {
 // 此时，eastic搜索已关闭，请检查您的Elasticsearch服务
     if (error) {
         console.error('elasticsearch cluster is down!');
     } else {
         console.log('Everything is ok');
     }
 });

// 使用bodyparser作为中间件
app.use(bodyParser.json())
// 设置应用程序侦听的端口
app.set( 'port', process.env.PORT || 3001 );
// 设置路径来提供静态文件
app.use( express.static( path.join( __dirname, 'public' )));
// 启用CORS
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS');
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

// 定义了基本路线并返回一个名为tempate.html的HTML文件
app.get('/', function(req, res){
  res.sendFile('template.html', {
     root: path.join( __dirname, 'views' )
   });
})

// 定义应该返回弹性搜索结果的/ search路径
app.get('/search', function (req, res){
  // 声明查询对象以搜索弹性搜索，并从找到的第一个结果中仅返回200个结果。
  // 还匹配其中名称与发送的查询字符串类似的任何数据
  let body = {
    size: 200,
    from: 0,
    query: {
      match: {
        title: req.query['q'],

      }
    }
  }
  // 在索引中执行实际的搜索传递，搜索查询和类型
  client.search({index:'bole',  body:body, type:'doc'})
  .then(results => {
    res.send(results.hits.hits);
  })
  .catch(err=>{
    console.log(err)
    res.send([]);
  });

})
// 监听一个指定的端口
app.listen( app.get( 'port' ), function(){
  console.log( 'Express server listening on port ' + app.get( 'port' ));
} );

app.get('/v2', function(req, res){
  res.sendFile('template2.html', {
     root: path.join( __dirname, 'views' )
   });
})
