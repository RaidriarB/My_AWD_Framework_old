import requests

flag_api = "http://127.0.0.1:8888/api"

'''
提交flag的逻辑需要在这里编写
需要返回flag是否提交成功的判断
'''
def submit_flag(flag,host):

	if host == "172.17.2.1":
		return False

	r = requests.get(flag_api,params={"flag":flag,"host":host})
	if r.status_code == 404:
		return True
	else:
		return False