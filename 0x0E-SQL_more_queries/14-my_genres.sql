-- list genres
-- of dexter
SELECT tv_genres.name FROM tv_genres JOIN tv_shows 
  ON tv_show_genres.show_id = tv_genres.id;
