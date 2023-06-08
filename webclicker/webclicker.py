import webbrowser, time

url = input("URL>>")
while True:
	try:
		dur = int(input("Watch time>>"))
		break
	except:
		print("Number?")
while True:
	try:
		wtc = int(input("number of clicks>>"))
		break
	except:
		print("Number?")

for i in range(wtc):
	webbrowser.open_new(url)
	time.sleep(dur)