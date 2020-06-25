select name from actors
	where id in (select actor_id from movie_actors
		where movie_id = (select id from movies
			where director like "%Lerdam%"))


select director, COUNT(*) as count from movies
	group by director
	order by count desc

select name, COUNT(*) as count from actors join movie_actors on actors.id = movie_actors.actor_id
where name != "N/A"
group by name 
order by count desc limit 1

