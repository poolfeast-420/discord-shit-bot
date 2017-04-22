import datetime
from words import eventsaying, eventphoto

specialprofilechecker = True
currentyear = datetime.datetime.now().year
currentmonth = datetime.datetime.now().month
currentday = datetime.datetime.now().day

if (datetime.datetime.now() == datetime.date(currentyear,12,25)):
    evetdetector =  eventsaying['christmas']
    profilepicture = eventphoto['christmas']
elif (datetime.datetime.now() == datetime.date(currentyear,1,26)):
    eventdetector = eventsaying['stryaday']
    profilepicture = eventphoto['stryaday']
elif (datetime.datetime.now() == datetime.date(currentyear,3,20)):
    eventdetector = eventsaying['alienabduction']
    profilepicture = eventphoto['alienabduction']
elif (datetime.datetime.now() == datetime.date(currentyear,5,3)):
    eventdetector = eventsaying['lumpyrug']
    profilepicture = eventphoto['lumpyrug']
elif (datetime.datetime.now() == datetime.date(currentyear,2,22)):
    eventdetector = eventsaying['humble']
    profilepicture = eventphoto['humble']
elif (datetime.datetime.now() == datetime.date(currentyear,4,15)):
    eventdetector = eventsaying['thatsucks']
    profilepicture = eventphoto['thatsucks']
elif (datetime.datetime.now() == datetime.date(currentyear,11,19)):
    eventdetector = eventsaying['haveabadday']
    profilepicture = eventphoto['haveabadday']
elif (datetime.datetime.now() == datetime.date(currentyear,9,11)):
    eventdetector = eventsaying['911']
    profilepicture = eventphoto['911']
elif (datetime.datetime.now() == datetime.date(currentyear,1,8)):
    eventdetector = eventsaying['kimjongun']
    profilepicture = eventphoto['kimjongun']
elif (datetime.datetime.now() == datetime.date(currentyear,5,4)):
    eventdetector = eventsaying['force']
    profilepicture = eventphoto['force']
elif (datetime.datetime.now() == datetime.date(currentyear,3,4)):
    eventdetector = eventsaying['holyexperiment'] 
    profilepicture = eventphoto['holyexperiment']
elif (datetime.datetime.now() == datetime.date(currentyear,2,13)):
    eventdetector = eventsaying['pancakeday']
    profilepicture = eventphoto['pancakeday']
elif (datetime.datetime.now() == datetime.date(currentyear,12,18)):
    eventdetector = eventsaying['stalin']
    profilepicture = eventphoto['stalin']
elif (datetime.datetime.now() == datetime.date(currentyear,4,20)):
    eventdetector = eventsaying['hitler'] 
    profilepicture = eventphoto['hitler']
elif (datetime.datetime.now() == datetime.date(currentyear,1,15)):
    eventdetector = eventsaying['martinluther'] 
    profilepicture = eventphoto['martinluther']
elif (datetime.datetime.now() == datetime.date(currentyear,4,13)):
    eventdetector = eventsaying['hitchens']
    profilepicture = eventphoto['hitchens']
elif (datetime.datetime.now() == datetime.date(currentyear,7,26)):
    eventdetector = eventsaying['kubrick']
    profilepicture = eventphoto['kubrick']
elif (datetime.datetime.now() == datetime.date(currentyear,3,14)):
    eventdetector = eventsaying['einstein'] 
    profilepicture = eventphoto['einstein']
elif (datetime.datetime.now() == datetime.date(currentyear,2,12)):
    eventdetector = eventsaying['darwin'] 
    profilepicture = eventphoto['darwin']
elif (datetime.datetime.now() == datetime.date(currentyear,8,12)):
    eventdetector = eventsaying['Schrödinger'] 
    profilepicture = eventphoto['Schrödinger']
else: 
    eventdetector = eventsaying['default']
    profilepicture = eventphoto['default']
    specialprofilechecker = False 
