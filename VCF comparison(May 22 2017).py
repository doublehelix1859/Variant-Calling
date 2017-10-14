STEP 0. Indexing reference
	pwd: home/mk6134
	dir: home/mk6134/testrun/rawfiles2
	module: bwa/gnu/0.7.13
	command: bwa index h3n2.fa
	input: h3n2.fa(FASTA reference)
	output: h3n2.fa.ann  h3n2.fa.pac h3n2.fa.amb  h3n2.fa.bwt  h3n2.fa.sa
STEP 5.5.1 Indexing the ref(FASTA)
	pwd: home/mk6134
	directory: home/testrun/rawfiles2
	module: samtools/intel/1.3
	commands: samtools faidx h3n2.fa
	output: h3n2.fa.fai
	
	STEP 5.5.2 Creating dictionary file
	pwd: home/mk6134
	directory: home/mk6134/testrun/rawfiles2
	module: picard-tools/1.129
	input: h3n2.fa(reference FASTA file)
	command: java -jar /share/apps/picard-tools/1.129/picard.jar CreateSequenceDictionary R= h3n2.fa O= h3n2.dict
	output: h3n2.dict
	getting info: https://software.broadinstitute.org/gatk/documentation/article?id=1601

(modifying column values)
up vote
6
down vote
accepted
awk '{ $3 -= 2; print }' filename >new_filename 
Or, if you really only want to touch 3's and 4's:

awk '{ if ( $3 == 3 ) { $3 = 1 } else if ( $3 == 4 ) { $3 = 2 }; print}' filename >new_file

((partitioning segment by segment))

>>> vcf_reader=vcf.Reader(open("/scratch/mk6134/mirella107/1.SAM-BCF.flt.vcf"))
>>> with open("1.SAM-BCF.flt.PB2.txt",'w') as f:
...     for record in vcf_reader:
...             if record.CHROM=="PB2":
...                     f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')

vcf_reader=vcf.Reader(open("/scratch/mk6134/mirella107/1.SAM-BCF.flt.PB2.txt",'w'))
with open("1.SAM-BCF.flt.PB2.txt",'w') as f:
	for record in vcf_reader[3]:
	