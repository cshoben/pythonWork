import re

#if __name__ == '__main__':
####### number 1 ###############


print ('Answers question #1, see final CRS.A1.Numbers1_3')
print ('Have the file <UHRF1_promoter_region.txt> in the same folder as this script')

#open the motif sequence and read it. 
promoterseq = open('UHRF1_promoter_region.txt', 'r')

#create and open for writing to the assignment saved file. 
answers = open('CRS.A1.Numbers1_3', 'w')
answers.write('\n ANSWERS TO NUMBER 1 \n')

#read the newly opened line
firstline = promoterseq.read()
answers.write('The motif sequnence is: \n')
answers.write(firstline)
     
binding_site = re.findall('TTT[C,G][C,G]CGC', firstline)
answers.write('\n The binding site is: \n')
answers.write(str(binding_site))

#length/number
answers.write('\n The number of binding sites is: ') 
answers.write(str(len(binding_site)))
newline = '\n'
for A in binding_site:
	i = firstline.find(A)
	capture = ('One sequence is', A, 'at positions:', i,)
	answers.write(newline)
	answers.write(str(capture))
	answers.write(newline)

#################Q #2	####################
print ('Answers question #2, see final CRS.A1.Numbers1_3')
answers.write('\n ANSWERS TO NUMBER 2 \n')
print ('Have the file <E2F1_motif.txt> in the same folder as this script')

#open, readlines makes it a list, removed first item of list.
PWMmotif = open('E2F1_motif.txt', 'r')
PWM = PWMmotif.readlines()

pwm = PWM[1:]


#initialize my dictionary
pwm_dict = {}


for item in pwm:
	pwm_strip = item.strip().split('\t')	
	key = pwm_strip[0][0]
	value = [float(num) for num in pwm_strip[1:]]
	pwm_dict[key] = value
	

max_score = -1
max_position = -1

for i in range(len(firstline)-10):
	window = firstline[i:i+11]
	
	score = 1

	for (pos, base) in enumerate (window):
		score = score*pwm_dict[base][pos]
		
	if score > max_score:
		max_score = score
		max_position = i
	
best_sequence = ('The best E2F1 position is',firstline[max_position:max_position+11],)		
best_score =  ('With a score of',max_score)
best_position = ('At position',max_position)  

answers.write(newline)
answers.write(str(best_sequence))
answers.write(newline)
answers.write(str(best_score))
answers.write(newline)
answers.write(str(best_position))
answers.write(newline)



###############################################
print ('Answers question #3, see final CRS.A1.Numbers1_3')
### GOAL: Reading the ChIP-seq peaks, look for the E2F1 site. print to a file (# of sites in each sequence). Print # of sites in each peak that is >0
### LOOK ON BOTH STRANDS. 
## Compare number of peaks with site to number without. 
answers.write('\n ANSWERS TO NUMBER 3 \n')
print ('Have the file <E2F1_ChIPseq_peaks.fa> in the same folder as this script')
#define variables
linecounter = 0
numpeakswithsites = 0


HeLafasta = open( 'E2F1_ChIPseq_peaks.fa', 'r') #open file
HeLafastalines = HeLafasta.readlines()

#E2F1_sites_in_CHIP = open ('E2F1_sites_in_CHIP', 'w')

totalpeaks = len(HeLafastalines) / 2

for linereading in HeLafastalines:
	linecounter = linecounter + 1
#add one to the line counter, should line up that 1 = 1###
	if linecounter % 2 != 0: #if the line count is odd, since every other line we want to read
		#print ('odd line')
		#E2F1_sites_in_CHIP.write(linereading)
		peak = linereading
		

	if linecounter % 2 == 0: #if line is even, could of used else:
		#print ('even line')
		sites_in_peak = re.compile('TTT[C,G][C,G]CGC|GCG[G,C][G,C]AAA')
		num_sites_in_peak = len(sites_in_peak.findall(linereading))
		#E2F1_sites_in_CHIP.write(str(num_sites_in_peak), '\n')
		if (num_sites_in_peak>0):
			numpeakswithsites = numpeakswithsites + 1
			str1 = "The peak "+ peak.strip()
			str2 = 'contains '+ str(num_sites_in_peak)+ ' number of sites \n'
			answers.write(str1)
			answers.write(str2)
			
numpeak_write = 'There are a total of', numpeakswithsites, 'peaks containing TTTSSCGC or GCGSSAAA'
	
percentageoffasta = 100 * (float(numpeakswithsites) / totalpeaks)		
percent_write = 'The percentage of peaks was ', percentageoffasta

answers.write(newline)
answers.write(str(numpeak_write))
answers.write(newline)
answers.write(str(percent_write))
answers.write(newline)	
answers.write('I define this as a low number of peaks if the peaks are supposed to be specific to E2F1 \n')

################################################################

print ('Answers to # 4, see file wgEncode.fa')
print ('Have the files for the human genome chromosomes from HG19 in the same folder as this script is executed.')

ENCODEdata = open('wgEncodeSydhTfbsHelas3E2f1StdPk.narrowPeak', 'r')
readENCODE = ENCODEdata.readlines()

writepeakseq = open('wgEncode.fa', 'w')
linecounter=0


for lines in readENCODE:
	if linecounter < 5:
		linecounter = linecounter + 1
		writepeakseq.write('>' + lines) #write the line/peak name to new file
		linescut = lines.split()
		#print ('First item on each line is ',linescut[0])
		currentchr = linescut[0]
		filechrname = currentchr + '.fa'
		#print ('The file name I am trying to access is ',filechrname)
		
		#print ('The zero-based start position is ',linescut[1])
		#print ('The zero-based end position is   ', linescut[2])
		beginseq = (int(linescut[1]))
		#print ('We are going to begin counting from ', beginseq)
		
		endseq = int(linescut[2])
		
		openchrfile = open(filechrname, 'r+')
		#print (openchrfile.read(10))
		chrseq_list = openchrfile.readlines()
		chrseq_onlyseq = chrseq_list[1:]
		#print (type(chrseq_list))
		
		
		#for manyseqlines in chrseq_list:
			#manyseqlines.replace('\n', '')
				#manyseqlines.rstrip()
				#linecountseq = linecountseq + 1
				
		chrseq_no_carriage_list = [i.replace('\n','') for i in chrseq_onlyseq]
		
		chrseq_string = ''.join(chrseq_no_carriage_list)
		
		sequencecapture = chrseq_string[beginseq:endseq]
		writepeakseq.write(sequencecapture + '\n')
	else:
		break
print ('done')
#print ('We found the sequence for ',linecounter, 'peaks')
