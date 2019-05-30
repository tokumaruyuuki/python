inputSeconds = int(input())

hours = 0
minutes = 0
seconds = 0
if(inputSeconds == 0):
    print("00:00:00")
else:
    hours = int(inputSeconds / 3600)
    inputSeconds -= 3600 * hours
    minutes = int(inputSeconds / 60)
    seconds = inputSeconds - 60 * minutes
    tmphours = str(hours)
    tmpminutes = str(minutes)
    tmpseconds = str(seconds)
    if(len(tmphours) == 1):
        anshours = "0" + tmphours
    else:
        anshours = tmphours
    if(len(tmpminutes) == 1):
        ansminutes = "0" + tmpminutes
    else:
        ansminutes = tmpminutes
    if(len(tmpseconds) == 1):
        ansseconds = "0" + tmpseconds
    else:
        ansseconds = tmpseconds
    print(anshours + ":" + ansminutes + ":" + ansseconds)