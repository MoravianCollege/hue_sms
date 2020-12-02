# hue_sms (Version 2)
Control a Philips Hue light via SMS

Developers, please see `docs/developers.MD` for cloning, setup, how to run the program, and development instructions and guidelines.

## Version 1
   This program sets up a uses the Twilio SMS service, in connection with a Flask server to allow a SMS message to be converted into usable XY int values. 
   The program takes a String (color) as input, and compares the value with the colors.html file in order to get the appropriate RGB values, to then be converted into the correct XY values.
 
## Version 2: Additional Features  
   This project adds additional features that can be used so the user can gain more information about the previously chosen color as well as which colors can be texted to the hue light.
   This program can now take additional Strings as input, such as "previous" or "colors".
   By the use of requests in demoVersion2.py, it allows us to interact with the 'hue_flask.py' server.
   1. When the client types "previous", the Twilio SMS service as well as its connection to the Flask server interacts with the Redis database to respond with the previously chosen color
   2. When the client types "colors", an html link is returned that includes all the possible colors and their respective names that can be chosen for the hue light.

## Future Potential Additions
   Future potential additions include an increased number of color options, an additional method and timer which would alternate the light between two colors, and a mobile app which would provide information on the light and allow for control of the light via the app.