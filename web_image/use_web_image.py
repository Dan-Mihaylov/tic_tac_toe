import urllib.request
import io
from PIL import Image, ImageTk

"""
With this class we convert a web .png image to the logo we display on the main screen, since having it in a 
local path creates problems with other machines and it is easier to change logo if you want to.
"""


class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        resize = Image.Image.resize(image, (50, 50))
        self.image = ImageTk.PhotoImage(resize)

    def get(self):
        return self.image
