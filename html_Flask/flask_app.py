from flask import Flask, render_template, request
from flask import redirect, url_for, session, send_from_directory

# set the project root directory as the static folder, you can set others,
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('./index_flask.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/main')
def hello_workd():
    return '<h1>Hello FLASK World!</h1>'

@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username='default'):
    return 'USER : %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post #Num : %d'%post_id

@app.route('/logging')      # show logging message on console
def logging_test():         # logger message
    test = 1
    app.logger.debug('NEED : Debugging!')
    app.logger.warning(str(test) + ' Line')
    app.logger.error('*** ERROR!! ***')
    return "_EOL_ : End of Logging message is printed out at console : DONE!"

@app.route('/login_form')
def login_form():
    return render_template('./login_form.html')

@app.route('/login', methods=['POST'] )
def login():
    if request.method == 'POST':
        if (request.form['username'] == 'Jamie' and request.form['password'] == '1234'):
            session['logged_in'] = True
            session['username'] = request.form['username']

        else:
            return '*** ERROR: Login Information are not valid!'
    else:
        return '*** ERROR: Wrong Acess (Access\'s denied)'

@app.route('/get_test', methods=['GET'])
def get_test():
    if request.method == 'GET':
        if (request.args.get('username') == 'Jamie' and request.args.get('password') == '1234'):
            return request.args.get('username') + "~!! , we welcome you...."
        else:
            return '*** ERROR: Login Information are not valid!'
    else:
        return '*** ERROR: Wrong Acess (Access\'s denied)'

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/template')
@app.route('/template/<temp_id>')
def template_test(temp_id='Golf'):
    sports = ['Baseball','Soccer','Basketball','Valleyball','Hokkey','Golf','Ping-pong',]
    return render_template('template.html', temp_id=temp_id, sports=sports)

app.secret_key = 'sample_secret_key'
# session & request were used.
# app.secret_key = 'abc' --> should be added!




if __name__ == '__main__':
    app.run(
        host='localhost',
        debug = True,
        port=int('5000'),
        )
