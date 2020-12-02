from redis import Redis


class PreviousColorsRedis:

    def __init__(self):
        self.connect()

    def connect(self):
        self.db = Redis('localhost', 6379)

    def setCurrentColor(self, current_color):
        r = self.db
        r.set("current", current_color)


    def getCurrentColor(self, *kwargs):
        r = self.db
        value = r.get("current")
        if not value:
            r.set("current", *kwargs)
            value = r.get("current")
            return value.decode()
        return value.decode()

    def setPreviousColor(self, prev_color):
        r = self.db
        r.set("previous", prev_color)

    def getPreviousColor(self):
        r = self.db
        value = r.get("previous")
        if not value:
            return "Previous color not set yet"
        return value.decode()

    def updatePreviousColor(self, current_color):
        previous_value = self.getCurrentColor(current_color)
        if current_color == previous_value:
            pass
        else:
            self.setCurrentColor(current_color)
            self.setPreviousColor(previous_value)

