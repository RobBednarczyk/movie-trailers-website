
|\    /|   __           __		\        / __  __  __   ___  __
| \  / |  /  \	\  / | |__		 \  /\  / |__ |__)(__ |  |  |__
|  \/  |  \__/	 \/  | |__ 		  \/  \/  |__ |__) __)|	 |  |__  


1. INTRODUCTION

	The "Movie Website" project is an application written in Python. 
	It enables a user to dynamically generate and view a website with links to movies provided in the input.

2. HOW TO RUN THE APPLICATION

	A user shoud install Python environment on their system. 
	Then they should download the files from a Github repository https://github.com/RobBednarczyk/movie-trailers-website.

	a) Unix systems

		A user should navigate to the folder with the downloade files using the terminal.
		The application is run by typing the command: python entertainment_center.py

	b) Windows systems

		Although it is possible to use a Windows command prompt just like in point a) the user is encouraged to download 
		a Python Integrated Development environment such as "IDLE" or "CANOPY and run the environment_center.py file.

3. RUNNING THE APPLICATION

	Firstly the users are asked if they would like to add details of a movie. 
	Only two answers are allowed in this step: yes [y] or no [n].
	If the answers is yes then the user is asked to provide:

		* the title of the movie 
		* a short storyline 
		* a url of the poster to be displayed on the webpage
		* a url of the movie trailer

	The answers to these 4 questions should be provided as a string of characters.
	After giving details about a movie the users are asked again if they want to add an additional movie.
	If the answer is "No" the application will generate a website with the movies which details were uploaded.


