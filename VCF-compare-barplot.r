library(ggplot2)
variant<-read.table("VCF-compare-stats.txt",row.names='Segment',header=T)

##only varinat##
trial <- matrix(c(459, 883, 25092, 56, 178, 4466, 82, 175, 3326, 69, 192, 4025, 121, 85, 4891, 22, 64, 2521, 74, 85, 3318, 20,7, 1171, 16, 98, 1620 ), nrow=3)
colnames(trial) <- c('Total', 'PB2','PB1','PA','HA','NP','NA','MP','NS')
rownames(trial) <- c('GATK', 'SAM','common')
trial.table <- as.table(trial)
trial
barplot(trial,beside=TRUE,legend=T,ylab='Number of Variants',xlab='Segment',col=c('skyblue','yellow','purple'))


##total variant##
total <- matrix(c(25551, 25975, 25092, 4522, 4644, 4466, 3408, 3501, 3326, 4094, 4217, 4025, 5012, 4976, 4891, 2543, 2585, 2521, 3392, 3403, 3318, 1191, 1178, 1171, 1636, 1718, 1620), nrow=3)
colnames(total) <- c('Total', 'PB2','PB1','PA','HA','NP','NA','MP','NS')
rownames(total) <- c('GATK', 'SAM','common')
total.table <- as.table(trial)
total
barplot(total,beside=TRUE,legend=T,ylab='Number of Variants',xlab='Segment',col=c('skyblue','yellow','green'))

##stacked barplot##
barplot(total,legend=T)

##t-test##
GATK<-total[1,]
SAM<-total[2,]

t.test(GATK,SAM, var.equal=T)
