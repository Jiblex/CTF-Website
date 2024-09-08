***Continuous Development Guide:***

**Deployment Instructions**

*Challenges not within docker containers can:*

1. Can be uploaded to whatever platform is being used for the CTF and players can download those files and solve for the flags pertaining to those files.

2. Files can be provided to players in some folder, or whatever means the CTF makers would prefer, and solve for the flags pertaining to those files.





*Challenges within Docker Containers:*

These challenges can all be ran with the single following command:
$docker run -it <<container_name>> 

This applies to the website challenges as well. Running the aforementinoed command will give back an IP (the one that is not localhost) and the website can be accessed via that IP (note that it is http not https).





**Continuous Development**


**Non-website Challenges**

These challenges are all stand alone and have no special continuous development guide. The challenges can be edited as one sees fit, and other challenges can be created in their separate environments, whether that be a Docker container or files that host the challenges within themselves. 





**Website Challenges**

*Note* For debug mode run "export FLASK_DEBUG=1" before starting up website or edit the run.py file to set debug=True. 

*Note* The templating language used is Jenja2, not JavaScript. Variables from python can be used in the html templates by passing the variable into the render_template() funtion in the form "render_template("template.html", var=var)" where the variable var is being passed into the template as var, and can be used refered to as var. If and loops are made using {% code %} and other code is in {{ code }}.


The file system for the website is the following:

ctf_web:
	- CTF_env
	- Dockerfile
	- README.md
	- requirements.txt
	- run.py
	- app
		- html_templates
		- static
		- __init__.py
		- forms.py
		- models.py
		- routes.py

- CTF_env can be used to create a virtual environment with all the needed python packages. It can be started with the following command:
$source CTF_web/bin/activate 
and stopped with:
$deactivate


- Dockerfile has instructions for docker container creation. 


- README.md has all of the challenge details, list of users on the website, and commands to run the flask website (you will probably not want to run it in the docker container when developping).


- requirements.txt has all the python packages that the Dockerfile downloads when it builds the container. 


- run.py is used to run the website. Use "python3 run.py". Conversely use "flask run" if command has been setup (which the virtualenv should have). 


- In app:

	- html_templates holds all of the html templates the website uses. The names are self explanatory and all mentioned in the routes.py file with the given routes they are being used for.


	- static has the css files, images, wordlists and can hold other static information.


	- __init.py__ acts as app. It sets up all environment variables. To import from it use "from app import app.package_name". Doing it this way avoids circular import errors.


	- forms.py holds all the form classes used on the website, such as login form, registration form...


	- models.py holds all of the database table classes used in the SQLite database. 


	- routes.py has all of the routes of the website along with any GET/POST request validation, and handling of inputs. All challenge specific routes are seperated by "-------" and their names are marked within these lines. 


Use the above descriptions to continue using this project organization. One can of course change the setup as they see fit. 




