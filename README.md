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

5.Open browser 

   Endpoint to add malware url to database
   (Note: add some urls to the database )
      
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
           
  Endpoint to check the url is safe or not

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
  
 

