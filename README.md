# Simulation of NBA Games

This project will simulate National Basketball Association (NBA) games for the purpose of
predicting the outcomes of real world games. Each game will be repeated 1000 times to
approximate the chance of a particular team winning a match. Predictions will be compared to
Las Vegas odds, FiveThirtyEight, and home court advantage results. Home court advantage
will be used as the baseline for our simulations since historically it predicts winners 60% of the
time. Simulations will use the latest data available, obtaining
real world updated data before each day’s simulation. As a secondary indicator of successful
approximations of game outcomes each game’s spread will be compared to the Las Vegas
spread and the FiveThirtyEight spread. The spread is the number of points a team is predicted
to win by. For example, if the home team is predicted to win by 2 points, then the spread is -2.

# Data Collection 
Team and player data will be gathered from stats.nba.com. This is a freely accessible website hosted by the NBA. This site contains a rich set of information, such as the exact location of every shot for every game. Unfortunately, this site does not have a public API, so scripts will be devised for data scrapping. Once that data is gathered it will be transformed into data that will allow us to easily calculate various probability distributions. Below is a list of collected data.  

* Team Rosters: The team rosters for each of the 30 teams in the NBA. Of particular
importance is the player ID used to store each player’s statistics.
* Player Shooting Log: A record of every shot taken by each player during 2017-2018
regular season. This includes:
   * Made or missed shots.
   * Whether a shot is for 2 points or 3 points.
   * Location on the court.
* Team Per 100 Possession Averages: Contain the averages for the 2017-2018 regular
season. This includes turnovers, offensive rebounds, field goal attempts, and blocked
field goal attempts per 100 possessions.

Each record obtained is saved in comma-separated values (csv) files and stored to the local hard
drive.


# Data Selection
While there is a vast amount of information being tracked for each game in the NBA, only a few
factors where used for our simulations: 100 possessions per team, player shot selection, player
field goal percentages, team turnovers, team blocked shots, team offensive rebounds, and free
throws made. The reasoning behind this decision is that any given team can score an amount
of points that is limited by the number of field goals attempted for any particular game.
Furthermore, field goal attempts are limited by the number of possessions a team has per
game, which are increased with offensive rebounds and decreased with turnovers.


# Probability Distributions
Each team is composed of an official roster containing roughly 16 players.  The roster may fluctuate due to player injuries and may also include players in the G League .  For example, the Warriors current roster contains the following players:

Players | Players
-------|--------------------
Patrick McCaw |	David West
JaVale McGee  |	Quinn Cook
Jordan Bell |	Kevon Looney
Nick Young |	Klay Thompson
Andre Iguodala |	Damian Jones
Chris Boucher |	Omri Casspi
Zaza Pachulia |	Draymond Green
Stephen Curry |	Shaun Livingston
Kevin Durant |	


Each player has a record of every shot taken for the current season.  


SHOT |	PLAYER_NAME |	EVENT_TYPE |	SHOT_TYPE |	SHOT_ZONE_AREA |	SHOT_ZONE_RANGE 
-----|--------------|--------------|--------------|--------------------|------------------------
0 |	Kevin Durant |	Missed Shot |	3PT Field Goal |	Right Side Center(RC) |	24+ ft.
1 |	Kevin Durant |	Missed Shot |	2PT Field Goal |	Center(C) |	8-16 ft.
2 |	Kevin Durant |	Made Shot |	2PT Field Goal | Right Side(R) |	8-16 ft.
3 |	Kevin Durant |	Missed Shot |	2PT Field Goal |	Right Side(R) |	8-16 ft.
4 |	Kevin Durant |	Made Shot |	3PT Field Goal |	Right Side Center(RC) |	24+ ft.
N |	…….. |	…….. |	……..	 |……..|	……...


Using the shooting records and rosters we will calculate each team’s and player’s shooting distributions.  
To select which shooter will shoot the ball for any given possession, each player’s total shots are divided by the total shots taken by the entire roster for the current season.

Each player will have a shooting distribution that accounts for all shots taken by that player for the 2017-2018 season.  All shots will be grouped into 15 zones.  These zones will be used to calculate the player’s shooting distribution and accuracy from different locations on the court.  When selecting the shot a player will take, first sample from the player’s percent of total shots, then assigned the probability of making the shot with its respective accuracy. 


Distance |	Location|	Percent of Total Shots|	Accuracy
---------|--------------|-----------------------------|----------
Less Than 8 ft.|	Center|	20.2%|	60.8%
8-16 ft.|	Center|	6.3%|	52.3%
8-16 ft.|	Left Side|	3.1%|	44.2%
8-16 ft.|	Right Side|	4.5%|	37.0%
16-24 ft.|	Center	|3.4%	|36.1%
16-24 ft.|	Left Side Center|	3.7%|	41.1%
16-24 ft.|	Left Side|	3.1%	|63.6%
16-24 ft.|	Right Side Center|	5.7%	|41.7%
16-24 ft.|	Right Side|	2.8%|	53.8%
24+ ft.|	Center	|5.8%|	33.8%
24+ ft.	|Left Side Center|	10.6%|	40.4%
24+ ft.	|Left Side|	4.9%|	48.5%
24+ ft.	|Right Side Center|	17.5%|	43.2%
24+ ft.	|Right Side|	8.1%	|40.2%
Back Court|	Back Court	|0.0%	|0.0%


The following is the list of other statistics that will be used that are gathered precomputed by the NBA.

Statistic | Purpose
--------------------|--------------------------------------------
Offensive Rebounding|	Offensive rebounds per 100 possessions
Offensive Blocked Shots	|Shots blocked will attempting a shot per 100 possessions.
Turnovers|	Turnovers per 100 possessions
Free throw|	Free throws per 100 possessions


# Events
The following are all the possible events used in the simulation:

* ****Possession****:  A team has taken possession of the ball.
* ****Pick a Shooter****:  A player is selected to take a shot.
* ****Shot****:  A player shoots the ball.
* ****Turnover****:  Possession is passed to the other team.
* ****Block shot****:  A shot is blocked.
* ****Offensive Rebound****:  A team adds a possession after a missed shot. 


# System Initialization
1.	Each team loads its roster.
2.	Player statistics are calcualted and assigned.
3.	Team statistics are loaded.
4.	Set possesion count for each team at 100.
5.	Begin simulation.


# Flow of Events
The simulation will start with Team A possessing the ball.  Next, Team A will have a chance to commit a turnover by sampling from their turnover rate per 100 possessions.  If the ball is not turned over, then a player is selected to shot the ball.  Next, we check whether the shot is going to be blocked by sampling from the teams shots blocked rate per 100 possessions.  If the shot is not blocked, then the shot is taken.  If the shot is blocked, then both teams have a 50% chance of recovering the ball.  The player’s shot location and shooting percentages will be used to determine if the shot goes in.  If the shot goes in, then possession is passed to Team B.  If the shot misses, then we check if Team A recovers an offensive rebound using the per 100 possessions rate.  If Team A does not recover the offensive rebound, then Team B is assumed to recover the defensive rebound.  This process is repeated until all possessions are completed.


![](https://github.com/tony-mtz/nba-simulation/blob/master/doc/bball.png)
