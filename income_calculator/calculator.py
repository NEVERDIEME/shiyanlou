# -*- coding: utf-8 -*-
import sys
import csv

class Args(object):
	def __init__(self):
		self.args = sys.argv[1:]
	def get_path(self,cmd):
		return self.args[self.args.index(cmd)+1]

args = Args()

class Config(object):
	def __init__(self):
		self.config = self._read_config()

	def _read_config(self):
		config = []
		with open(args.get_path('-c')) as f:
			for line in f.readlines():
				config.append(line.split(' = '))
			config = dict(config)
		return config
	
	def get_config(self,cfg):
		return self.config.get(cfg,None)

cfgs = Config()

class UserData(object):
	def __init__(self):
		self.userdata = self._read_users_data()

	def _read_users_data(self):
		userdata = []
		with open(args.get_path('-d')) as f:
			lines = csv.reader(f)
			for line in lines:
				userdata.append([int(x) for x in line])
		return dict(userdata)

usd = UserData()

class IncomeTaxCalculator(object):
	def calc_for_all_userdata(self):
		users = cfgs.userdata
		for id,income in users.items():
			id = id
			income = income
			jishul = cfgs.get_config('JiShuL')
			jishuh = cfgs.get_config('JiShuH')
			yanglao = cfgs.get_config('YangLao')
			yiliao = cfgs.get_config('YiLiao')
			shiye = cfgs.get_config('ShiYe')
			gongshang = cfgs.get_config('GongShang')
			shengyu = cfgs.get_config('ShengYu')
			gongjijin = cfgs.get_config('GongJiJin')
			security = min(max(income,jishul),jishuh)*sum([yanglao,yiliao,shiye,gongshang,shengyu,gongjijin])
			tax_rate = [0.45,0.35,0.3,0.25,0,2,0.1,0.03]
			quick_deduction = [13505,5505,2755,1005,555,105,0]
			breakpoint = [80000,55000,35000,9000,4500,1500]
	
	def export(self, default='csv'):
		result = self.calc_for_all_userdata()
		with open(args.get_path('-o')) as f:
			writer = csv.writer(f)
			writer.writerows(result)
			 
		
