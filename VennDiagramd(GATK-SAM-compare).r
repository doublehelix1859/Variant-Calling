install.packages("VennDiagram")
library("VennDiagram")

##Total
grid.newpage()
a1<-459 
a2<-889 
n12<-25092
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4
		
##Total - ave
grid.newpage()
a1<-0.96 
a2<-1.82
n12<-52.40
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##PB2
grid.newpage()
a1<-56 
a2<-178
n12<-4466
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##PB2 - ave
grid.newpage()
a1<-56 
a2<-178
n12<-4466
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##PB1
grid.newpage()
a1<-82 
a2<-175
n12<-3326
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##PA
grid.newpage()
a1<-69
a2<-192
n12<-4025
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##HA
grid.newpage()
a1<- 121
a2<- 85
n12<-4891
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##NP				
grid.newpage()
a1<-22
a2<- 64
n12<-2521
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##NA
grid.newpage()
a1<-74
a2<- 85
n12<-3318
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##MP		
grid.newpage()
a1<- 20
a2<-7
n12<-1171
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4

##NS		
grid.newpage()
a1<- 16
a2<-98
n12<-1620
area1<-a1+n12
area2<-a2+n12
draw.pairwise.venn(area1,area2,n12 , category = c("GATK", "SAM"), lty = "blank",fill = c("skyblue", "mediumorchid"))
t1<-(a1/area1)*100
t2<-(a2/area2)*100
t3<-(n12/area1)*100
t4<-(n12/area2)*100
t1
t2
t3
t4