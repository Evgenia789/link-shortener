from flask import (abort, Blueprint, current_app, flash, redirect, request,
                   render_template, url_for)
from sqlalchemy.exc import SQLAlchemyError

from app.short_link.models import Link
from app.database.db import db
from app.short_link.forms import LinkCreateForm


module = Blueprint('views', __name__, url_prefix ='/link_shortener')


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)

@module.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    """Redirect to short URL"""
    link = None
    try:
        link = Link.query.filter_by(short_url=short_url).first_or_404()
        link.clicks = link.clicks + 1
        db.session.commit()
    except SQLAlchemyError as e:
        log_error('Error while querying database', exc_info=e)
        flash('An unexpected error occurred during the request.', 'danger')
        abort(500)
    return redirect( link.long_url)

@module.route('/', methods=['GET'])
def index():
    links = None
    try:
        links = Link.query.order_by(Link.created_at).all()
        db.session.commit()
    except SQLAlchemyError as e:
        log_error('Error while querying database', exc_info=e)
        flash('An unexpected error occurred during the request.', 'danger')
        abort(500)
    return render_template('link/index.html', object_list=links)

@module.route('/shorten', methods=['POST'])
def create():
    """Create a short URL"""
    form = LinkCreateForm(request.form)
    try:
        if request.method == 'POST' and form.validate():
            if Link.query.filter_by(long_url=form.data['long_url']).first() is None:
                link = Link(**form.data)
                db.session.add(link)
                db.session.flush()
                db.session.commit()
                flash('The entry was successfully added!', 'success')
            else:
                link = Link.query.filter_by(long_url=form.data['long_url']).first()

            links = Link.query.order_by(Link.created_at).all()
    except SQLAlchemyError as e:
        log_error('There was error while querying database', exc_info=e)
        db.session.rollback()
        flash('An unexpected error occurred during a database query', 'danger')

    return render_template('link/shortened_link.html', object=link, object_list=links)
