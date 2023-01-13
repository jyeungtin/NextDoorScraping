#get links from result lists
post_grid = driver.find_elements(By.CLASS_NAME, "css-n4lbsh") #pass list of individual posts to post_grid

post = []
text = []
neighbourhood_name = []
post_username = []
comment_count = []
post_date = []
reaction_count = []


for i in range(len(post_grid)):
    try: 
        print(f"Current post: {i}") #Tell us which post the script is processing :)

        #click on  "more comments" and "more content" button and find comments count
        try:
            comment_button = post_grid[i].find_element(By.CLASS_NAME, "css-mn71l5").find_element(By.CSS_SELECTOR, 'button') #find more comments button
            driver.execute_script("arguments[0].click();", comment_button) #use javascript to click the button

            expand_text_button = post_grid[i].find_element(By.CLASS_NAME, "css-zglld0").find_element(By.CSS_SELECTOR, 'button') #find expand text button
            driver.execute_script("arguments[0].click();", expand_text_button) #use javascript to click the button
            
            time.sleep(1) #wait one second for comments to load in

        except NoSuchElementException:
            pass
  
        #get post comment counts 
        temp_comment_count = post_grid[i].find_element(By.CLASS_NAME, "css-13yklgh").find_elements(By.CLASS_NAME, "_2kP4d1Rw") #return list of comment (if any)
        comment_count.append(len(temp_comment_count))

        post_id = post_grid[i].get_attribute("id") #get the post id 

        #get post user
        post_user = post_grid[i].find_element(By.CLASS_NAME, "E7NPJ3WK").text

        #get post text
        post_text = post_grid[i].find_element(By.CLASS_NAME, "content-body").text #get body text from post[i]
            
        #get post date
        byline = post_grid[i].find_elements(By.CLASS_NAME, "post-byline-redesign") #getting two elements from byline

        neighbourhood = byline[0].text #pass the first element to neighbourhood name

        date = byline[1].text #pass the second element to date 

        eng_date = dutch_to_eng(date) #change dutch date to eng date

        changed_date = changedate(eng_date) #reformat date 
        
        #get reactions, including likes and other emojis
        temp_reaction_count = get_reaction()

        '''''
        Append all extracted information to the lists 
        '''''
        post.append(post_id) 
        text.append(post_text)
        neighbourhood_name.append(neighbourhood)
        post_username.append(post_user)
        reaction_count.append(temp_reaction_count)
        post_date.append(changed_date)
        
    except NoSuchElementException: #handle exception where no element indicated was found
        pass