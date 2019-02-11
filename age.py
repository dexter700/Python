import datetime
now = datetime.datetime.now()
dob=input("Enter Your DATE-OF-BIRTH: ")
sd=dob.split("-")
if len(sd[0]) <2 or len(sd[0])>2 or int(sd[0])<1 or int(sd[0])>31:
	print("Month should be 2 digit long between 01-31")
elif len(sd[1])<2 or len(sd[1])>2 or int(sd[1])<1 or int(sd[1])>12:
	print("Month should be 2 digit between (01-12)")
elif len(sd[2])<4 or len(sd[2])>4 or int(sd[2])>now.year:
	print("Year should be 4 digit long less than %d" %(now.year))
else:
	print("=================Age calculator===============")
	#start
	y=now.year-int(sd[2])
	if(now.day >  int(sd[0])):
		d=now.day-int(sd[0])
	else:
		d=int(sd[0])-now.day

	if(now.month > int(sd[1])):
		m=now.month-int(sd[1])
	else:
		m=int(sd[1])-now.month

	print(y)
	print(d)
	print(m)
	#end
