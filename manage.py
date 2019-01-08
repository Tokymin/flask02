# encoding='utf-8'

from flask import Flask, request

# 实例化，创建对象
ligong = Flask(__name__)


@ligong.route('/')
def index():
    return 'hello'


@ligong.route('/path/<path:p>/')
def path(p):
    return p


@ligong.route('/test_request/')
def test_request():
    # 返回完整的URL
    # return request.url
    # return request.base_url
    # return request.host_url
    # return request.path
    return request.remote_addr  # 客户端访问的IP地址


# 启动实例
if __name__ == '__main__':
    ligong.run(debug=True, port=5055, threaded=True, host='0.0.0.0')
