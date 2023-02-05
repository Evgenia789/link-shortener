from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
    current_app,
)
from sqlalchemy.exc import SQLAlchemyError

from app.short_link.models import Link
from app.database.db import db
from app.short_link.forms import LinkCreateForm

module = Blueprint('links', __name__, url_prefix ='/link_shortener')


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)

@module.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    link = None
    try:
        link = Link.query.filter_by(short_url=short_url).first_or_404()
        link.clicks = link.clicks + 1
        db.session.commit()
    except SQLAlchemyError as e:
        log_error('Error while querying database', exc_info=e)
        flash('Во время запроса произошла непредвиденная ошибка.', 'danger')
        abort(500)
    return redirect(link.original_url)

@module.route('/', methods=['GET'])
def index():
    links = None
    try:
        links = Link.query.order_by(Link.created_at).all()
        db.session.commit()
    except SQLAlchemyError as e:
        log_error('Error while querying database', exc_info=e)
        flash('Во время запроса произошла непредвиденная ошибка.', 'danger')
        abort(500)
    return render_template('entity/index.html', object_list=links)

@module.route('/shorten', methods=['POST'])
def create():
    form = LinkCreateForm(request.form)
    try:
        if request.method == 'POST' and form.validate():
            link = Link(**form.data)
            db.session.add(link)
            db.session.flush()
            id = link.id
            db.session.commit()
            flash('Запись была успешно добавлена!', 'success')
            return redirect(url_for('entity.view', id=id))
    except SQLAlchemyError as e:
        log_error('There was error while querying database', exc_info=e)
        db.session.rollback()
        flash('Произошла непредвиденная ошибка во время запроса к базе данных', 'danger')
    return render_template('entity/create.html', form=form)
