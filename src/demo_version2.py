import requests
from bs4 import BeautifulSoup


def text_the_server():
    """
    Text the server with a <color> to change the light's color, or 'previous' to get the previous color.
    And can also text 'colors' to get a webpage link that contains the list of all colors.
    """
    phone_number = '5400000000'
    pphac_hue_light_number = '4848951386'
    input_message = input(" ")
    params = {'From':phone_number,'To':pphac_hue_light_number, 'Body': input_message}
    response = requests.post('http://localhost:5000/', params=params)
    response.raise_for_status()
    message = response.text
    soup = BeautifulSoup(message, 'html.parser')
    print(soup.text)


if __name__ == '__main__':
    text_the_server()

