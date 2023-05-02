--количество исполнителей в каждом жанре;

SELECT name, count(id_artist) FROM genresartists ga 
LEFT JOIN genres g ON ga.id_genre  = g.id  
GROUP BY name;


--количество треков, вошедших в альбомы 2019-2020 годов;

SELECT COUNT(*) FROM tracks t 
LEFT JOIN albums a ON t.id_album = a.id 
WHERE a.album_year BETWEEN 2019 AND 2020;

--вариант с группировкой по годам

SELECT  album_year, COUNT(*) FROM tracks t 
LEFT JOIN albums a ON t.id_album = a.id 
WHERE a.album_year BETWEEN 2019 AND 2020
GROUP BY album_year;


--средняя продолжительность треков по каждому альбому;

SELECT a.name, AVG(duration) FROM tracks t 
LEFT JOIN albums a ON t.id_album  = a.id 
GROUP BY a.name
ORDER BY AVG(duration) DESC;

--все исполнители, которые не выпустили альбомы в 2020 году;

SELECT DISTINCT a.name FROM artistsalbums aa 
LEFT JOIN artists a ON aa.id_artist = a.id 
LEFT JOIN albums al ON aa.id_album  = al.id 
WHERE al.album_year != 2020;

--названия сборников, в которых присутствует конкретный исполнитель (выберите сами);

SELECT DISTINCT collections.name FROM collections 
JOIN collectionstracks ct ON ct.id_collection = collections.id  
JOIN tracks t ON ct.id_tracks  = t.id  
JOIN albums a ON a.id = t.id_album  
JOIN artistsalbums art ON art.id_album  = a.id  
JOIN artists ON artists.id  = art.id_artist  
WHERE artists.name LIKE '%Mick%';

--название альбомов, в которых присутствуют исполнители более 1 жанра;

SELECT a."name", count(g2."name")  FROM albums a 
JOIN artistsalbums a2 ON a.id = a2.id_album 
JOIN artists a3 ON a3.id = a2.id_artist 
JOIN genresartists g ON a3.id = g.id_artist 
JOIN genres g2 ON g2.id = g.id_genre
GROUP BY a."name"
HAVING COUNT(g2."name") > 1;

--наименование треков, которые не входят в сборники;

SELECT tracks.id  FROM tracks
LEFT JOIN collectionstracks c ON c.id_tracks = tracks.id 
WHERE c.id_collection is null; 

-- исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);

SELECT a3."name", t.duration  FROM tracks t 
JOIN albums a ON a.id  = t.id_album 
JOIN artistsalbums a2 ON a2.id_album = a.id 
JOIN artists a3 ON a3.id = a2.id_artist 
WHERE t.duration = (SELECT MIN(duration) FROM tracks)

--название альбомов, содержащих наименьшее количество треков.

SELECT a.name, count(t.id)  FROM albums a 
JOIN tracks t ON t.id_album = a.id 
GROUP BY a.name
having count(t.id) = 
	(select count(t.id)  from albums a 
	join tracks t on t.id_album  = a.id 
	group by a.id 
	order by count(t.id)
	limit 1);

