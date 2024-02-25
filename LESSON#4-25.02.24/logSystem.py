import datetime

def logger(msg, level=None, timestamp=None, event=None):

    def _parse_event(event):
        if event is None:
            return ""
        event = "event: "+str(event)
        return event
    
    def _parse_level(level):
        if level is None:
            return ""
        level= "level: "+level
        return level
    
    def _parse_timestamp(timestamp):
        if timestamp is None:
            return ""
        timestamp = "timestamp: "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return timestamp
    
    log_message = []
    log_message.append(msg)
    log_message.append(_parse_level(level))
    log_message.append(_parse_timestamp(timestamp))
    log_message.append(_parse_event(event))
    return log_message

def logManager(withTime=False,shortMessage=False,startRange=None,endRange=None):

    def _withTime(loglst):
        logged=[]
        for log in loglst:
            if log[2].count("timestamp")>0:
                logged.append(log)
        return logged
    def _shortMessage(loglst):
        logged=[]
        for log in loglst:
            if len(log[0])<10:
                logged.append(log)
        return logged
    def _Range(loglst,startRange,endRange):
        logged=[]
        for log in loglst:
            if log[2]!=None:
                startTimestamp=datetime.strptime(startRange,"%Y-%m-%d %H:%M:%S")
                endTimestamp=datetime.strptime(endRange,"%Y-%m-%d %H:%M:%S")
                logTimestamp=datetime.strptime(log[2],"%Y-%m-%d %H:%M:%S")
                if logTimestamp>=startTimestamp and logTimestamp<=endTimestamp:
                    logged.append(log)
        return logged
    if withTime:
        return _withTime
    if shortMessage:
        return _shortMessage
    if startRange!=None and endRange!=None:
        return _Range
    return None
    


# Example usage
# Output: ['This is a message', 'level: INFO', 'timestamp: 2022-02-24 12:00:00', 'event: Some event']

log1 = logger("This is a message", "INFO", None, "Some event1")
log2 = logger("This is another message", "DEBUG", None, "Some event2")
log3 = logger("This is a mfeessage", "ERROR", None, "Some event3")
log4 = logger("This is ancasother message", "DEBUG", None, "Some event4")
log5 = logger("This is a mesxasssage", "INFO", None, "Some event5")
log6 = logger("This is anothear message", "DEBUG", True, "Some event6")
log7 = logger("This is a messsage", "ERROR", True, "Some event7")

loglst=[log1,log2,log3,log4,log5,log6,log7]
for log in logManager(withTime=True)(loglst):
    print(log)
