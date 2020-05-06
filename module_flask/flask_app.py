"""
# Simple 'HELLO! flask World!' Practice
# REF SITE = https://bit.ly/35AiM8r
"""
# 파이썬 Flask로 간단 웹서버 구동하기
# NOTE: templates, static should be as it is named

print(__doc__)

from flask import (
                Flask,
                render_template,
                request,
                redirect,
                url_for,
                session,
                send_from_directory,
            )

LINKS = {
        'home' : 'http://localhost:5000/home',
        'info' : 'http://localhost:5000/info',
        'log-in': 'http://localhost:5000/login_form',
        'post': 'http://localhost:5000/post/1',
        'user': 'http://localhost:5000/user/',
        'test': 'http://localhost:5000/get_test',
        'log-out': 'http://localhost:5000/logout',
        'template': 'http://localhost:5000/template/Baseball',
    }

def main():

    # @app.route('/')
    # def index():
    #     return 'Hello Flask World!'

    @app.route('/')
    @app.route('/home')
    def index():
        render = render_template(
                        'index.html',
                        links=LINKS,
            )
        return render

    @app.route('/info')
    def info():
        img = url_for('static', filename='totoro.jpg')
        thumbs = {
                'redish' : url_for('static', filename='ve01_redish.jpg'),
                'paprika' : url_for('static', filename='ve02_paprika.jpg'),
                'eggplant' : url_for('static', filename='ve03_eggplant.jpg'),
                'avocado' : url_for('static', filename='ve04_avocado.jpg'),
            }


        render = render_template(
                'info.html',
                title='Flask Template Test',
                home_str='Hello Flask!',
                home_list=[1, 2, 3, 4],
                img=img,
                thumbs=thumbs,
                size_thumbnail=110,
                links=LINKS,
            )
        return render

    @app.errorhandler(404)
    def page_not_found(error):
        return '<H1>404-PAGE NOT FOUND!</H1>', 404


    @app.route('/post/<int:id_post>')
    def show_post(id_post):
        return f"<H1> TEMPLATE : POST #NUM = {id_post} </H1>"


    @app.route('/logging')      # show logging message on console
    def logging():         # logger message
        warning = 12
        app.logger.debug('NEED : Debugging!')     # ONLY IF DEBUGGING = ON
        app.logger.warning(f'***{warning} LINE ***')
        app.logger.error('*** OUT OF INDEX ERROR!! ***')
        return "Logging message is printed out at console!"

    @app.route('/user/')
    @app.route('/user/<username>')
    def show_profile(username='False!'):
        return f"<H1> USERNAME = {username} </H1>"

    @app.route('/login_form')
    def login_form():
        render = render_template(
                            'login_form.html',
                            links=LINKS,
                        )
        return render

    # @app.route('/login', methods=['POST'] )
    # def login():
    #     if request.method == 'POST':
    #         if (request.form['username'] == 'Jamie' and request.form['password'] == '1234'):
    #             session['logged_in'] = True
    #             session['username'] = request.form['username']
    #         else:
    #             return '*** ERROR: Login Information are not valid!'
    #     else:
    #         return '*** ERROR: Wrong Acess (Access\'s denied)'


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
        return redirect(url_for('home'))

    @app.route('/template')
    @app.route('/template/<temp_id>')
    def template_test(temp_id='Golf'):
        sports = [
                    'Baseball',
                    'Soccer',
                    'Basketball',
                    'Valleyball',
                    'Hokkey',
                    'Golf',
                    'Ping-pong',
                ]
        render = render_template(
                            'template.html',
                            temp_id=temp_id,
                            sports=sports,
                            links=LINKS,
                        )
        return render


if __name__ == '__main__':
    app = Flask(__name__)
    main()
    app.run()
