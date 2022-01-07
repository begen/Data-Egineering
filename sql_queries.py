# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS music_library(
    songplay_id int PRIMARY KEY, 
    start_time DATETIME NOT NULL, 
    user_id int, level text, 
    song_id int, artist_id int, 
    session_id int, 
    location varchar, user_agent text[]
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
        user_id int PRIMARY KEY, 
        first_name varchar, 
        last_name varchar, 
        gender text, 
        level varchar);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id text PRIMARY KEY, 
    title text NOT NULL,
    artist_id text NOT NULL REFERENCES artists(artist_id),
    year int,
    duration foalt NOT NULL
);


""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artistis(
    artists_id text PRIMARY KEY,
    name text NOT NULL,
    location text,
    latitude float,
    longitude float);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time date PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday text);
""")

# INSERT RECORDS

songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent


songplay_table_insert = ("""


""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]