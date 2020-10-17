# DataProject2Submission
UCI Data Analytics Project 2 Vishal Patel, Stephen Chu, Steve Thorne, Saburo Nakano

## Data Project 
Topic: To see the differences of players today in the NBA and their selves in college. This project aims to create interactive visuals to tell a story about how players in college translate to the NBA, and if there are certain trends we can find. 

## How to run/structure of files
### Python files:
get_data.py (not reccomended to run this)
May need pip install sportsreference and pip install dnspython
get_data.py is a python program that scrapes data for NBA and NCAA data, using a pypi package named sportsreference(https://pypi.org/project/sportsreference/) and along with a local csv file from Kaggle that contains college names for every NBA player (https://www.kaggle.com/justinas/nba-players-data). We combined this and merged with Google Maps API to get lat and long for each college, and eventually merge them into 4 collections of data. Then, we used Mongodb Atlas to store the data in the cloud, so the flask app calls the cloud server to jsonify the data. This ensures there are no local files being run in the flask app, only data from mongo.
 (NOTE* IT IS HIGHLY RECCOMENDED NOT TO RUN THIS PROGRAM. It takes up to 15 minutes to get the data )

app.py (need this to run flask app)
This houses the main flask app, but requires dnspython to run. Please make sure to pip install dnspython to run. The reason is because the data is in the cloud and this is needed in Pymongo to access it. Includes routes to all the pages for the site, including routes for data, which is returned jsonified. 

### Structure of HTML/CSS/JS
There is a template being used for the project, approved by instructors, called Forty by Pixelarity (https://pixelarity.com/forty)

html is in templates/
css and js is in static/assets/cs/ or static/assets/js

While all the html started as templates, there is modification to all of them. The home page is index.html, and there is an about page called proposal.html. Here is a breakdown of the view pages:

### View 1: Profile Chart (moving scatterplot)
The first view is a moving axis chart that plots player profiles in the x axis, including height and weight, and in the y axis different statistics such as PPG, APG, RPG, TPG(turnovers per game), SPG(steals per game). Each statistic on each axis is selectable and points move dynamically. Points also have tooltips to show the player, and a link to his Data Comparison page, shown in View 2.
ROUTE: /profile
FILES: updatedprofile.html and profilelogic.js

### View 2: Data Comparison (stacked Bargraphs for Each Player) -new library here
This view contains the new JS library not covered in class. This is called awesomeplete(https://projects.verou.me/awesomplete/) and is a search box and dropdown menu all in one. This makes it much easier to search for players, without having to remember spelling, and without a clunky dropdown. Once selected, and pressed the button, the players data is pulled from the cloud and put into a table divided by college and NBA side by side. Then below a dynamic Plotly bar graph takes the above data and plots is so its easy to compare a players college and NBA stats. Theres also another route that automatically fills the table for a specific player
ROUTES: /data,  /data/PLAYER_NAME
FILES: datapage.html, dataplayerpage.html, jsdatapage.js, datapageplayer.js

### View 3: Map of Colleges 
This view contains a map of the US that has marker clusters, and a basketball icon marker to mark College locations. When a marker is selected, it views the average statistics for an NBA player to come from that college.
ROUTE: /map
FILES: mappy.js, map.html

## Data Routes
### /NBAData
Has each NBA player's statistics.
### /NCAAData
Has each college player's statistics
### /NBALocation
Contains each NBA player, as well as the college name and Lat, Lon of the college they went to.
### /Averages
Contains each college with the average statistics of NBA players from that college.


* All data was stored from get_data.py, however already stored in the cloud in mongo. No need to run.
