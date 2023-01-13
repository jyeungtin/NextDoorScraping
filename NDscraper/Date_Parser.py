import re 

#Format weird date to normal date
def format_weird_date(weird_date):

    today = datetime.datetime.today() #set today

    #check if uur / minuten included
    uur_minute_check = ['minuten','uur'] #to list 

    if any(word in weird_date for word in uur_minute_check) == True: #check whether uur / minute is included
        pretty_date = today.strftime("%d/%m/%Y") # pass today date to pretty_date if uur/ minute is returned 
    else:
        days_from_now = int(re.sub(r"[A-Za-z]","",weird_date).strip()) #replace all letters with spaces and trim trailing whitespace
        
        pretty_date = today - datetime.timedelta(days_from_now) #find date with day difference from Nextdoor format (x dag geleden)
        
        pretty_date = datetime.datetime.strftime(pretty_date,"%d/%m/%Y") #format dates into dmY format 

    return pretty_date

#change Dutch spelling into english
import datetime

def replace_multiple(text, replace): #function to perform multi-value replacement
    for org, subs in replace.items(): #for loop to replace original item by substitutes
        text = text.replace(org, subs) #pass replaced version of text to text
    return text #return text

def dutch_to_eng(date):
    global eng_date

    replace_words = {'mrt':'mar','mei':'may.','okt':'oct', ' bewerkt':''} #dict for replacement (ONLY DUTCH NOW)

    if bool(re.match(r".*geleden", date)) == False: #simply replace words if the format is regular
        eng_date = replace_multiple(date,replace_words)
    else:
        eng_date = format_weird_date(date) #use format_weird_date function if the format is unstandard
    
    return eng_date

#Check if date retrieved is the same year
def same_year_check(date):
    year_now = datetime.datetime.today().strftime("%Y") #get year now
    year_now = datetime.datetime.strptime(year_now, "%Y")
    
    today = datetime.datetime.today() #pass today date to var. today 
    
    diff_date = today - date
    diff_date = diff_date.days 

    return diff_date

#parse date and time of post 
def changedate(date):
    year_now = datetime.datetime.today().strftime("%Y") #get year now (str)
    year_now_dtob = datetime.datetime.strptime(year_now, "%Y") #get year now (datetime object)

    try:
        changed_date = datetime.datetime.strptime(date, '%d %b.').strftime(f'%d/%m/{year_now}') #format date 

        changed_date_dtob = datetime.datetime.strptime(changed_date, "%d/%m/%Y") #make datetime object for format date

        if same_year_check(changed_date_dtob) > 0:
            return changed_date
        else:
            last_year = year_now_dtob - relativedelta(years=1) #get last year 
            last_year = datetime.datetime.strftime(last_year, "%Y") #format last_year into %Y format

            changed_date = datetime.datetime.strptime(changed_date, "%d/%m/%Y").strftime(f'%d/%m/{last_year}') #format date 
            return changed_date

    except ValueError:
        try:
            changed_date = datetime.datetime.strptime(date, '%d %b. %y').strftime('%d/%m/%Y') #alternative date formatting if parsed datatime is not %d/%m/%Y
            return changed_date
        except ValueError:
            return date #return date if the date is already formatted on NextDoor
    except TypeError:
        pass