def generate_wallpaper(color):
    response = openai.Image.create(
        prompt=f"Create a creative wallpaper with the color {color}",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url
