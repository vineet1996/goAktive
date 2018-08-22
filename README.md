hello,

steps to execute

1.Clone these files in a directory

2.Open terminal and move to the directory where you have cloned these files

3.Activate venv by executing following command 
    $ source venv/bin/activate 
  when it is executed, it some how look like 
    (venv) $

4.Then run the flask 
    $flask run

5.Open browser with 
    localhost:5000 
 It returns False for Malware urls stored in database.
 It returns True if the requested url is not in database.

One thing i used mysql so i have local database .You should install mysql

after you install mysql
* if you keep root password as "123" it would be better.
* if mysql is already installed 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/proj'
  In __init__.py file just need to change the username and password as per the database. 
1. create database and use it
      >>create database proj;
      >>use proj;

2. create table 
      create table links (id int not null auto_increment, url varchar(100),  primary key(id));

3.insert values
      insert into links (url) values ("image"),("qwert"),("zxcv"),("asdf"),("1234");
