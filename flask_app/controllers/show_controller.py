from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.show_model import Show
from flask_app.models.user_model import User

@app.route('/shows/new')
def show_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create_show.html')

@app.route('/shows/create', methods=['post'])
def create_show():
    if not Show.validate_show(request.form):
        return redirect('/shows/new')
    show_data={
        **request.form,
        'user_id': session['user_id']
    }
    Show.save_show(show_data)
    return redirect('/shows')

@app.route('/shows/show/<int:show_id>')
def show_show(show_id):
    if 'user_id' not in session:
        return redirect('/')
    show=Show.get_by_id_show({'id':show_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template('show_show.html',show=show,user=user)

@app.route('/shows/edit/<int:show_id>')
def edit_show(show_id):
    if 'user_id' not in session:
        return redirect('/')
    show= Show.get_by_id_show({'id': show_id})
    session['show_id']= show_id
    return render_template('edit_show.html',show=show)

@app.route('/shows/edit', methods=['post'])
def edit():
    show_data= {
        **request.form,
        'id': session['show_id']
    }
    Show.update_show(show_data)
    return redirect('/shows')

@app.route('/shows/delete/<int:show_id>')
def delete(show_id):
    Show.delete_show({'id':show_id})
    return redirect('/shows')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')