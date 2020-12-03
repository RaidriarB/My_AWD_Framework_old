'''
这里的所有方法都会被执行，用于获取flag。
方法应该传入被攻击主机ip（格式：127.0.0.1）
应该返回可以提交的flag字符串
请不要在这里输出额外信息。
'''

def attack_test1(ip):

	if ip == "172.17.2.1":
		return None	
	host = "http://%s:8080" % ip
	flag = "flag{host_is_%s}" % host
	return flag

def attack_test2(ip):

	return "flag{ip_is_%s}"%ip

def attack_error_test1(ip):

	a = 1/0 # Exception
	return "flag{you_should_not_see_this}"

