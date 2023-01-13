#get reaction
def get_reaction():
    try:
        temp_reaction_count = post_grid[i].find_element(By.CLASS_NAME, "_3n6Fnd22").text #pass number of reactions to temp_reaction_count 
        return temp_reaction_count #return value
    except NoSuchElementException: #handle no such element exception
        temp_reaction_count = 0 #pass 0 to temp_reaction_count if there is no element to be extracted 
        return temp_reaction_count #return 0 
        