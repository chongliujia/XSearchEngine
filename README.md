# XSearchEngine
项目简介
=
利用scrapy爬虫爬取数据，并将数据存入elasticsearch中，之后利用一个网页做成一个搜索引擎

###功能特性

可以进行实时搜索

###环境依赖


UNIX/LINUX   
scrapy 1.4.0  
python 3.6.8  
elasticsearch-6.5.4  
node v8.11.2  
vue 2.9.6 

###部署步骤


进入elasticsearch文件中的bin文件 在终端中输入： 
<code>
./elasticsearch start
</code>  
之后进入search文件后，在终端中输入：  
<code>
node index.js
</code>

项目最终效果图
=
![Alt text](image/demo.png)
