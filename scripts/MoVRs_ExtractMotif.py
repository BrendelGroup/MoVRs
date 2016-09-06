#!/usr/bin/env python
import argparse,math,re

#ParseMEME parses a multi-motif input file (MEME-formatted) into a dictionary
#with key the motif name and value a string containg all the content for this
#motif.
#The other functions support the optional culling of the motif list by evalue
#threshold, number of motifs, or specified motif names.


def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

def sorted_by_evalue( l ):
	tmp_list={}
	for key in l.keys():
		motif=l[key]
		lines=motif.split('\n')
		second=lines[1].strip()
		E_value=second.split('E=')[1].strip()
		E_value=float(E_value)
		tmp_list[key]=E_value
	tmp_sorted=sorted(tmp_list.items(),key=lambda x: x[1])
        tmp_return = [x[0] for x in tmp_sorted]
	return tmp_return

def ParseMEME(MotifFile):
	with open(MotifFile,'r') as fileMEME:
		content = fileMEME.read()
	motif_list = {}
	tabs = content.split('MOTIF')
	for i in range(1,len(tabs)):
		current = tabs[i]
		title = 'MOTIF'+ current.split('\n')[0]
		name = title.split(' ')[1]
		tmp = current.split('\n')[0]+'\n'
		motif = current.replace(tmp,'')
		motif_list[name] = title + '\n' + motif
	return motif_list

#check_threshold: return true when E-value is less than threshold
def check_threshold(motif,threshold):
	lines = motif.split('\n')
	second = lines[1].strip()
	E_value = second.split('E=')[1].strip()
	E_value = float(E_value)
	if E_value == 0:
		return True
	if math.log(E_value/threshold)<=0: 
		return True

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--motif_MEME',required=True)
	parser.add_argument('-t','--motif_threshold')
	parser.add_argument('-k','--keepnmotifs')
	parser.add_argument('-n','--motif_name')
	parser.add_argument('-o','--out_file',required=True)
	args = parser.parse_args()

	motif_list = ParseMEME(args.motif_MEME)

	#extract motifs according to threshold
	if args.motif_threshold:
		threshold = float(args.motif_threshold)
		for key in list(motif_list):
			content = motif_list[key]
			if not check_threshold(content,threshold):
				del motif_list[key]

	#extract top n motifs (by evalue ranking)
	if args.keepnmotifs:
                mylist = sorted_by_evalue( motif_list )
		keepn = float(args.keepnmotifs)
		i = 0
		for key in list(mylist):
                    i += 1
		    if i > keepn:
			del motif_list[key]

	#extract motifs according to motif names in motif_name file
	if args.motif_name:
		with open(args.motif_name,'r') as fileName:
			i = 0
			for line in fileName:
				line="".join(line.split())
				line = line.replace("'","")
				i += 1
				output = 'Group'+str(i)
				tmp = line.strip()
				tab = tmp[1:-1].split(',')#the list of motif names for each group
		with open(args.out_file,'w') as ofile:
			ofile.write("MEME version 4\n"+"ALPHABET= ACGT\n\n")
			for each in tab:
				content = motif_list[each]
				ofile.write(content)
	else:
		with open(args.out_file,'w') as ofile:
			ofile.write('MEME version 4\n'+"ALPHABET= ACGT\n\n")
			mykeys = sorted_nicely(motif_list.keys())
			for each in mykeys:# the motif name in each group
 				content = motif_list[each]
 				ofile.write(content)
