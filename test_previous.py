from unittest import mock
from colors_redis import colorsRedis
from previousRedisColor import PreviousColorsRedis
from mockRedis import mock_connect


@mock.patch.object(colorsRedis, 'connect', mock_connect)
@mock.patch.object(PreviousColorsRedis, 'connect', mock_connect)
def test_get_previous_color():
    cdb = colorsRedis()
    prev = PreviousColorsRedis()
    cdb.register_color("Blue", '46', '180', '230')
    previous_color = prev.getPreviousColor()
    assert previous_color == 'Previous color not set yet'


@mock.patch.object(colorsRedis, 'connect', mock_connect)
@mock.patch.object(PreviousColorsRedis, 'connect', mock_connect)
def test_get_previous_color2():
    cdb = colorsRedis()
    prev = PreviousColorsRedis()
    cdb.register_color("Blue",'46', '180', '230')
    prev.updatePreviousColor("Blue")
    cdb.register_color("Red", '237', '10', '63')
    prev.updatePreviousColor("Red")
    previous_color = prev.getPreviousColor()
    assert previous_color == 'Blue'


@mock.patch.object(colorsRedis, 'connect', mock_connect)
@mock.patch.object(colorsRedis, 'connect', mock_connect)
@mock.patch.object(PreviousColorsRedis, 'connect', mock_connect)
def test_previous_color_with_same_color():
    cdb = colorsRedis()
    prev = PreviousColorsRedis()
    cdb.register_color("Blue", '46', '180', '230')
    prev.updatePreviousColor("Blue")
    cdb.register_color("Red",'237', '10', '63')
    prev.updatePreviousColor("Red")
    cdb.register_color("Red",'237', '10', '63')
    prev.updatePreviousColor("Red")
    previous_color = prev.getPreviousColor()
    assert previous_color == 'Blue'


@mock.patch.object(colorsRedis, 'connect', mock_connect)
@mock.patch.object(PreviousColorsRedis, 'connect', mock_connect)
def test_update_with_multiple_previous_colors():
    cdb = colorsRedis()
    prev = PreviousColorsRedis()
    cdb.register_color("Blue", '46', '180', '230')
    prev.updatePreviousColor("Blue")
    cdb.register_color("Red", '237', '10', '63')
    prev.updatePreviousColor("Red")
    cdb.register_color("Green", '58', '166', '85')
    prev.updatePreviousColor("Green")
    previous_color = prev.getPreviousColor()
    assert previous_color == 'Red'
