#p3) write into a file
import os
filename = input("enter file name to write ninto ")
if os.path.isfile(filename):
	f = None
	try:
		f = open(filename, "a")
		data = input(" enter data to written ") 
		f.write(data + "\n")
	except Exception as e:
		print("issue", e)
	finally:
		if f is not None:
			f.close()
else:
	print(filename ," does not exists ")