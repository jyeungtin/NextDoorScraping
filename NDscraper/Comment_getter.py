def find_post_comments():
    comment = []
    comment_author = []
    comment_post_id = []
    comment_IDs = []
    comment_neighbourhoods = []

    for i in range(len(post_grid)):
        try:
            print(f"Current post: {i}") #Tell us which post the script is processing :)

            post_id = post_grid[i].get_attribute("id") #get post id

            temp_comment_count = post_grid[i].find_element(By.CLASS_NAME, "css-13yklgh").find_elements(By.CLASS_NAME, "_2kP4d1Rw") #return list of comment (if any)
            temp_comment_count = len(temp_comment_count) #return num of comment (if any)
            
            if temp_comment_count != 0:
                for comment_num in range(temp_comment_count):
                    try:
                        ctext_buttons = post_grid[i].find_elements(By.LINK_TEXT, "Meer bekijken") #find expand comment text button

                        for button in ctext_buttons:
                            driver.execute_script("arguments[0].click();", button) #use javascript to click the button

                        time.sleep(1) #wait one second for comments to load in
                    except NoSuchElementException:
                        print("nsee")
                        pass

                    comment_ID = post_grid[i].find_elements(By.CLASS_NAME, "js-media-comment")[comment_num].get_attribute("id") #get comment ID of a certain comment

                    comment_text = post_grid[i].find_elements(By.CLASS_NAME, "js-media-comment")[comment_num].find_element(By.CLASS_NAME, "Linkify").text #get comment main text

                    comment_user = post_grid[i].find_elements(By.CLASS_NAME, "js-media-comment")[comment_num].find_element(By.CLASS_NAME, "comment-detail-author-name").text #get comment's username

                    comment_neighbourhood = post_grid[i].find_elements(By.CLASS_NAME, "js-media-comment")[comment_num].find_element(By.CLASS_NAME, "css-19hrmqv").text #get comment's author's located neighbourhood

                    '''''
                    Append all extracted information to the lists 
                    '''''

                    comment.append(comment_text)
                    comment_post_id.append(post_id)
                    comment_author.append(comment_user)
                    comment_IDs.append(comment_ID)
                    comment_neighbourhoods.append(comment_neighbourhood)
                    
        except NoSuchElementException:  #handle exception where no element indicated was found
            pass
        except IndexError:  #handle index error 
            pass
    return comment, comment_post_id, comment_author, comment_IDs, comment_neighbourhoods