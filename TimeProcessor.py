# stringIsInt
# check if the input string can be parsed into an integer
# if so, return that integer
# else return false
# @param: strin, the input string to be checked

def stringIsInt(strin):
    if type(strin) is not str:
        raise(InputIsNotStringError())
    try:
        intout = int(strin)
        return intout
    except ValueError:
        return False


# given a correctly formatted time, return a list with the begin time and (if applicable) end time
# the input has the following format: 11:00am, 1:00pm, or 11:00am-1:00pm
# if there's no dash, the time is begin time, and we assume this event is one hour long
# @param: strin, the input string to be parsed
# the input time is 12-hour, and the output will be converted to 24-hour
def process(strin):
    if strin.find('-') == -1:
        pm = False
        begin = strin.split(':') # begin = [hr, min]
        if begin[1].find('p') != -1:
            pm = True
        begin[1] = begin[1][0:2] # truncate am/pm
        begin[0] = stringIsInt(begin[0])
        if pm:
            begin[0] += 12
        begin[1] = stringIsInt(begin[1])
        end = []
        end.append(begin[0] + 1)
        end.append(begin[1])
    else:
        beginpm = False
        endpm = False
        strin = strin.split('-')
        begin = strin[0]
        end = strin[1]
        if begin.find('p') != -1:
            beginpm = True
        if end.find('p') != -1:
            endpm = True
        begin = begin.split(':')
        end = end.split(':')
        begin[1] = begin[1][0:2]
        begin[1] = stringIsInt(begin[1])
        begin[0] = stringIsInt(begin[0])
        if beginpm:
            begin[0] += 12
        end[1] = end[1][0:2]
        end[1] = stringIsInt(end[1])
        end[0] = stringIsInt(end[0])
        if endpm:
            end[0] += 12
    result = []
    if begin[0] == 24:
        begin[0] = 0
    if end[0] == 24:
        end[0] = 0
    result.append(begin[0])
    result.append(begin[1])
    result.append(end[0])
    result.append(end[1])
    return result
