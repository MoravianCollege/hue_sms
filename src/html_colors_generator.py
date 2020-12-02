import redis


def generate_colors_from_redis():
    r = redis.Redis(
        host='localhost', port=6379, db=0)
    generated_colors = {}
    colors = r.hgetall("colors")
    for name, rgb_value in colors.items():
        generated_colors[name.decode()] = rgb_value.decode()
    return generated_colors
