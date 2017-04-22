from datetime import datetime,date
from words import eventsaying, eventphoto

specialprofilechecker = True
currentyear = datetime.now().year()
if (datetime.date() == datetime.date(currentyear,25,12)):
    evetdetector =  eventsaying['christmas']
    profilepicture = eventphoto['christmas']
elif (datetime.date() == datetime.date(currentyear,26,1)):
    eventdetector = eventsaying['stryaday']
    profilepicture = eventphoto['stryaday']
elif (datetime.date() == datetime.date(currentyear,20,3)):
    eventdetector = eventsaying['alienabduction']
    profilepicture = eventphoto['alienabduction']
elif (datetime.date() == datetime.date(currentyear,3,5)):
    eventdetector = eventsaying['lumpyrug']
    profilepicture = eventphoto['lumpyrug']
elif (datetime.date() == datetime.date(currentyear,22,2)):
    eventdetector = eventsaying['humble']
    profilepicture = eventphoto['humble']
elif (datetime.date() == datetime.date(currentyear,15,4)):
    eventdetector = eventsaying['thatsucks']
    profilepicture = eventphoto['thatsucks']
elif (datetime.date() == datetime.date(currentyear,19,11)):
    eventdetector = eventsaying['haveabadday']
    profilepicture = eventphoto['haveabadday']
elif (datetime.date() == datetime.date(currentyear,11,9)):
    eventdetector = eventsaying['911']
    profilepicture = eventphoto['911']
elif (datetime.date() == datetime.date(currentyear,8,1)):
    eventdetector = eventsaying['kimjongun']
    profilepicture = eventphoto['kimjongun']
elif (datetime.date() == datetime.date(currentyear,4,5)):
    eventdetector = eventsaying['force']
    profilepicture = eventphoto['force']
elif (datetime.date() == datetime.date(currentyear,4,3)):
    eventdetector = eventsaying['holyexperiment'] 
    profilepicture = eventphoto['holyexperiment']
elif (datetime.date() == datetime.date(currentyear,13,2)):
    eventdetector = eventsaying['pancakeday']
    profilepicture = eventphoto['pancakeday']
elif (datetime.date() == datetime.date(currentyear,18,12)):
    eventdetector = eventsaying['stalin']
    profilepicture = eventphoto['stalin']
elif (datetime.date() == datetime.date(currentyear,20,4)):
    eventdetector = eventsaying['hitler'] 
    profilepicture = eventphoto['hitler']
elif (datetime.date() == datetime.date(currentyear,15,1)):
    eventdetector = eventsaying['martinluther'] 
    profilepicture = eventphoto['martinluther']
elif (datetime.date() == datetime.date(currentyear,13,4)):
    eventdetector = eventsaying['hitchens']
    profilepicture = eventphoto['hitchens']
elif (datetime.date() == datetime.date(currentyear,26,7)):
    eventdetector = eventsaying['kubrick']
    profilepicture = eventphoto['kubrick']
elif (datetime.date() == datetime.date(currentyear,14,3)):
    eventdetector = eventsaying['einstein'] 
    profilepicture = eventphoto['einstein']
elif (datetime.date() == datetime.date(currentyear,12,2)):
    eventdetector = eventsaying['darwin'] 
    profilepicture = eventphoto['darwin']
elif (datetime.date() == datetime.date(currentyear,12,2)):
    eventdetector = eventsaying['Schrödinger'] 
    profilepicture = eventphoto['Schrödinger']
else: 
    eventdetector = eventsaying['default']
    profilepicture = eventphoto['default']
    specialprofilechecker = False 
