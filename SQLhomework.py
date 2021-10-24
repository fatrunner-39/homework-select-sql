import sqlalchemy
from create_tables_like_classes import Singer, Genre, SingerGenre, Album, Track, SingerAlbum, \
    Collection, TrackCollection


System_of_a_Down = Singer("System of a Down")
Wiz_Khalifa = Singer("Wiz Khalifa")
king_and_jester = Singer("Король и шут")
John_Williams = Singer("John Williams")
Imagine_dragons = Singer("Imagine dragons")
Papa_Roach = Singer("Papa Roach")
Linkin_Park = Singer("Linkin Park")
Birdy = Singer("Birdy")
singers = [System_of_a_Down, Wiz_Khalifa, king_and_jester, John_Williams, Imagine_dragons,
           Papa_Roach, Linkin_Park, Birdy]

alternative = Genre("Alternative")
rap = Genre("Rap")
punk = Genre("Punk")
music_from_films = Genre("Music from films")
rock = Genre("Rock")
pop = Genre("Pop")
nu_metal = Genre("nu metal")
genres = [alternative, rap, punk, music_from_films, rock, pop, nu_metal]
# genres = [pop, nu_metal]

el1 = SingerGenre(1, 1)
el2 = SingerGenre(2, 2)
el3 = SingerGenre(3, 3)
el4 = SingerGenre(4, 4)
el5 = SingerGenre(5, 5)
el6 = SingerGenre(6, 5)
el7 = SingerGenre(7, 7)
el8 = SingerGenre(8, 6)
singergenges = [el1, el2, el3, el4, el5, el6, el7, el8]

toxicity = Album("Toxicity", 2001, 9.5)
hypnotize = Album("Hypnotize", 2001, 8.7)
rolling_papers = Album("Rolling papers", 2011, 8.9)
no_gun = Album("Жаль, что нет ружья", 2002, 9.1)
old_fairytale = Album("Как в старой сказке", 2001, 8.8)
starwars = Album("Starwars", 2010, 9.9)
origins = Album("Origins", 2018, 9.7)
mercury = Album("Mercury", 2021, 8.5)
to_be_loved = Album("To Be Loved", 2010, 8.3)
meteora = Album("Meteora", 2021, 8.5)
fire_within = Album("Fire Within", 2013, 9.1)
albums = [toxicity, hypnotize, rolling_papers, no_gun, old_fairytale, starwars, origins, mercury,
          to_be_loved, meteora, fire_within]

tr1 = Track("Chop Suey!", 210, True, 1)
tr2 = Track("Toxicity", 218, True, 1)
tr3 = Track("Lonely Day", 227, False, 2)
tr4 = Track("Black and Yellow", 228, False, 3)
tr5 = Track("Мертвый анархист", 247, True, 4)
tr6 = Track("Проклятый старый дом", 257, True, 5)
tr7 = Track("Duel of Fates", 254, True, 6)
tr8 = Track("The Imperial March", 179, True, 6)
tr9 = Track("Natural", 189, True, 7)
tr10 = Track("Bad Liar", 260, True, 7)
tr11 = Track("My Life", 224, True, 8)
tr12 = Track("Last Resort", 200, False, 9)
tr13 = Track("Numb", 187, True, 10)
tr14 = Track("Faint", 144, True, 10)
tr15 = Track("Strange Birds", 183, True, 11)
tr16 = Track("Wings", 252, True, 11)
tracks = [tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10, tr11, tr12, tr13, tr14, tr15, tr16]

singalb1 = SingerAlbum(1, 1)
singalb2 = SingerAlbum(1, 2)
singalb3 = SingerAlbum(2, 3)
singalb4 = SingerAlbum(3, 4)
singalb5 = SingerAlbum(3, 5)
singalb6 = SingerAlbum(4, 6)
singalb7 = SingerAlbum(5, 7)
singalb8 = SingerAlbum(5, 8)
singalb9 = SingerAlbum(6, 9)
singalb10 = SingerAlbum(7, 10)
singalb11 = SingerAlbum(8, 11)
singalbes = [singalb1, singalb2, singalb3, singalb4, singalb5, singalb6, singalb7, singalb8,
             singalb9, singalb10, singalb11]

col1 =Collection("First", "First collection", 2005)
col2 =Collection("Second", "Second collection", 2005)
col3 =Collection("Third", "Third collection", 2005)
col4 =Collection("Fourth", "Fourth collection", 2005)
col5 =Collection("Fifth", "Fifth collection", 2005)
col6 =Collection("Sixth", "Sixth collection", 2005)
col7 =Collection("Seventh", "Seventh collection", 2005)
col8 =Collection("Eighth", "Eighth collection", 2005)
collections = [col1, col2, col3, col4, col5, col6, col7, col8]

trackcol1 = TrackCollection(1, 1)
trackcol2 = TrackCollection(1, 2)
trackcol3 = TrackCollection(1, 3)
trackcol4 = TrackCollection(1, 5)
trackcol5 = TrackCollection(2, 14)
trackcol6 = TrackCollection(2, 15)
trackcol7 = TrackCollection(2, 1)
trackcol8 = TrackCollection(3, 2)
trackcol9 = TrackCollection(3, 14)
trackcol10 = TrackCollection(3, 7)
trackcol11 = TrackCollection(3, 8)
trackcol12 = TrackCollection(4, 16)
trackcol13 = TrackCollection(4, 14)
trackcol14 = TrackCollection(5, 1)
trackcol15 = TrackCollection(5, 2)
trackcol16 = TrackCollection(6, 4)
trackcol17 = TrackCollection(6, 12)
trackcol18 = TrackCollection(6, 16)
trackcol19 = TrackCollection(7, 1)
trackcol20 = TrackCollection(7, 2)
trackcol21 = TrackCollection(7, 3)
trackcol22 = TrackCollection(8, 5)
trackcol23 = TrackCollection(8, 6)
trackcollections = [trackcol1, trackcol2, trackcol3, trackcol4, trackcol5, trackcol6, trackcol7,
                    trackcol8, trackcol9, trackcol10, trackcol11, trackcol12, trackcol13,
                    trackcol14, trackcol15, trackcol16, trackcol17, trackcol18, trackcol19,
                    trackcol20, trackcol21, trackcol22, trackcol23]

db = 'postgresql://postgres:08320902@localhost:5432/test_database'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# connection.execute(
#     """CREATE TABLE IF NOT EXISTS singer (id serial primary key, name varchar(80) not null unique);
#     CREATE TABLE IF NOT EXISTS genre(
#         id serial primary key,
#         genre_name varchar(50) not null unique);
#     CREATE TABLE IF NOT EXISTS singergenre (
#         id serial primary key,
#         singer_id integer references singer(id),
#         genre_id integer references genre(id));
#     CREATE TABLE IF NOT EXISTS album (
#         id serial primary key,
#         title varchar(50) not null unique,
#         year_of_start integer not null,
#         ratio numeric not null check(ratio > 0));
#     CREATE TABLE IF NOT EXISTS singeralbum (
#         id serial primary key,
#         singer_id integer references singer(id),
#         album_id integer references album(id));
#     CREATE TABLE IF NOT EXISTS track(
#         id serial primary key,
#         track_title varchar(50) not null unique,
#         duration integer not null,
#         is_like boolean not null,
#         album_id integer references album(id)
#         );
#     CREATE TABLE IF NOT EXISTS collection(
#         id serial primary key,
#         collection_title varchar(100) not null unique,
#         description text not null,
#         start_year integer not null);
#     CREATE TABLE IF NOT EXISTS trackcollection (
#         id serial primary key,
#         collection_id integer references collection(id),
#         track_id integer references track(id));"""
#     )

# for singer in singers:
#     connection.execute(
#         f"""INSERT INTO singer(name)
#             VALUES ('{singer.name}');"""
#     )
#
# for genre in genres:
#     connection.execute(
#         f"""INSERT INTO genre(genre_name)
#             VALUES ('{genre.genre_name}');"""
#     )
#
# for singergenre in singergenges:
#     connection.execute(
#         f"""INSERT INTO singergenre(singer_id, genre_id)
#             VALUES ('{singergenre.singer_id}' , '{singergenre.genre_id}');"""
#     )
#
# for album in albums:
#     connection.execute(
#         f"""INSERT INTO album(title, year_of_start, ratio)
#             VALUES ('{album.title}', '{album.year_of_start}', '{album.ratio}');"""
#     )

# for track in tracks:
#     connection.execute(
#         f"""INSERT INTO track(track_title, duration, is_like, album_id)
#             VALUES ('{track.track_title}', '{track.duration}', '{track.is_like}', '{track.album_id}');"""
#     )

# for singalb in singalbes:
#     connection.execute(
#         f"""INSERT INTO singeralbum(singer_id, album_id)
#             VALUES ('{singalb.singer_id}', '{singalb.album_id}');"""
#     )

# for collection in collections:
#     connection.execute(
#         f"""INSERT INTO collection(collection_title, description, start_year)
#             VALUES ('{collection.collection_title}', '{collection.description}', '{collection.start_year}');"""
#     )

# for trackcollection in trackcollections:
#     connection.execute(
#         f"""INSERT INTO trackcollection(collection_id, track_id)
#             VALUES ('{trackcollection.collection_id}', '{trackcollection.track_id}');"""
#     )

# sel = connection.execute(
#     """SELECT title, year_of_start FROM album
#     WHERE year_of_start = '2018';"""
# ).fetchall()

# sel = connection.execute(
#     """SELECT track_title, duration
#     FROM track
#     ORDER BY duration DESC
#     LIMIT 1;"""
# ).fetchall()

# sel = connection.execute(
#     """SELECT track_title
#     FROM track
#     WHERE duration >= '210';"""
# ).fetchall()

# sel = connection.execute(
#     """SELECT collection_title
#     FROM collection
#     WHERE start_year
#     BETWEEN 2018 AND 2021;"""
# ).fetchall()

# sel = connection.execute(
#     """SELECT name
#     FROM singer
#     WHERE (LENGTH(name) - LENGTH(replace(name, ' ', '')) + 1) = 1;"""
# ).fetchall()

sel = connection.execute(
    """SELECT track_title
    FROM track
    WHERE track_title
    LIKE '%%my%%'
    OR track_title
    LIKE '%%My%%';"""
).fetchall()

print(sel)
