import redis


def setCurrentColor(current_color):
    r = redis.Redis(
        host='localhost', port=6379, db=0)
    r.set("current", current_color)


def getCurrentColor(*kwargs):
    r = redis.Redis(
        host='localhost', port=6379, db=0)
    value = r.get("current")
    if not value:
        r.set("current", *kwargs)
        value = r.get("current")
        return value.decode()
    return value.decode()


def setPreviousColor(prev_color):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set("previous", prev_color)


def getPreviousColor():
    r = redis.Redis(
        host='localhost', port=6379, db=0)
    value = r.get("previous")
    if not value:
        return "not set yet.. or something like that"
    return value.decode()


def updatePreviousColor(current_color):
    previous_value = getCurrentColor(current_color)
    if current_color == previous_value:
        # return "the same as the current color"
        pass
    else:
        setCurrentColor(current_color)
        setPreviousColor(previous_value)

