from datetime import timedelta
from flask import Flask, request
from flask_restful import Api, Resource
# from account import Account
# from userAuth import UserAuth
from flask_jwt_extended import JWTManager
from apscheduler.schedulers.blocking import BlockingScheduler
from coreModule import scheduler
import zoneinfo
import random




app = Flask(__name__)
app.secret_key = '123qweasd'
api = Api(app)

app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
jwt = JWTManager(app)

JKT = zoneinfo.ZoneInfo("Asia/Jakarta")
sched = BlockingScheduler(timezone=JKT)


# @sched.scheduled_job('cron', id='my_job_id', hour=16, minute=40)
@sched.scheduled_job('cron', id='my_job_id', second='*')    
def start():
    print('start checking')
    scheduler.schedule()
sched.start()
    
# api.add_resource(Account, '/accounts')
# api.add_resource(UserAuth, '/login')



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    # def post(self):
    #     url = 'http://localhost:3000/'
    #     dat = request.form
    #     crateData = {'name': 123}
    #     # print()
    #     response = requests.post(
    #         url, data=json.dumps(crateData),
    #         headers={'Content-Type': 'application/json'}
    #     )
        
    #     return response.json()
        # return {'data': data}    

class ImagePost(Resource):
    def post(self):
        # fileImage = request.files['image']
        return {'asas'}
        

api.add_resource(HelloWorld, '/')
api.add_resource(ImagePost, '/image')




if __name__ == "__main__":
    app.run()

app.run(port=5000, debug=True)

