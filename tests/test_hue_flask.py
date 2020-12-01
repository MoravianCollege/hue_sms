from src.hue_flask import app as hue_app
from unittest import mock


@mock.patch('hue_flask.PreviousColorsRedis.getPreviousColor')
def test_app_post_previous(mock_previous_color):
    mock_previous_color.return_value = 'red'
    app = hue_app
    app.config['TESTING'] = True
    client = app.test_client()

    phone_number = '5400000000'
    pphac_hue_light_number = '4848951386'
    message = 'previous'
    params = '?From={}&To={}&Body={}'.format(phone_number,pphac_hue_light_number,message)
    response = client.post('/{}'.format(params))

    assert response.status_code == 200

    expected = b'The previous color was red'
    assert expected in response.data


def test_app_post_colors():
    app = hue_app
    app.config['TESTING'] = True
    client = app.test_client()

    phone_number = '5400000000'
    pphac_hue_light_number = '4848951386'
    message = 'colors'
    params = '?From={}&To={}&Body={}'.format(phone_number,pphac_hue_light_number,message)
    response = client.post('/{}'.format(params))

    assert response.status_code == 200

    expected = b'>http://localhost:5000/colors'
    assert expected in response.data
