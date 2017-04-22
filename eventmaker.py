import datetime
from words import eventsaying, eventphoto

specialprofilechecker = True
if (datetime.date() == datetime.date(datetime.datetime.now().year,25,12)):
    evetdetector =  eventsaying['christmas']
    profilepicture = eventphoto['christmas']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,26,1)):
    eventdetector = eventsaying['stryaday']
    profilepicture = eventphoto['stryaday']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,20,3)):
    eventdetector = eventsaying['alienabduction']
    profilepicture = eventphoto['alienabduction']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,3,5)):
    eventdetector = eventsaying['lumpyrug']
    profilepicture = eventphoto['lumpyrug']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,22,2)):
    eventdetector = eventsaying['humble']
    profilepicture = eventphoto['humble']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,15,4)):
    eventdetector = eventsaying['thatsucks']
    profilepicture = eventphoto['thatsucks']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,19,11)):
    eventdetector = eventsaying['haveabadday']
    profilepicture = eventphoto['haveabadday']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,11,9)):
    eventdetector = eventsaying['911']
    profilepicture = eventphoto['911']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,8,1)):
    eventdetector = eventsaying['kimjongun']
    profilepicture = eventphoto['kimjongun']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,4,5)):
    eventdetector = eventsaying['force']
    profilepicture = eventphoto['force']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,4,3)):
    eventdetector = eventsaying['holyexperiment'] 
    profilepicture = eventphoto['holyexperiment']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,13,2)):
    eventdetector = eventsaying['pancakeday']
    profilepicture = eventphoto['pancakeday']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,18,12)):
    eventdetector = eventsaying['stalin']
    profilepicture = eventphoto['stalin']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,20,4)):
    eventdetector = eventsaying['hitler'] 
    profilepicture = eventphoto['hitler']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,15,1)):
    eventdetector = eventsaying['martinluther'] 
    profilepicture = eventphoto['martinluther']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,13,4)):
    eventdetector = eventsaying['hitchens']
    profilepicture = eventphoto['hitchens']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,26,7)):
    eventdetector = eventsaying['kubrick']
    profilepicture = eventphoto['kubrick']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,14,3)):
    eventdetector = eventsaying['einstein'] 
    profilepicture = eventphoto['einstein']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,12,2)):
    eventdetector = eventsaying['darwin'] 
    profilepicture = eventphoto['darwin']
elif (datetime.date() == datetime.date(datetime.datetime.now().year,12,2)):
    eventdetector = eventsaying['Schrödinger'] 
    profilepicture = eventphoto['Schrödinger']
else: 
    eventdetector = eventsaying['default']
    profilepicture = eventphoto['default']
    specialprofilechecker = False 
