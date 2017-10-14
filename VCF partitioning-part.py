(SAM-BCF)
(Entire)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.prt.txt",'w') as f:
		for record in vcf_reader:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(PB2)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.PB2.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PB2" and 0 < record.POS < 2281:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(PB1)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.PB1.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PB1" and 0 < record.POS < 2275:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(PA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.PA.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PA" and 0 < record.POS < 2152:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(HA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.HA.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "HA" and 0 < record.POS < 1701:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(NP)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.NP.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NP" and 0 < record.POS < 1498:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
				
(NA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.NA.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NA" and 0 < record.POS < 1411:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
				
(MP)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.MP.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "MP" and 0 < record.POS < 983:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
				
(NS)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.NS.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NS" and 0 < record.POS < 839:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')

(GATK)
(ALL)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.prt.txt",'w') as f:
		for record in vcf_reader:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(PB2)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.PB2.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PB2" and 0 < record.POS < 2281:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(PB1)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.PB1.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PB1" and 0 < record.POS < 2275:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(PA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.PA.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PA" and 0 < record.POS < 2152:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(HA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.HA.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "HA" and 0 < record.POS < 1701:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
(NP)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.NP.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NP" and 0 < record.POS < 1498:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
				
(NA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.NA.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NA" and 0 < record.POS < 1411:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
				
(MP)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.MP.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "MP" and 0 < record.POS < 983:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')
				
(NS)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.NS.prt.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NS" and 0 < record.POS < 839:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\n')