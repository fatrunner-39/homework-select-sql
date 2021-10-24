import sqlalchemy


db = 'postgresql://postgres:08320902@localhost:5432/test_database'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# Select 1
# sel = connection.execute(
#     """SELECT genre_name, COUNT(singer_id)
#     FROM genre as g
#     JOIN singergenre as sg
#     ON g.id = sg.genre_id
#     GROUP BY genre_name;"""
# ).fetchall()

# Select 2
# sel = connection.execute(
#     """SELECT COUNT(track_title)
#     FROM track as t
#     JOIN album as a
#     ON t.album_id = a.id
#     WHERE a.year_of_start
#     BETWEEN 2019 AND 2021;"""
# ).fetchall()

# Select 3
# sel = connection.execute(
#     """SELECT title, AVG(duration)
#     FROM album as a
#     JOIN track as t
#     ON a.id = t.album_id
#     GROUP BY a.title;"""
# ).fetchall()

# connection.execute(
#         """INSERT INTO album(title, year_of_start, ratio)
#         VALUES('Minutes to Midnight', 2007, 8.8);"""
#     )

# connection.execute(
#         """INSERT INTO track(track_title, duration , is_like, album_id)
#         VALUES('What Ive Done', 205, True, 12);"""
#     )

# connection.execute(
#     """INSERT INTO singeralbum (singer_id , album_id)
#     VALUES(7, 12);"""
# )

# Select 4
# sel = connection.execute(
#     """SELECT DISTINCT name
#     FROM singer as s
#     JOIN singeralbum as sa
#     ON s.id = sa.singer_id
#     JOIN album as a
#     ON sa.album_id = a.id
#     WHERE name NOT IN(SELECT name
#     FROM singer as s
#     JOIN singeralbum as sa
#     ON s.id = sa.singer_id
#     JOIN album as a
#     ON sa.album_id = a.id
#     WHERE a.year_of_start = 2021);"""
# ).fetchall()

# Select 5
# sel = connection.execute(
#     """SELECT DISTINCT collection_title
#     FROM collection as c
#     JOIN trackcollection as tc
#     ON c.id = tc.collection_id
#     JOIN track as t
#     ON tc.track_id = t.id
#     JOIN album as a
#     ON t.album_id = a.id
#     JOIN singeralbum as sa
#     ON a.id = sa.album_id
#     JOIN singer as s
#     ON sa.singer_id = s.id
#     WHERE name = 'System of a Down';"""
# ).fetchall()

# connection.execute(
#     """INSERT INTO singergenre (singer_id , genre_id)
#     VALUES(7, 5);"""
# )

# # Select 6
# sel = connection.execute(
#     """SELECT DISTINCT title
#     FROM album as a
#     JOIN singeralbum as sa
#     ON a.id = sa.album_id
#     JOIN singer as s
#     ON sa.singer_id = s.id
#     JOIN singergenre as sg
#     ON s.id = sg.singer_id
#     WHERE sg.singer_id in (SELECT singer_id
#     FROM singergenre
#     GROUP BY singer_id
#     HAVING COUNT(genre_id) > 1);"""
# ).fetchall()

# Select 7
# sel = connection.execute(
#     """SELECT track_title FROM track AS t
#     LEFT JOIN trackcollection AS tc
#     ON t.id = tc.track_id
#     WHERE tc.collection_id IS NULL;"""
# ).fetchall()

# Select 8
# sel = connection.execute(
#     """SELECT name
#     FROM singer as s
#     JOIN singeralbum as sa
#     ON s.id = sa.singer_id
#     JOIN album as a
#     ON sa.album_id = a.id
#     JOIN track as t
#     ON a.id = t.album_id
#     WHERE t.id IN(SELECT id
#     FROM track
#     WHERE duration
#     IN (SELECT MIN(duration)
#     FROM track));"""
# ).fetchall()

# Select 9
sel = connection.execute(
    """SELECT DISTINCT title
    FROM album a
    JOIN track t
    ON a.id = t.album_id
    WHERE t.album_id IN
    (SELECT album_id
    FROM track
    GROUP BY album_id
    HAVING COUNT(id) =
    (SELECT COUNT(id)
        FROM track
        GROUP BY album_id
        ORDER BY COUNT(id)
        LIMIT 1));"""
).fetchall()

print(sel)

# SELECT track_title
#     FROM track
#     WHERE duration
#     IN (SELECT MIN(duration)
#     FROM track)