import os
from datetime import datetime

'''The approach here using 'if' is very basic, can be exhausting if chat capability is decided to be added. 
It is very much recommended to use this method to just have multiple one word features/functions where the bot only recieves one user text and the endpoint is very clear in that word, hence we know what definitely needs to be returned'''

def sample_res(text):
    user_mes = str(text).lower()
    
    ## The message by the user should exactly match one of the three,("hello","hi","hey") here, for the bot to actually return something that is intended
    if user_mes in ("hello","hi","hey"):
        return "Hey there!"
    
    if user_mes in ("what do you do?","what do you do","who are you?","who are you"):
        return "A certain text that can be versatile for all the above questions asked"
    
    if user_mes in ("time", "tell me the time", "date"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        
        return str(date_time)
        
    return "The default message that is returned in case no 'if' is triggered"