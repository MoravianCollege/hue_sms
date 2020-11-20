from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from hue_controller import HueController
from name_converter import clean_name
from data_writer import writeFile,colorPercent,mostRecentColors,numOfEachColor,invalidColors,firstEntryDate
from previousRedisColor import getPreviousColor, updatePreviousColor
import logging

logging.basicConfig(level=logging.INFO,filename="hue_log.log",
                    format="%(asctime)s:%(levelname)s:%(message)s"	)

app = Flask(__name__)
controller = HueController()
file = "data.csv"

@app.route('/', methods=['POST'])
def set_color():
    phone_number = request.values.get('From', None)
    color_name = request.values.get('Body', None)
    color_name = clean_name(color_name)

    if color_name == "black":
        response = MessagingResponse()
        response.message("Haha... please use a color that contains light.")
        return str(response)

    if color_name == "previous":
        prev_color = getPreviousColor()
        response = MessagingResponse()
        response.message("The previous color was {}".format(clean_name(prev_color)))
        return str(response)

    if color_name == "colors":
        colors_link = 'http://localhost:5000/colors'  # the link of the end point for '/colors'
        response = MessagingResponse()
        response.message("{}".format(colors_link))
        return str(response)

    message = controller.set_color(color_name)
    percent = colorPercent(file,color_name)
    date = firstEntryDate(file)
    response = MessagingResponse()
    response.message(message + " This entry has been chosen " + str(percent) + "% of the time since " + date + "!")
    logging.info("Color " + color_name + " has been set by the phone number " + phone_number + ".")
    writeFile(file,str(phone_number), str(color_name), str(message))
    updatePreviousColor(color_name)

    return str(response)
@app.route('/recents',methods=['GET'])
def get_most_recent():
    return mostRecentColors(file)
@app.route('/number',methods=['GET'])
def get_num_of_each():
    return numOfEachColor(file)
@app.route('/invalids',methods=['GET'])
def get_invalids():
    return invalidColors(file)


@app.route('/colors',methods=['GET'])
def get_colors():
    """return a html page that display the colors with their name"""
    return


if __name__ == '__main__':
    app.run()
    logging.info("Server has been stopped")
