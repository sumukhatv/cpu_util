import time
import string
import sys
import commands

def get_cpu_usage(proc):
	for entry in commands.getoutput("ps aux").split("\n"):
		if (proc in entry.split()[10]):
			return float(entry.split()[2])
	return 0.0

def usage():
	print "usage: python proc_cpu_usage.py <interval seconds> <process name> <output filename>"
	return

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		if (sys.argv[1] == "-h"):
			usage()
			exit(0)
	
	if (len(sys.argv) == 4):
		f = open(sys.argv[3], "w")
		print("%CPU")
    		f.write("%CPU\n")
    		try:
        		while True:
            			load = get_cpu_usage(sys.argv[2])
            			if load:
            				print("%.2f" % (load))
					f.write("%.2f\n" % (load))
            			time.sleep(float(sys.argv[1]))
    		except KeyboardInterrupt:
        		exit(0)
	else:
		usage()
