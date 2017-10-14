(file size bash)
ls -n file.txt


grep -Fx -f file1 file2
'''intersection between the two files'''

sort file1 file2 | uniq -d

'''lines in file2 that are not in file1'''
grep -Fxv -f file1 file2

(GATK only entire)
filename: GATK-entire-only.sh

#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=24:00:00
#SBATCH --mem=20GB
#SBATCH --job-name=GATK-entire-only
#SBATCH --mail-type=END
#SBATCH --mail-user=mk6134@nyu.edu
#SBATCH --output=slurm_%j.out
#SBATCH --error=GATK-entire-only.err

cd /scratch/mk6134/mirella107
for i in {1..107}; do
grep -Fxv -f $i.SAM-BCF.flt.prt.txt $i.GATK_flt_variants.prt.txt > $i.GATK-entire-only.txt
done

(SAM only entire)
filename: SAM-entire-only.sh
#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=24:00:00
#SBATCH --mem=20GB
#SBATCH --job-name=SAM-entire-only
#SBATCH --mail-type=END
#SBATCH --mail-user=mk6134@nyu.edu
#SBATCH --output=slurm_%j.out
#SBATCH --error=SAM-entire-only.err

cd /scratch/mk6134/mirella107
for i in {1..107}; do
grep -Fxv -f $i.GATK_flt_variants.prt.txt $i.SAM-BCF.flt.prt.txt  > $i.SAM-entire-only.txt
done

(making a loop)
(intersection)
#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=24:00:00
#SBATCH --mem=20GB
#SBATCH --job-name=GATK-SAM-intersect
#SBATCH --mail-type=END
#SBATCH --mail-user=mk6134@nyu.edu
#SBATCH --output=slurm_%j.out
#SBATCH --error=GATK-SAM-intersect.err

cd /scratch/mk6134/mirella107

for i in {1..107};do
for j in {'PB2','PB1','PA','HA','NP','NA','MP','NS'};do
grep -Fx -f $i.GATK_flt_variants.$j.prt.txt $i.SAM-BCF.flt.$j.prt.txt > $i.GATK-SAM.$j.intersect.txt
done

(SAM only)
#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=24:00:00
#SBATCH --mem=20GB
#SBATCH --job-name=SAMonly
#SBATCH --mail-type=END
#SBATCH --mail-user=mk6134@nyu.edu
#SBATCH --output=slurm_%j.out
#SBATCH --error=SAMonly.err

cd /scratch/mk6134/mirella107

for i in {1..107}; do
for j in {'PB2','PB1','PA','HA','NP','NA','MP','NS'};do
grep -Fxv -f $i.GATK_flt_variants.$j.prt.txt $i.SAM-BCF.flt.$j.prt.txt > $i.SAM.$j.only.txt
done

(GATK only)
#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=24:00:00
#SBATCH --mem=20GB
#SBATCH --job-name=GATKonly
#SBATCH --mail-type=END
#SBATCH --mail-user=mk6134@nyu.edu
#SBATCH --output=slurm_%j.out
#SBATCH --error=GATKonly.err

cd /scratch/mk6134/mirella107

for i in {1..107}; do
for j in {'PB2','PB1','PA','HA','NP','NA','MP','NS'};do
grep -Fxv -f $i.SAM-BCF.flt.$j.prt.txt $i.GATK_flt_variants.$j.prt.txt > $i.GATK.$j.only.txt
done