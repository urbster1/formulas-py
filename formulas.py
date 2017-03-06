import sys,os,re,itertools
import mingus.core.notes as notes
def shift(l,n):
    return itertools.islice(itertools.cycle(l),n,n+len(l))
formulas = []
root = ""
if len(sys.argv) == 2:
	root = sys.argv[1]
	if (root.find("b") > -1 or root == "F"):
		flat = 1
	else:
		flat = 0
try:
	rootval = notes.note_to_int(root)
except:
	root = "0"
	rootval = 0
	flat = 0
if rootval > 0:
	listorder = list(shift([0,1,2,3,4,5,6,7,8,9,10,11],rootval))
	listorder = listorder[1:]
else:
	listorder = [1,2,3,4,5,6,7,8,9,10,11]
if not root == "0":
	print('Sets using ' + root + ' as root\n1-note set\n' + root)
	for x in range(1,12):
		formulas = itertools.combinations(listorder,x)
		if x < 11:
			print(str(x+1) + "-note sets")
		else:
			print(str(x+1) + "-note set")
		for f in formulas:
			notelist = []
			for note in f:
				if flat == 1:
					notelist.append(notes.int_to_note(note, 'b'))
				else:
					notelist.append(notes.int_to_note(note))
			print(root + '\t' + '\t'.join(notelist))
		if x < 11:
			input("Press Enter to continue")
else:
	root = "1"
	print('Generating formulas\n1-note formula\n' + root)
	listorder = ['b2','2','b3','3','4','b5','5','b6','6','b7','7']
	for x in range(1,12):
		formulas = itertools.combinations(listorder,x)
		if x < 11:
			print(str(x+1) + "-note formulas")
		else:
			print(str(x+1) + "-note formula")
		for f in formulas:
			print(root + '\t' + '\t'.join(f))
		if x < 11:
			input("Press Enter to continue")
