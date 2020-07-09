library(tidyverse)

df <- read_csv("andre.csv", col_names = TRUE)

df<- filter(df, Year !=1976)
df<- filter(df, Year < 1994)

ggplot(data=df, aes(df$H))+geom_histogram()
