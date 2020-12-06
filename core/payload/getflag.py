'''
这里的所有方法都会被执行，用于获取flag。
方法应该传入被攻击目标（例如格式：127.0.0.1:8080）
应该返回可以提交的flag字符串
请不要在这里输出额外信息。

注：记得加上timeout
'''

def attack_test1(target):

	if target == "172.17.2.1":
		return None	
	host = "http://%s" %target
	flag = "flag{host_is_%s}" % host
	return flag

def attack_test2(target):

	return "flag{target_is_%s}"%target

def attack_error_test1(target):

	a = 1/0 # Exception
	return "flag{you_should_not_see_this}"

def attack_duplicate_test(target):
	# flag 重复了
	return "flag{host_is_%s}"%target