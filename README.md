hello,

steps to execute

1.Clone these files in a directory

2.Open terminal and move to the directory where you have cloned these files

3.Activate venv by executing following command 
   >> $ source venv/bin/activate 
   
  when it is executed, it some how look like 
   
   >> (venv) $

4.Install flask then run it
   >> pip3 install flask
   
   >> (venv)$flask run

5.Open browser with 

    localhost:5000/urlinfo/1/<url>
 It returns true if url is safe
            {
             "success": true, 
             "value": "url"
            }
 It returns false if url is malware url
            {
               "success": false, 
               "value": "url"
            }
  
 Endpoint to add malware url to database
      
      localhost:5000/add/<url>
 It returns true and url is added to database
            {
             "success": true, 
             "value": "url added to database"
            }
 It returns false if url already present in database
            {
               "success": false, 
               "value": "url already present in database"
            }

One thing i used mysql so i have local database .You should install mysql

after you install mysql
* if you keep root password as "123" it would be better.
* if mysql is already installed 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/proj'
  In __init__.py file just need to change the username and password as per the database. 
1. create database and use it
      >>create database proj;
      >>use proj;

2. create table:
      >>create table links (id int not null auto_increment, url varchar(100),  primary key(id));

3.insert values:
      >>insert into links (url) values ("image"),("qwert"),("zxcv"),("asdf"),("1234");
