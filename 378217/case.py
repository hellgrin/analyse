#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
df.info()
df['Revenue (Millions)'].fillna(-1, inplace=True)
df['Metascore'].fillna(-1, inplace=True)
johanson_films = 0
johanson_rating = 0
patison_films = 0
patison_rating = 0
holland_films = 0
holland_rating = 0
timberlake_films = 0
timberlake_rating = 0
washington_rating = 0
washington_films = 0
def split_actors(actors):
    return actors.split(', ')
def vin_count(row):
    global johanson_films , johanson_rating, patison_films, patison_rating, holland_films, holland_rating, timberlake_films, timberlake_rating, washington_films, washington_rating
    if 'Scarlett Johansson' in row['Actors']:
        johanson_films += 1
        johanson_rating += row['Rating']
    elif 'Robert Pattinson' in row['Actors']:
        patison_films += 1
        patison_rating += row['Rating']
    elif 'Tom Holland' in row['Actors']:
        holland_films += 1
        holland_rating += row['Rating']
    elif 'Justin Timberlake' in row['Actors']:
        timberlake_films += 1
        timberlake_rating += row['Rating']
    elif 'Denzel Washington' in row['Actors']:
        washington_films += 1
        washington_rating += row['Rating']
df['Actors'] = df['Actors'].apply(split_actors)
print(df["Actors"])
df.apply(vin_count, axis = 1)
actors_ratings = dict()
actors_ratings['Justin Timberlake'] = [round(timberlake_rating/timberlake_films, 2), timberlake_films]
actors_ratings['Denzel Washington'] = [round(washington_rating/washington_films, 2), washington_films]
actors_ratings['Scarlett Johansson'] = [round(johanson_rating/johanson_films, 2), johanson_films]
actors_ratings['Tom Holland'] = [round(holland_rating/holland_films, 2), holland_films]
actors_ratings['Robert Pattinson'] = [round(patison_rating/patison_films, 2), patison_films]


actors_rating = []
for actors in actors_ratings:
    actors_rating.append(actors_ratings[actors][0])
print(actors_rating)
print(actors_ratings)
s = pd.Series(index = actors_ratings.keys(), data = actors_rating)
s.plot(kind = 'barh', figsize = (15, 8))
plt.show()




comedy_rating = 0
comedy_films = 0
drama_rating = 0
drama_films = 0
fantasy_rating = 0
fantasy_films = 0
scifi_rating = 0
scifi_films = 0
horror_films = 0
horror_rating = 0
def split_genres(genres):
    return genres.split(',')
def genres_count(row):
    global comedy_films, comedy_rating, drama_films, drama_rating, fantasy_films, fantasy_rating, scifi_films, scifi_rating, horror_films, horror_rating
    if 'Comedy' in row['Genre']:
        comedy_films += 1
        comedy_rating += row['Rating']
    elif 'Drama' in row['Genre']:
        drama_films += 1
        drama_rating += row['Rating']
    elif 'Fantasy' in row['Genre']:
        fantasy_films += 1
        fantasy_rating += row['Rating']
    elif 'Sci-Fi' in row['Genre']:
        scifi_films += 1
        scifi_rating += row['Rating']
    elif 'Horror' in row['Genre']:
        horror_films += 1
        horror_rating += row['Rating']
df['Genre'] = df['Genre'].apply(split_genres)
print(df["Genre"])
df.apply(genres_count, axis = 1)



genres_ratings = dict()
genres_ratings['Comedy'] = [round(comedy_rating/comedy_films, 2), comedy_films]
genres_ratings['Drama'] = [round(drama_rating/drama_films, 2), drama_films]
genres_ratings['Fantasy'] = [round(fantasy_rating/fantasy_films, 2), fantasy_films]
genres_ratings['Sci-Fi'] = [round(scifi_rating/scifi_films, 2), scifi_films]
genres_ratings['Horror'] = [round(horror_rating/horror_films, 2), horror_films]


genres_rating = []
for genres in genres_ratings:
    genres_rating.append(genres_ratings[genres][0])
print(genres_rating)
print(genres_ratings)
s2 = pd.Series(index = genres_ratings.keys(), data = genres_rating)
s2.plot(kind = 'barh', figsize = (15, 8))
plt.show()


i = 0
i120 = 0
i_rating = 0
i120_rating = 0
def runtime_count(row):
    global i, i120, i120_rating, i_rating
    if int(row['Runtime (Minutes)']) <= 120:
        i120 += 1
        i120_rating += row['Rating']
    else:
        i += 1
        i_rating += row['Rating']
df.apply(runtime_count, axis = 1)
ratings = dict()
ratings['Runtime<=120'] = [round(i120_rating/i120, 2), i120]
ratings['Runtime>120'] = [round(i_rating/i, 2), i]
runtime_rating = []
for runtime in ratings:
    runtime_rating.append(ratings[runtime][0])
print(runtime_rating)
print(ratings)
s2 = pd.Series(index = ratings.keys(), data = runtime_rating)
s2.plot(kind = 'barh', figsize = (15, 8))
plt.show()

