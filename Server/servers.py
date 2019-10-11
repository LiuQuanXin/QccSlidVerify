# !/usr/bin/python
# coding: utf-8
# time: 2019/6/20

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urlparse
import json
import logging
from flask import Flask, make_response, request, jsonify, render_template
import datetime

today = datetime.datetime.now()

app = Flask(__name__, static_folder='static')


@app.route('/qcc')
def qcc():
    return render_template("qcc.html")

@app.route('/ali', methods=['get', 'post'])
def ali():
    query = urlparse.parse_qs(request.query_string)
    logging.warning('轨迹生成加密参数[' + query['n'][0] + ']')
    d = {
        "success": True,
        "result":
            {
                "csessionid": "01NARpzbxMmcSeS_ddSrBU19FwoKl9g7Sml13oTdICjXDMDNVtDC5f4Rw4-yjhC9mt_SACvQ7y0gh3d0xIxWmtGGCPTxLVPmFVWgNrJfbz2Il4xWPpmrqNFWApDr4s8xl9ujWpvYpgykOFcvRGIYmRN-DUma2ZVFKNrDPSAPwY6B0",
                "code": 0,
                "value": "05jSD_TG6z_UmOqV4rRQeS-v4oQPPI8s4z2RRrqLAvxoFyoVSMKVynHegmrBWqMSMMjTQViAU_sQuKqbE9ZimVKtdvSdTkeZALQ0rrIMYWunJvgOeHdtBC3lYmiq4SCzI4AbaUvWLdIQSwJtKubblRE8TOZsimQMfHGuQ2WS57prjuSDCV-8-LXtZvs7hfhYwXY-Z_IIB96tuFc1bzMFEvJl8pzwqKkyXOqgng2LuMCY1n1kzrTnzAJjn02qZ1i-AGSwaVrzH3i73YLDhmYSctE_2xHj2riTJoG-HEm7hZx6gyeUS0XGeDcGRr0WSnaPsxdVSLMfEvW0OzU_5M-EIdUZ_VqPGOfZ8pbUrUxLRRPpp4POS7crVt4z9PzvC2duTk"
            }
    }
    res = '{cb}({d});'.format(cb=query['callback'][0], d=json.dumps(d))
    res = make_response(res)
    logging.warning(
        'https://cf.aliyun.com/nocaptcha/analyze.jsonp?' + request.url.replace('http://127.0.0.1:8880/ali?', ''))
    res.headers["content-type"] = "text/javascript;charset=UTF-8"
    return res


if __name__ == '__main__':
    app.run(debug=True, port=8880, threaded=True)
