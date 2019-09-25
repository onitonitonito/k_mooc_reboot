from flask import Flask
from flask_restful import Resource, Api

import os

buildBranch = 'master'

# 어느패스에 빌드할 것인지 목적지 설정(!)
# buildCommend = 'cd ' + buildPath + ' && git pull origin ' + buildBranch + ' && npm run build'
buildPath = '/var/www/project/'

# cd /var/www/project/ && git pull origin master && .... 과 같은 명령
# 커맨드로 해결할 수 있는것은 다 가능하다
buildCommend = 'cd ' + buildPath + ' && git pull origin ' + buildBranch

app = Flask(__name__)
api = Api(app)

class setDeploy(Resource):
    def post(self):
        os.system(buildCommend)
        return {'status': 'success'}

api.add_resource(setDeploy, '/deploy')
# 예외처리는 생략 함




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=420, debug=True)
