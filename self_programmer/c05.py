# 1
fav_musician = ["Little Glee Monster","Superfly","Claris","Dreams Come True","Kohmi Hirose","Eiru Aoi"]
print(fav_musician)
print('\n')

# 2
my_place = [
    (35.682850,139.883018),
    (39.066448,141.737926),
    (35.484216,139.645108),
    (34.670856,134.224413)
    ]
print(my_place)
print('\n')

# 3
my_features = {
    "fav_color": "red",
    "fav_artist": "Little Glee Monster",
    "want to be": "programmer of freelance",
    "nationality": "Japanese",
    }
print(my_features)
print('\n')

# 4
print("fav_color","fav_artist","want to be","nationality")
a_feature = input("Input a item in these if you want to know about me!")
if a_feature in my_features:
    print(my_features[a_feature])
    print('\n')
else:
    print("Input accurately, plz.")
    print('\n')

# 5
fav_artist_and_works = {
    "Little Glee Monster": ["Eyes to me","Don't worry be happy","Close to you","Girls be free"],
    "Kohmi Hirose": ["God of Romance","promise","Snow Fall"],
    "Claris": ["border","irony","Diamonds","Cheers"]
    }
print(fav_artist_and_works)
