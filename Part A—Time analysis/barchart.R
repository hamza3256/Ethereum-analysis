library(ggplot2)

df = read.table("/Users/hamza/Desktop/bigDataCW/partA/out_partA.txt",sep='\t')
names(df) = c('Date','Transaction')
df = df [df$Date != '1970-01',]
options(scipen=999)

ggplot(data = df, aes(x = Date, y = Transaction)) +
  geom_bar(stat = "identity", fill = "steelblue")+
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))
  
