from flask import Flask, request
from time import time,strftime,localtime
from os import getcwd, mkdir
import urllib.request

p = getcwd()
try:
    mkdir(p+'/Get_IP/')
except FileExistsError:
    pass
try:
    mkdir(p+'/Get_IP/logs/')
except FileExistsError:
    pass

app = Flask(__name__)


@app.route('/api/Get/IP')
def Get_IP():

    # 如果使用Nginx，请使用以下代码：
    """
    ip = request.headers['X-Forwarded-For']
    """
    ip = request.remote_addr
    response = urllib.request.urlopen('http://ip-api.com/json/'+ip).read().decode('utf-8')
    if not bool(request.args.get('id')):
        with open('./Get_IP/logs/'+request.args.get('id')+'.log','a', encoding='ASCII') as f:
            f.write(strftime('%Y-%m-%d %H:%M:%S', localtime())+'  '+ip+response+'\n')
        return '唔唔唔'
    else:
        return '唔唔唔你知不知你没加参数唔唔唔'


if __name__ == '__main__':
    app.run()

