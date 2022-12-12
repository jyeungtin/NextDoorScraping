#get links from result lists
from bs4 import element
from pandas import DataFrame
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

post_grid = driver.find_elements(By.CLASS_NAME, "css-15wtqd7") #pass list of individual posts to post_grid

post = []
text = []
comment_count = []
post_date = []
reaction_count = []


for i in range(len(post_grid)):
    try:
        while i == 0: #click on all "more comments" button for the first iteration
            post_grid[i].find_element(By.CLASS_NAME, "css-adjc8x").click() #class css-adjc8x is the class name for more comments

        post_id = post_grid[i].get_attribute("id") #get the post id 

        #get post text
        post_text = post_grid[i].find_element(By.CLASS_NAME, "content-body").text #get body text from post[i]

        #get post comment counts 
        comment = post_grid[i].find_element(By.CLASS_NAME, "comment-container").find_elements(By.CLASS_NAME, "Linkify") #return list of comment (if any)

        temp_comment_count = len(comment)
            
        #get post date
        byline = post_grid[i].find_elements(By.CLASS_NAME, "post-byline-redesign") #getting two elements from byline

        date = byline[1].text #pass the second element to date 

        eng_date = dutch_to_eng(date) #change dutch date to eng date

        changed_date = changedate(eng_date) #reformat date 
        
        #get reactions, including likes and other emojis
        temp_reaction_count = get_reaction()

        post.append(post_id) 
        text.append(post_text)
        comment_count.append(temp_comment_count)
        reaction_count.append(temp_reaction_count)
        post_date.append(changed_date)

        print(f"Processed post: {i}")
        

    except NoSuchElementException:
        pass


#Create data frame
all_post = pd.DataFrame(columns=['ID','Text','Comment Count'])

all_post['ID'] = post
all_post['Text'] = text
all_post['Comment Count'] = comment_count
all_post['Date'] = post_date
all_post['Reaction Count'] = reaction_count

all_post.head(20)

#Specific function for actual comment as it requires a set of different data structure 

comment = []
comment_post_id = []

for i in range(len(post_grid)):
    try:
        post_id = post_grid[i].get_attribute("id") #get post id

        temp_comment_count = post_grid[i].find_element(By.CLASS_NAME, "comment-container").find_elements(By.CLASS_NAME, "Linkify") #return list of comment (if any)
        
        if temp_comment_count != 0:
            for comment_num in range(len(temp_comment_count)):
                comment_text = post_grid[i].find_element(By.CLASS_NAME, "comment-container").find_elements(By.CLASS_NAME, "Linkify")[comment_num].text

                comment.append(comment_text)
                comment_post_id.append(post_id)
    except NoSuchElementException:
        pass


#Create comment texts dataframe
detailed_comment = pd.DataFrame(columns=["ID","Comment"])

detailed_comment['ID'] = comment_post_id
detailed_comment['Comment'] = comment

#Merge dataframe
all_post = all_post.merge(detailed_comment, on = "ID", how = "left")

all_post.head(20)