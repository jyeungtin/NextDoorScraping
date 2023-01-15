# NextDoorScraping
This is an extended project for <em> Building Communitarianism in Diverse Neighbourhoods : A Perspective of Communication Infrastructure Theory </em> (honours thesis, under supervision of Duyvendak, J.W. & Hurenkamp, M. in 2021). The original paper investigats how hyperlocal social media Nextdoor facilitates community building through the lens of communication infrastructure theory (CIT, Ball-Rokeach et al., 2001) by the means of manual qualitative content analysis. 

This extended project is to automate the data collection process on Nextdoor to make the procedure more efficient and allow for a multi-method approach to analyse Nextdoor. 

Latest update: 15/01/2023

## IMPORTANT NOTE!
The scraper only works for the Dutch version of NextDoor right now! 

If you wish to contribute to the scraper, please contact me on Twitter.

## Current Status
Alpha testing! There are few [to-dos](https://github.com/jyeungtin/NextDoorScraping/edit/main/README.md#to-do) to make the scraping more efficient and complete. 

The scraping of the following items can be automated:

1. Reactions counts
2. Expand comments (multilevel)
3. Comments count and comment text
4. Body texts
5. Post and comment ID
6. Formatted date 
7. Scrolling by date (with exceptions, see [to-dos](https://github.com/jyeungtin/NextDoorScraping/edit/main/README.md#to-do))
8. Get post user_name and comment user_name 
9. Get neighbourhood data of posts' and comments' authors

## To-do
1. Not urgent, but can also automate login processes and allow for multiple neighbourhoods to be examined (this is not within the scope of the project)
2. Scrolling by date may be at times faulty as the feed on Nextdoor is not solely ranked by post date, but also other factors. If we are to scroll by date, we may stumble upon a 2-year-old post in the middle of newer posts. This is to be resolved.
3. English version of Nextdoor.

## Backlog
1. Multimedia content
2. Get reactions categorisations (sad, likes, laughs, etc.)
