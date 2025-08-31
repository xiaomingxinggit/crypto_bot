import urllib.request
import urllib.error
import json

import ssl
# 创建一个SSL上下文对象
context = ssl.create_default_context()
# 忽略SSL证书验证
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

import os
# 获取企业微信群消息推送KEY
wechat_bot_key = os.getenv('WECHAT_BOT_KEY', '')

def wechat_push(text):
	data = {
		"msgtype": "text",
		"text": {
			"content": text
		}
	}

	json_data = json.dumps(data).encode('utf-8')

	request = urllib.request.Request(
		f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={wechat_bot_key}',
		data = json_data,
		headers = {'Content-Type': 'application/json'},
		method = 'POST'
	)
	try:
		with urllib.request.urlopen(request, context=context) as response:
			response_json = json.load(response)
		if response_json['errmsg'] == 'ok':
			return True
		else:
			print(response_json)
			return False
	except Exception as e:
		print(e)
		return False

if __name__ == '__main__':
	wechat_push('wechat_push 已接入')
