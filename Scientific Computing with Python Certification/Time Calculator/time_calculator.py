def add_time(start, duration, day = ""):

  result = list()

  #get am-pm in proper format
  ampm = start.split(":")[1].split()[1]

  #get numerical values of the time
  result.append(start.split(":")[0])
  result.append(start.split(":")[1].split()[0])

  result = result + duration.split(":")

  minute = int(result[1]) + int(result[3])

  carryhour = minute // 60

  minute = minute % 60

  hour = int(result[0]) + int(result[2]) + carryhour

  #for am-pm computation
  carryday = int (hour / 12) 

  daysafter = int (hour / 24)

  hour = hour % 12
  #in order to show 00.01 as 12.01 am 
  if hour == 0:
    hour = 12 
  

  change = carryday % 2 == 1

  if change:
    if ampm == "PM":
      ampm = "AM"
      daysafter = int((carryday + 1) / 2) 
    else:
      ampm = "PM"
      daysafter = int(carryday / 2) 

  hour = str(hour)
  minute = str(minute)

  if len(minute) == 1:
    minute = "0" + minute

  whichday = ""
  dayindex = -1

  daylist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  if day != "":
    for i in range(7):
      if day.upper() == daylist[i].upper():
        dayindex = i
        break

  if dayindex != -1:
    whichday = daylist[(dayindex + daysafter) % 7]


  result = str(hour) + ":" + str(minute)  + " " + ampm 
  
  if whichday != "":
    result = result + ", " + whichday

  if daysafter == 1:
    result = result + " (next day)"

  if daysafter > 1:
    result = result + " (" + str(daysafter) + " days later)"
  
  print(result)
  
  return result 