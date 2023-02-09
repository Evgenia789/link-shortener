from flask import (abort, Blueprint, current_app, redirect, request,
                   render_template)
from http import HTTPStatus
from sqlalchemy.exc import SQLAlchemyError

from app.short_link.models import Link
from app.database.db import db
from app.short_link.forms import LinkCreateForm
from config import Config


module = Blueprint('views', __name__, url_prefix='/link_shortener')


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


@module.route('/<short_url>', methods=['GET'])
def forward_to_target_url(short_url: str):
    """Forward to target URL"""
    link = None
    try:
        link = Link.query.filter_by(short_url=short_url).first_or_404()
        link.clicks += 1
        db.session.commit()
    except SQLAlchemyError as e:
        log_error('Error while querying database', exc_info=e)
        abort(HTTPStatus.NOT_FOUND)
    return redirect(link.long_url)


@module.route('/', methods=['GET'])
def index():
    """Get all URLs"""
    links = None
    try:
        links = Link.query.order_by(Link.created_at.desc()).all()
        db.session.commit()
    except SQLAlchemyError as e:
        log_error('Error while querying database', exc_info=e)
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    context = {"object_list": links}

    return render_template('link/index.html', context=context)


@module.route('/shorten', methods=['GET', 'POST'])
def create_url():
    """Create a short URL"""
    form = LinkCreateForm(request.form)
    try:
        if (form.validate() and Link.query.filter_by(
            long_url=form.data['long_url']
        ).first() is None):
            db.session.add(Link(**form.data))
            db.session.commit()
    except SQLAlchemyError as e:
        log_error('There was error while querying database', exc_info=e)
        db.session.rollback()

    context = {
        "object": Link.query.filter_by(long_url=form.data['long_url']).first(),
        "object_list": Link.query.order_by(Link.created_at.desc()).all(),
        "base_url": Config.BASE_URL+module.url_prefix,
        "form": form
    }

    return render_template('link/shortened_link.html', context=context)
