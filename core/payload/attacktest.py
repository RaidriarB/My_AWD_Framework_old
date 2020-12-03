'''
请不要在这里输出信息
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

