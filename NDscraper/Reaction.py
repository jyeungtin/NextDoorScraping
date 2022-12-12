#get reaction
def get_reaction():
    try:
        temp_reaction_count = post_grid[i].find_element(By.CLASS_NAME, "_3n6Fnd22").text
        return temp_reaction_count
    except NoSuchElementException:
        temp_reaction_count = 0
        return temp_reaction_count
        