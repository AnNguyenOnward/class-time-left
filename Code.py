import datetime
#schedule = input('what schedule do you want to use')
#time that is given to get to classes in minutes
passing_time = 4
dt = datetime.datetime.today()
def give_time(i,period_time):
	print('period {}: {} - {}'.format(i,period_time[0],period_time[1]))
def int_t(convert,h_m):
	p = convert.split(':')
	pas = int(p[h_m])
	return pas
def check_time(period_time):
	period_time_start = datetime.datetime(dt.year,dt.month,dt.day,int_t(period_time[0],0),int_t(period_time[0],1))
	period_time_end = datetime.datetime(dt.year,dt.month,dt.day,int_t(period_time[1],0),int_t(period_time[1],1))
	time_left = period_time_end - dt
	time_till = period_time_start - dt
	if time_till <= datetime.timedelta(days=0) <= time_left:
		 return 'time left: {} minutes and {} seconds \n'.format(round(time_left.total_seconds()/60),round(time_left.total_seconds()%60))
def check_block(period_times,day):
	lunch_time = period_times[-1]
	for i in range(len(period_times)-1):
		if check_time(period_times[i]) != None:
			print(check_time(period_times[i]))
	if day == 2:
		lunch_time = period_times[-1]
		for i in range(len(period_times)-1):
			give_time(((i*2)+1),period_times[i])
		print('lunch time: {} - {}'.format(lunch_time[0],lunch_time[1]))
	elif day == 3:
		for i in range(len(period_times)-1):
			give_time((i+1)*2,period_times[i])
		print('lunch time: {} - {}'.format(lunch_time[0],lunch_time[1]))
def time_left(period_times):
	lunch_time = period_times[-1]
	for i in range(len(period_times)-1):
			return check_time(period_times[i])
#24 hour time
#time layout: [['start time','end time'],['start time','end time']]
#example
#checks if it a wensday or thursaday
if dt.weekday() == 2:
	check_block([['7:25','8:55'],['8:59','10:24'],['10:58','12:23'],['12:27','20:52'],['10:25','10:54']],2)
elif dt.weekday() == 3:
	check_block([['7:25','8:55'],['8:59','10:24'],['10:58','12:23'],['12:27','13:52'],['10:25','10:54']],3)
else:
	print(time_left([['7:25','8:07'],['08:11','08:58'],['09:02','09:44'],['09:48','10:30'],['11:04','11:46'],['11:50','12:32'],['12:36','13:18'],['13:22','14:05'],['10:30','11:00']]))
