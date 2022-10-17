# NextDoorScraping
This is an extended project for <em> Building Communitarianism in Diverse Neighbourhoods : A Perspective of Communication Infrastructure Theory </em> (honours thesis, under supervision of Duyvendak & Hurenkamp in 2021). The original paper investigats how hyperlocal social media Nextdoor facilitates community building through the lens of communication infrastructure theory (CIT, Ball-Rokeach et al., 2001) by the means of manual qualitative content analysis. 

This extended project is to automate the data collection process on Nextdoor to make the procedure more efficient and allow for a multi-method approach to analyse Nextdoor. 

Latest update: 17/10/2022

## Current Status
Initial code commited. However, there are few [to-dos](https://github.com/jyeungtin/NextDoorScraping/edit/main/README.md#to-do) to make the scraping more efficient and complete. 

The scraping of the following items can be automated:

1. Reactions counts
2. Expand comments 
3. Comments count and comment text
4. Body texts
5. Post ID
6. Formatted date(with exceptions, see [to-dos](https://github.com/jyeungtin/NextDoorScraping/edit/main/README.md#to-do))

## To-do
1. Scrolling by date, currently is manually interrupted
2. Get reactions categorisations (sad, likes, laughs, etc.) 
3. Get dates that are at least 6 days old, posts that are 5 day-old or more recent will return a faulty date due to a different formatting on NextDoor
4. Not urgent, but can also automate login processes and allow for multiple neighbourhoods to be examined (this is not within the scope of the project)
