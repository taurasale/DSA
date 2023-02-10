import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_path = pathlib.Path(r'C:\Users\taura\Desktop\pythonProject1\Tennis-Major-Tournaments-Match-Statistics\AusOpen-men-2013.csv')
df = pd.read_csv(data_path)

class Bottle:
    def __init__(self, volume, type_, soda):
        self.volume = volume
        self.type_ = type_
    def pour (self):
        print("Pouring..")

tauras = Bottle(5,10,20)

print(tauras.self)
import media
class Movie():
    def __init__(self, title, storyline,poster_image_url, trailer_yt_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_yt_url = trailer_yt_url

toy_story = Movie("Toy Story",
                        " A story of a boy",
                        "Wiki",
                        "yt nuroda")
print (toy_story.storyline)
import datetime
class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    def age(self):
        today = datetime.date(2023,1,14)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy,mm,dd) #Date of birthday
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User("tauras aleksa", "19960114")

print(user.age())



