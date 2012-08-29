import os
import sys
vcprojs = []
slns = []
def scan_folder(f):
	for root, subFolders, files in os.walk(f):
		for file in files:
			if file.endswith('.vcproj'):
				vcprojs.append(os.path.join(root,file))
			if file.endswith('.sln'):
				slns.append(os.path.join(root,file))
		for file in subFolders:
			scan_folder(os.path.join(root,file))

def replace_in_file(f, frm, to):
	with open(f, "r") as sources:
		lines = sources.readlines()
	with open(f, "w") as sources:
		for line in lines:
			sources.write(line.replace(frm, to))
	print "Replaced %s => %s in %s"%(frm, to, f)

if len(sys.argv) < 2:
	print "Invalid sytax: python %s <version>"%sys.argv[0]
	os.exit(1)

if sys.argv[1] == "2005":
	target_vc = '8.00'
	target_sln = '09.00'
elif sys.argv[1] == "2008":
	target_vc = '9.00'
	target_sln = '10.00'
else:
	print "Invalid version: %s"%sys.argv[1]
	os.exit(1)
	
scan_folder(os.getcwd())
for f in vcprojs:
	replace_in_file(f, 'Version="9.00"', 'Version="%s"'%target_vc)
	replace_in_file(f, 'Version="8.00"', 'Version="%s"'%target_vc)
	replace_in_file(f, 'Version="7.10"', 'Version="%s"'%target_vc)
	
for f in slns:
	replace_in_file(f, 'Microsoft Visual Studio Solution File, Format Version 10.00', 'Microsoft Visual Studio Solution File, Format Version %s'%target_sln)
	replace_in_file(f, 'Microsoft Visual Studio Solution File, Format Version 09.00', 'Microsoft Visual Studio Solution File, Format Version %s'%target_sln)
	replace_in_file(f, 'Microsoft Visual Studio Solution File, Format Version 08.00', 'Microsoft Visual Studio Solution File, Format Version %s'%target_sln)
