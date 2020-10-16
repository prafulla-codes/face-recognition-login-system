<h1 align=center> Face Recognition Login System </h1>
<hr/>
<h4 align="center"> :camera: A facial recognition based login system using Python,HTML,CSS and Bootstrap 
</h4>
<h2>Preview</h2>
<img src="Preview/p1.png">
<img src="Preview/p2.png">
<hr/>
<h2> Tools & Libraries Used </h2>
<hr/>
<ul>
  <b>
<li> Python - face_recognition - https://github.com/ageitgey/face_recognition </li>
<li> XAMPP - https://www.apachefriends.org/download.html </li>
<li> Bootstrap - https://getbootstrap.com/ </li>
<li> CGI </li>
    
    
  </b>
</ul>
<strong> Note </strong>  - These files must be hosted on XAMPP Apache server or other server, else login.py will not work.

<hr/>
<h2> Working </h2>

- Install Python
- Install XAMPP
- Navigate to `htdocs` fodler and clone this project.
- Open `login.py` and make sure to replace the top comment `#! C:\Users\PRAFULLA\AppData\Local\Programs\Python\Python39\python.exe` with your python path.
- Navigate to `htdocs/face-recognition-login-system` and execute the following command `pip install -r requirements.txt`
- Navigate to `xampp/apache/config` and modify the `httpd.conf` file by adding  
```conf
Options Indexes FollowSymLinks Includes ExecCGI
AddHandler cgi-script .py .cgi .pl .asp
```   
at the end of the file. Then save & exit
- Then run XAMPP & go to `localhost/face-recognition-login-system/login.html`
- Put all the images of students in the 'students' folder 
  <img src='Preview/n1.png'>
- Pictures must be in the format (email_address_of_student).jpg 
 
 <img src='Preview/n2.png'><br>
<b>Optional -</b> <i>you can create a seperate registration form for students, where they may upload their picture and the picture gets stored as (email_address).jpg in the 'students' folder.</i>

<hr/>

