from flask import Flask, request
from time import strftime, localtime
from os import getcwd, mkdir
import urllib.request

p = getcwd()
try:
    mkdir(f'{p}/Get_IP/')
except FileExistsError:
    pass
try:
    mkdir(f'{p}/Get_IP/logs/')
except FileExistsError:
    pass

app = Flask(__name__)


@app.route('/api/Get/IP')
def get_ip():    # 虽然感觉用大写好点，但编辑器还是推荐我用小写/滑稽
    # 如果使用Nginx，请使用以下代码：
    """
    ip = request.headers['X-Forwarded-For']
    """
    ip = request.remote_addr
    response = (
        urllib.request.urlopen(f'http://ip-api.com/json/{ip}')
        .read()
        .decode('utf-8')
    )
    if bool(request.args.get('id')):
        with open('./Get_IP/logs/' + request.args.get('id') + '.log', 'a', encoding='ASCII') as f:
            f.write(strftime('%Y-%m-%d %H:%M:%S', localtime()) + '  ' + ip + response + '\n')
        return '唔唔唔'
    else:
        return '唔唔唔你知不知你没加参数唔唔唔'


@app.route('/api/See/IP')
def see_ip():  # 虽然感觉用大写好点，但编辑器还是推荐我用小写/滑稽
    if not bool(request.args.get('id')):
        return '唔唔唔你知不知你没加参数唔唔唔'
    with open('./Get_IP/logs/' + request.args.get('id') + '.log', 'r', encoding='ASCII') as f:
        fi = f.read()
    return fi


if __name__ == '__main__':
    app.run()
