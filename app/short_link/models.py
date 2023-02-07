from datetime import datetime
import secrets
from sqlalchemy import Column, Integer, String, DateTime
import string

from app.database.db import db


class Link(db.Model):
    """
    A class used to represent a link.
    A short link is automatically generated before saving.
    """
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
        """Check existing and generate a short URL"""
        characters = string.digits + string.ascii_letters
        short_url = "".join(secrets.choice(characters) for _ in range(8))
        link = Link.query.filter_by(short_url=short_url).first() is None
        if link:
            return short_url
        
        return link.short_url
