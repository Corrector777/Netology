CREATE TABLE IF NOT EXISTS Genres(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Artists(
	id SERIAL PRIMARY KEY,
	name VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS GenresArtists (
	id_artist INTEGER REFERENCES Artists(id),
	id_genre INTEGER REFERENCES Genres(id),
	CONSTRAINT ppk PRIMARY KEY (id_artist, id_genre) 
);

CREATE TABLE IF NOT EXISTS Albums(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	albums_year DATE
);

CREATE TABLE IF NOT EXISTS ArtistsAlbums (
	id_artist INTEGER REFERENCES Artists(id),
	id_album INTEGER REFERENCES Albums(id),
CONSTRAINT sk PRIMARY KEY (id_artist, id_album) 
);

CREATE TABLE IF NOT EXISTS Tracks (
id SERIAL PRIMARY KEY,
id_album INTEGER REFERENCES Albums(id),
name VARCHAR(80) NOT NULL,
duration INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Collections (
id SERIAL PRIMARY KEY,
name VARCHAR(80) NOT NULL,
collection_year TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS CollectionsTracks (
	id_collection INTEGER REFERENCES Collections(id),
	id_tracks INTEGER REFERENCES Tracks(id),
CONSTRAINT tk PRIMARY KEY (id_collection, id_tracks) 
);

-- Заполните базу данных из предыдущего домашнего задания. В ней должно быть:

-- не менее 8 исполнителей:

INSERT INTO artists (name) VALUES
('Mick Jager'),
('Madonna'),
('Marylin Manson'),
('Lady Gaga'),
('Linking Park'),
('Oxxxymiron'),
('Saveus'),
('Moby');

-- не менее 5 жанров;

INSERT INTO genres (name) VALUES
('Rock'),
('Alternative'),
('Pop'),
('Rap'),
('Techno');

--таблица связи жанр-исполнитель:

INSERT INTO genresartists (id_artist, id_genre) VALUES
(1,1),
(1,2),
(2,3),
(2,1),
(3,3),
(4,5),
(4,3),
(5,4),
(6,4),
(7,5),
(7,3),
(8,2),
(8,5);
-- не менее 8 альбомов:

--ALTER TABLE albums ALTER COLUMN album_year TYPE integer USING extract(YEAR FROM album_year);

--ALTER SEQUENCE albums_id_seq RESTART WITH 1;

--delete from albums 
--where id>0;

INSERT INTO albums (name, album_year) VALUES
('first',2008),
('second',2018),
('third',2011),
('fourth',2019),
('fifth',2020),
('sixth',2022),
('seventh',2006),
('eighth',2021)

--таблица связи альбом-исполнитель:

INSERT INTO artistsalbums(id_artist, id_album) VALUES
(1,2),
(1,4),
(2,1),
(3,3),
(4,5),
(5,6),
(6,7),
(6,3),
(7,8),
(7,3),
(8,8);

-- не менее 15 треков:
--ALTER TABLE tracks ALTER COLUMN duration TYPE real ;
--ALTER SEQUENCE tracks_id_seq RESTART WITH 1;

--delete from tracks 
--where id>0;

INSERT INTO tracks (id_album, name, duration) VALUES
(1,'1track', 3.2),
(1,'2track', 2.2),
(2,'3track', 2.5),
(2,'4track', 4.2),
(3,'5track', 3.3),
(3,'6track', 4.3),
(4,'7track', 2.2),
(4,'8track', 2.7),
(5,'9track', 2.9),
(5,'10track', 3.1),
(6,'11track', 2.2),
(6,'12track', 5.5),
(7,'13track', 4.4),
(7,'14track', 4.4),
(8,'15track', 1.2),
(8,'16track', 2.0),
(6,'mytrack', 3.2),
(7,'track_my', 4.2);


-- не менее 8 сборников.
--ALTER TABLE collections ALTER COLUMN collection_year TYPE integer USING (collection_year::integer);

INSERT INTO collections(name, collection_year) VALUES
('1', 2012),
('2', 2014),
('3', 2015),
('4', 2020),
('5', 2023),
('6', 2019),
('7', 2018),
('8', 2021);

--таблица связи трек-коллекция:
INSERT INTO collectionstracks (id_collection, id_track) VALUES
(1,1),
(1,2),
(2,5),
(2,6),
(3,3),
(3,9),
(4,5),
(5,10),
(5,6),
(6,8),
(6,7),
(7,11),
(7,8),
(8,12),
(8,13),
(6,14),
(7,15),
(7,18),
(7,16);

-- Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.

--название и год выхода альбомов, вышедших в 2018 году:

SELECT name, album_year FROM albums
WHERE album_year = 2018;

--название и продолжительность самого длительного трека:

SELECT name, duration FROM tracks
WHERE duration = (SELECT MAX(duration) FROM tracks);

--название треков, продолжительность которых не менее 3,5 минуты:

SELECT name FROM tracks
WHERE duration >= 3.5;

--названия сборников, вышедших в период с 2018 по 2020 год включительно:

SELECT name FROM collections
WHERE collection_year >=2018 AND collection_year <=2020;

--исполнители, чье имя состоит из 1 слова:
SELECT name FROM artists
where name NOT LIKE '% %';
--where array_length(regexp_split_to_array(name, '\s+'),1) = 1; stackoverflow

--название треков, которые содержат слово “мой”/“my”:
SELECT name FROM tracks
where name LIKE '%my%';


  
