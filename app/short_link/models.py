from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app.database.db import db
from app.utils.keygen import generate_random_key


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
        self.short_url = self.create_short_url()

    def create_short_url(self):
        """Check the existence and uniqueness of the short URL"""
        key = generate_random_key()
        while Link.query.filter_by(short_url=key).first() is not None:
            key = generate_random_key()

        return key
