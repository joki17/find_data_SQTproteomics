import csv 
import os

#input file should be in same path as cwd, or else manually change fhand file path. 
print (os.getcwd())
dir_path = os.getcwd()

fhand = open(dir_path+'/HTMLcontains_Data.txt')

NSAF_list = []
geneName_list = []
geneSymbol_list = []

for line in fhand: 
    new_line = line.rstrip() 
    
    last_found_dfn = -1
    while True:

    	#find <dfn> tags in file, where only the titles of genes are with NSAFs and other info
    	last_found_dfn = new_line.find('<dfn>', last_found_dfn + 1)

    	if last_found_dfn == -1:
    		break
    	else:
    		
    		#make string containing the titles of genes are with NSAFs and other info
    		end_info = new_line.find('PE=', last_found_dfn + 1)
    		start_info = new_line.find('</a>', last_found_dfn - 100)

    		info = new_line[start_info : end_info]
    		#print(info)

    		#find all indexes of t char
    		inds = [i for i,c in enumerate(info) if c == 't']

    		#get NSAF, always between the 7th and 8th t tabs
    		NSAF = info[inds[7] + 3 : inds[8] - 2]
    		print('NSAF : ', NSAF)

    		NSAF_list.append(NSAF)

    		#get gene name
    		end_gene = info.find('OS=')
    		start_gene = info.find('<dfn>')
    		gene_name = info[start_gene + 5 : end_gene] 
    		print ('Gene name : ' , gene_name)

    		geneName_list.append(gene_name)

    		#get gene symbol
    		start_geneSymbol = info.find('GN=')
    		geneSymbol = info[start_geneSymbol + 3 : end_info] 
    		print ('Gene symbol : ', geneSymbol)

    		geneSymbol_list.append(geneSymbol)


download_dir = "test_proteomics.csv" #where you want the file output to be downloaded to 


rows = zip(geneName_list, geneSymbol_list, NSAF_list)
with open(download_dir,'w') as csvfile:
    mywriter = csv.writer(csvfile, dialect='excel')

    for row in rows:
    	mywriter.writerow(row)


fhand.close()