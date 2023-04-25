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
duration TEXT NOT NULL
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

