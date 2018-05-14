import datetime

from peewee import (ForeignKeyField, CharField)

from models.photo import Photo
from models.base import BaseModel
from models.hashtag import Hashtag

class HashtagUsed(BaseModel):

    photo = ForeignKeyField(Photo)
    hastag = ForeignKeyField(Hashtag)
