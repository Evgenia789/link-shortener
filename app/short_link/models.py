import secrets
import string
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app.database.db import db

class Link(db.Model):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    long_url = Column(String(512))
    short_url = Column(String(8), unique=True)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = "".join(secrets.choice(characters) for _ in range(8))
        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url
