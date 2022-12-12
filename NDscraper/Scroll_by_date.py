#get oldest date for scrolling
import time

def find_min_date(target_date):
    list_of_byline = driver.find_elements(By.CLASS_NAME, "post-byline-redesign") #find by-line (containing neighbourhood name and date)
    list_of_date = []

    target = datetime.datetime.strptime(target_date,"%d/%m/%Y") #pass target date to target 

    for i in range(1, len(list_of_byline), 2): #for loop with 2 as increment interval (index of odd numbers are dates)
        temp_date = list_of_byline[i].text #pass date to temp_date 

        temp_date = dutch_to_eng(temp_date) #change dutch date to eng date
        temp_date = changedate(temp_date) #change date format

        list_of_date.append(temp_date) #append date to list of dates

    min_date = min(list_of_date) #find oldest date 

    min_date = datetime.datetime.strptime(min_date,"%d/%m/%Y") #pass formatted oldest date to min_date
    days_diff = min_date - target #calculate the date difference between oldest date and target date 

    return days_diff

#scroll by date
def scroll_by_date(target_date): #user input has to be %d/%m/%Y
    days_diff = find_min_date(target_date) #find date difference

    while days_diff.days > 0: #if there is still date difference (i.e., diff >= 0), keep scrolling
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #scroll
        time.sleep(7) #wait 7 seconds for the page to load

        days_diff = find_min_date(target_date) #find again the oldest date in the updated list of dates 