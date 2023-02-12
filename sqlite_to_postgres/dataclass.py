import uuid
from dataclasses import dataclass
from datetime import datetime

from dateutil import parser


@dataclass
class BasedMixin:

    @classmethod
    def row_factory(cls, cursor, row):
        columns = [column[0] for column in cursor.description]
        row = dict(zip(columns, row))
        return cls.from_row(**row)


@dataclass
class TimeStampedMixin:
    created_at: datetime
    updated_at: datetime

    def to_datetime(self):
        self.created_at = parser.parse(self.created_at)
        self.updated_at = parser.parse(self.updated_at)
        
   
@dataclass
class UUIDMixin:
    id: uuid.UUID

    def to_uuid(self):
        self.id = uuid.UUID(self.id)


@dataclass
class Genre(TimeStampedMixin, UUIDMixin, BasedMixin):
    name: str
    description: str

    def __post_init__(self):
        self.to_datetime()
        self.to_uuid()

    @classmethod
    def from_row(cls, id, name, description, created_at, updated_at):
        return cls(
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at)
    
    def to_pg(self) ->dict:
        return {'id':str(self.id), 
                'name':self.name, 
                'description':str(self.description), 
                'created':str(self.created_at), 
                'modified':str(self.updated_at)}


@dataclass
class Person(TimeStampedMixin, UUIDMixin, BasedMixin):
    full_name: str

    def __post_init__(self):
        self.to_datetime()
        self.to_uuid()

    @classmethod
    def from_row(cls, id, full_name, created_at, updated_at):
        return cls(
            id=id,
            full_name=full_name,
            created_at=created_at,
            updated_at=updated_at)
        
    def to_pg(self) ->dict:
        return {'id':str(self.id), 
                'full_name':self.full_name,
                'created':str(self.created_at), 
                'modified':str(self.updated_at)}


@dataclass
class Filmwork(TimeStampedMixin, UUIDMixin, BasedMixin):
    title: str
    description: str
    creation_date: datetime
    rating: float
    type: str
    file_path: str

    def __post_init__(self):
        self.to_datetime()
        self.to_uuid()
        self.creation_date = None if self.creation_date is None else parser.parse(
            self.creation_date)
        self.rating = self.rating

    @classmethod
    def from_row(cls, id, title, description, creation_date, rating, type,
                 file_path, created_at, updated_at):
        return cls(
            id=id,
            title=title,
            description=str(description),
            creation_date=creation_date,
            rating=rating,
            type=type,
            file_path=str(file_path),
            created_at=created_at,
            updated_at=updated_at)
    
    def to_pg(self) ->dict:
        return {'id':str(self.id), 
                'title':self.title, 
                'description':self.description,
                'creation_date':str(self.creation_date),
                'rating':str(self.rating), 
                'type':self.type, 
                'file_path':self.file_path,
                'created':str(self.created_at), 
                'modified':str(self.updated_at)}


@dataclass
class PersonFilmwork(UUIDMixin, BasedMixin):
    film_work_id: uuid.UUID
    person_id: uuid.UUID
    role: str
    created_at: datetime

    def __post_init__(self):
        self.to_uuid()
        self.film_work_id = uuid.UUID(self.film_work_id)
        self.person_id = uuid.UUID(self.person_id)
        self.created_at = parser.parse(self.created_at)

    @classmethod
    def from_row(cls, id, film_work_id, person_id, role, created_at):
        return cls(
            id=id,
            film_work_id=film_work_id,
            person_id=person_id,
            role=role,
            created_at=created_at)
        
    def to_pg(self) ->dict:
        return {'id':str(self.id),
                'film_work_id':str(self.film_work_id), 
                'person_id':str(self.person_id), 
                'role':self.role,
                'created':str(self.created_at)}


@dataclass
class GenreFilmwork(UUIDMixin, BasedMixin):
    film_work_id: uuid.UUID
    genre_id: uuid.UUID
    created_at: datetime

    def __post_init__(self):
        self.to_uuid()
        self.film_work_id = uuid.UUID(self.film_work_id)
        self.genre_id = uuid.UUID(self.genre_id)
        self.create_at = parser.parse(self.created_at)

    @classmethod
    def from_row(cls, id, film_work_id, genre_id, created_at):
        return cls(
            id=id,
            film_work_id=film_work_id,
            genre_id=genre_id,
            created_at=created_at)
        
    def to_pg(self) ->dict:
        return {'id':str(self.id),
                'film_work_id':str(self.film_work_id), 
                'genre_id':str(self.genre_id), 
                'created':str(self.created_at)}
