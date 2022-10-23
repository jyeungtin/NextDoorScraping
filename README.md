# NextDoorScraping
This is an extended project for <em> Building Communitarianism in Diverse Neighbourhoods : A Perspective of Communication Infrastructure Theory </em> (honours thesis, under supervision of Duyvendak & Hurenkamp in 2021). The original paper investigats how hyperlocal social media Nextdoor facilitates community building through the lens of communication infrastructure theory (CIT, Ball-Rokeach et al., 2001) by the means of manual qualitative content analysis. 

This extended project is to automate the data collection process on Nextdoor to make the procedure more efficient and allow for a multi-method approach to analyse Nextdoor. 

Latest update: 23/10/2022

## Current Status
Initial code commited. However, there are few [to-dos](https://github.com/jyeungtin/NextDoorScraping/edit/main/README.md#to-do) to make the scraping more efficient and complete. 

The scraping of the following items can be automated:

1. Reactions counts
2. Expand comments 
3. Comments count and comment text
4. Body texts
5. Post ID
6. Formatted date (with exceptions, see [to-dos](https://github.com/jyeungtin/NextDoorScraping/edit/main/README.md#to-do))
7. Scrolling by date (with exceptions, see [to-dos](https://github.com/jyeungtin/NextDoorScraping/edit/main/README.md#to-do))
8. Get post user_name and comment user_name 

## To-do
1. Scrolling by date is not possible if the date is less than a year ago but in a different year (e.g., you cannot scroll to dec 2021 if we are now nov 2022). See point 4 for an elaboration.
2. Get reactions categorisations (sad, likes, laughs, etc.)
3. Not urgent, but can also automate login processes and allow for multiple neighbourhoods to be examined (this is not within the scope of the project)
4. Add a function to check date difference to correctly parse date. Nextdoor will not show the year if the date is not at least a year old (e.g., if today is 23/10/2022, 01/11/2021 will be shown as 1 nov. instead of 1 nov. 2021). A new function needs to be written to solve this problem. 
