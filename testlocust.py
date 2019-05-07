import os
from locust import HttpLocust, TaskSet, task


onejson = {
	"Method": "Get",
	"Host": "http://10.10.4.5",
	"Url": "/src/warn/#/login",
	"Data": {},
	"Usernum": 100,
	"Usersec": 20,
	"testtime": "20s",
}


def getonetask():
	# TODO: 读取一条记录进行测试
	pass


def makelocust(var_picpath):
	# TODO: 读取一条记录进行测试
	pass


def run(var_json=onejson):
	# TODO: 运行构建的locust
	runstr = 'locust -f testlocust.py --csv=result --no-web -c %d -r %d -t %s' % (
	onejson['Usernum'], onejson['Usersec'], onejson['testtime'])
	print(runstr)
	# return
	os.system(runstr)


class oneTaskSet(TaskSet):
	@task
	def onetask(self):
		if onejson['Method'] == 'Post':
			print('post')
		else:
			self.client.get(
				url=onejson['Url'],
				params=onejson['Data'],
				# verify=False,
			)


class oneTaskLocust(HttpLocust):
	task_set = oneTaskSet
	# TODO: 填写host
	host = onejson['Host']
	min_wait = 500
	max_wait = 1500
