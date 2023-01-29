CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
); 

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    genre_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
    created timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role TEXT NOT NULL,
    created timestamp with time zone
);

ALTER TABLE content.genre_film_work
    ADD CONSTRAINT fk_genre_id
    FOREIGN KEY (genre_id)
    REFERENCES content.genre (id) 
    ON DELETE CASCADE;

ALTER TABLE content.genre_film_work
    ADD CONSTRAINT fk_film_work_id
    FOREIGN KEY (film_work_id)
    REFERENCES content.film_work (id) 
    ON DELETE CASCADE;

ALTER TABLE content.person_film_work
    ADD CONSTRAINT fk_film_work_id
    FOREIGN KEY (film_work_id)
    REFERENCES content.film_work (id) 
    ON DELETE CASCADE;

ALTER TABLE content.person_film_work
    ADD CONSTRAINT fk_person_id
    FOREIGN KEY (person_id)
    REFERENCES content.person (id) 
    ON DELETE CASCADE;

CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id);
CREATE UNIQUE INDEX film_work_genre_idx ON content.genre_film_work (genre_id, film_work_id);
CREATE INDEX film_work_idx ON content.film_work (title);
CREATE INDEX film_work_creation_date_idx ON content.film_work (creation_date);
CREATE INDEX film_work_rating_idx ON content.film_work (rating);
CREATE INDEX person_idx ON content.person (full_name);
CREATE INDEX genre_idx ON content.genre (name);
