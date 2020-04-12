from flask import Blueprint, render_template, flash, url_for, redirect, request
from app.forms import PostForm
from app.models import Posts
from flask_login import current_user
from app.extensions import db

main = Blueprint('main',__name__)


@main.route('/', methods=['GET','POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            u = current_user._get_current_object()
            p = Posts(content=form.content.data, user=u)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('You need to login first')
            return redirect(url_for('user.login'))
    #read messages from db
    # posts = Posts.query.filter_by(rid=0).order_by(Posts.timestamp.desc()).all()

    # get current page number
    page = request.args.get('page', 1, type=int)
    pagination = Posts.query.filter_by(rid=0).order_by(Posts.timestamp.desc()).paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    return render_template('main/index.html', form=form, posts=posts, pagination=pagination)


