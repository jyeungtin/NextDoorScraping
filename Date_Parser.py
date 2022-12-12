#Format weird date to normal date
import re 
def format_weird_date(weird_date):
    today = datetime.datetime.today()

    days_from_now = int(re.sub(r"[A-Za-z]","",weird_date).strip()) #replace all letters with spaces and trim trailing whitespace
    
    pretty_date = today - datetime.timedelta(days_from_now) #find date with day difference from Nextdoor format (x dag geleden)
    
    pretty_date = datetime.datetime.strftime(pretty_date,"%d/%m/%Y") #format dates into dmY format 

    return pretty_date


#change Dutch spelling into english
import datetime

def replace_multiple(text, replace):
    for org, subs in replace.items(): 
        text = text.replace(org, subs) 
    return text

def dutch_to_eng(date):
    global eng_date

    replace_words = {'mrt':'mar','mei':'may','okt':'oct'} #dict for replacement 

    if bool(re.match(r".*geleden$", date)) == False: #simply replace words if the format is regular
        eng_date = replace_multiple(date,replace_words)
    else:
        eng_date = format_weird_date(date) #use format_weird_date function if the format is unstandard
    
    return eng_date

#parse date and time of post 
def changedate(date):
    try:
        changed_date = datetime.datetime.strptime(date, '%d %b.').strftime('%d/%m/2022') #format date 

        return changed_date

    except ValueError:
        return date
    except TypeError:
        pass