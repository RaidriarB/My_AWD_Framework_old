def load_config(config):
	conf_dict = {}
	with open(config,"r") as config:
		text = config.read()
		lines = text.split("\n")

		for line in lines:
			# 跳过空行
			if line.strip() == "":
				continue

			# 解析key-value
			key,value = line.split("=")[0].strip(),line.split("=")[1].strip()
			#print(key,value)
			conf_dict[key] = value
	return conf_dict

def load_ip_list(config):
	config_dict = load_config(config)
	
	# 列表生成式格式
	ip_rules = config_dict["iplist"]
	iplist = eval(ip_rules)
	return iplist
