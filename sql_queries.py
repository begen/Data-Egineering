

# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time BIGINT,
    user_id VARCHAR,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id VARCHAR,
    location VARCHAR,
    user_agent VARCHAR
);
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (
        user_id VARCHAR PRIMARY KEY,
        first_name varchar NOT NULL,
        last_name varchar,
        gender char(1) NOT NULL,
        level varchar NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs 
    (
        song_id varchar PRIMARY KEY,
        title varchar NOT NULL,
        artist_id varchar NOT NULL,
        year int,
        duration float(5) NOT NULL
    );
""")

artist_table_create = ("""
      CREATE TABLE IF NOT EXISTS artists 
    (
        artist_id varchar PRIMARY KEY,
        name text NOT NULL,
        location varchar,
        latitude float(6),
        longitude float(6)
    );
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY, 
    hour INT NOT NULL, 
    day INT NOT NULL, 
    week INT NOT NULL, 
    month INT NOT NULL, 
    year INT NOT NULL, 
    weekday INT NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
     VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""
    INSERT INTO users
    (user_id, first_name, last_name, gender, level)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT(user_id) DO UPDATE SET
        first_name = COALESCE(EXCLUDED.first_name,users.first_name),
        last_name = COALESCE(EXCLUDED.last_name,users.last_name),
        gender = COALESCE(EXCLUDED.gender,users.gender),
        level = COALESCE(EXCLUDED.level,users.level);
""")

song_table_insert = ("""
    INSERT INTO songs
    (song_id, title, artist_id, year, duration)
    VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT(song_id) DO UPDATE SET
        title = COALESCE(EXCLUDED.title,songs.title),
        artist_id = COALESCE(EXCLUDED.artist_id,songs.artist_id),
        year = COALESCE(EXCLUDED.year,songs.year),
        duration = COALESCE(EXCLUDED.duration,songs.duration);
    
""")

artist_table_insert = ("""
    INSERT INTO artists
    (artist_id, name, location, latitude, longitude)
    VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT(artist_id) DO UPDATE SET
        name = COALESCE(EXCLUDED.name,artists.name),
        location = COALESCE(EXCLUDED.location,artists.location),
        latitude = COALESCE(EXCLUDED.latitude,artists.latitude),
        longitude = COALESCE(EXCLUDED.longitude,artists.longitude);
""")


time_table_insert = ("""
    INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT(start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id
    FROM songs s 
    JOIN artists a ON s.artist_id = a.artist_id
    WHERE s.title = %s
    AND a.name = %s
    AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]