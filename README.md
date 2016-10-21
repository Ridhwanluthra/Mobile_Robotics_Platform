# Mobile Robotics Platform	[![Build Status](https://travis-ci.org/Ridhwanluthra/Mobile_Robotics_Platform.svg?branch=master)](https://travis-ci.org/Ridhwanluthra/Mobile_Robotics_Platform)	[![Code Climate](https://codeclimate.com/github/Ridhwanluthra/Mobile_Robotics_Platform/badges/gpa.svg)](https://codeclimate.com/github/Ridhwanluthra/Mobile_Robotics_Platform)	[![Issue Count](https://codeclimate.com/github/Ridhwanluthra/Mobile_Robotics_Platform/badges/issue_count.svg)](https://codeclimate.com/github/Ridhwanluthra/Mobile_Robotics_Platform)
Includes all the essentials to building a mobile robot capable to knowing its location in a given map and finding its way from one location to the other.

main.py
	Calls all the other functions and this is the only function that needs to be called to start the process

motion_planning.py
	motion planning class, should include all the motion planning algorithms (need to do this)

search.py
	executes A* search in the given grid.

get_smooth_path.py
	gives the smooth path from a 2d array of xy coordinates given.

particle_localisation.py
	a simple simulation showing localisation using particle filters.

particle_test.py
	localisation using particle filters without the simulation.	

gradient_decent.py
	a simple gradient decent algorithm to find the actual movement any expected movement.

map_from_matlab.py
	an atempt to create a map from a matlab image given showing the obstaces.

localisation_kalman.py
	localisation using kalman filters (needs to be corrected and landmarks be added)

collision_tester.py
	a way to test if the robot colides in an obstacle (started initialy now not sure if needed)

dead_reconing.py
	localisation using dead_reconing, the most basic algorithm in localisation.
