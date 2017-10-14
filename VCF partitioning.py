(1.SAM-BCF PB2)
#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=24:00:00
#SBATCH --mem=20GB
#SBATCH --job-name=variantsPart
#SBATCH --mail-type=END
#SBATCH --mail-user=mk6134@nyu.edu
#SBATCH --output=slurm_%j.out
#SBATCH --error=readmeSAM-partition.err

/bin/mk6134
/bin/scratch/mk6134/mirella107

cd /scratch/mk6134/mirella107

module load pyvcf/intel/0.6.8
module load pysam/intel/0.10.0
python


python 
import pysam
import vcf
execfile("")

(SAM-BCF)
(PB2)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.PB2.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PB2" and 0 < record.POS < 2281:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
(PB1)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.PB1.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PB1" and 0 < record.POS < 2275:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
(PA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.PA.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PA" and 0 < record.POS < 2152:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
(HA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.HA.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "HA" and 0 < record.POS < 1701:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
(NP)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.NP.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NP" and 0 < record.POS < 1498:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
				
(NA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.NA.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NA" and 0 < record.POS < 1411:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
				
(MP)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.MP.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "MP" and 0 < record.POS < 983:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
				
(NS)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".SAM-BCF.flt.vcf",'r'))
	with open(str(i)+".SAM-BCF.flt.NS.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NS" and 0 < record.POS < 839:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')

(GATK)
(PB2)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.PB2.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PB2" and 0 < record.POS < 2281:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
(PB1)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.PB1.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PB1" and 0 < record.POS < 2275:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
(PA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.PA.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "PA" and 0 < record.POS < 2152:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
(HA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.HA.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "HA" and 0 < record.POS < 1701:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
(NP)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.NP.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NP" and 0 < record.POS < 1498:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
				
(NA)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.NA.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NA" and 0 < record.POS < 1411:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
				
(MP)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.MP.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "MP" and 0 < record.POS < 983:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')
				
(NS)
for i in range(1,108):
	vcf_reader = vcf.Reader(open("/scratch/mk6134/mirella107/"+str(i)+".GATK_flt_variants.vcf",'r'))
	with open(str(i)+".GATK_flt_variants.NS.txt",'w') as f:
		for record in vcf_reader:
			if record.CHROM == "NS" and 0 < record.POS < 839:
				f.write(record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT)+'\t'+str(record.QUAL)+'\t'+str(record.FILTER)+'\n')

				
#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=24:00:00
#SBATCH --mem=20GB
#SBATCH --job-name=GATKvarcall
#SBATCH --mail-type=END
#SBATCH --mail-user=mk6134@nyu.edu
#SBATCH --output=slurm_%j.out

