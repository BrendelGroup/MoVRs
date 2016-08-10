#this script takes consensus motif as input and output homer motif
#!/usr/bin/env python
import os, argparse

class Consensus:
	def __init__(self,fileConsensus):
		self.fileConsensus = fileConsensus
	def readConsensus(self):
		with open(self.fileConsensus,"r") as fp:
			return self.ParseConsensus(fp)
	def ParseConsensus(self,fileConsensus):
		'''Get the motif name ,title and PWM'''
		motif_dic={}
		flag=False
		for line in fileConsensus:
			if line[:2]=="DE":
				flag=True
				pwm=""
				tab = line.split("\t")
				name = tab[1].split(" ")[0]
				thresh = tab[1].split(" ")[-1]
				title = ">DE\t"+name+"\t"+thresh
				continue
			if line[:2]=="XX":
				flag=False
				homer=title+pwm
				motif_dic[name]=homer
				continue
			if flag==True :
				tmp = line.split("\t")
				for i in range(4):
					pwm += tmp[i]+"\t"
				pwm += "\n"
		
		return motif_dic

###=======read motif consensus file and write output Homer file=========
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--consensus_file",required=True)
	parser.add_argument("-o","--homer_file",required=True)
	args=parser.parse_args()

	infile = Consensus(args.consensus_file)
	homer_dic = infile.readConsensus()

	with open(args.homer_file,"w") as fo:
		for key in homer_dic.keys():
			fo.write(homer_dic[key])
	fo.close()	

