from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from flash_learning import db
from flash_learning.email.utils import send_email
from flash_learning.main.emailtask import confirm_token, create_confirmation_token
from flash_learning.models.student import Student
from flash_learning.main.forms import ForgotPassword, ResetPassword


email = Blueprint("email", __name__)


@login_required
@email.route('/resend')
def resend_confirmation():
    token = create_confirmation_token(current_user.email)
    confirm_url = url_for('email.confirm_email', token=token, _external=True)
    html = render_template('confirm.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('main.index'))

@login_required
@email.route('/forgot_password', methods=['POST', 'GET'])
def forgot_confirmation():
    form = ForgotPassword()
    if form.validate_on_submit():
        flash('If your email is valid then you should receive a msg.', 'success')
        if  Student.query.filter_by(email=form.email.data).first()!=None:
            token = create_confirmation_token(form.email.data)
            confirm_url = url_for('email.confirm_password', token=token, _external=True)
            html = render_template('forgot_msg.html', confirm_url=confirm_url)
            subject = "Forgot Password"
            send_email(form.email.data, subject, html)
        return redirect(url_for('main.index'))
    return render_template("forgot_password.html", title="Forgot Password", form=form)






@email.route('/reset-password/<token>', methods=['POST', 'GET'])
def confirm_password(token):
    try:
        email = confirm_token(token)
    except:
        flash('Issue Resetting Password')
        return redirect(url_for('main.index'))
    form=ResetPassword()
    if form.validate_on_submit():
        user = Student.query.filter_by(email=email).first()
        user.set_password(form.password.data)
        flash("Password Succefully Reset")
        return redirect(url_for('main.index'))
    return render_template("reset_password.html", title="Reset Password", form=form)









    return redirect(url_for('main.index'))









@email.route('/confirm/<token>', methods=['POST', 'GET'])
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('This Confirmation Email has expired')
        return redirect(url_for('main.index'))

    user = Student.query.filter_by(email=email).first()

    if user.activated:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.activated = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')

    return redirect(url_for('main.index'))
