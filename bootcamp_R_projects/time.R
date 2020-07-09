Sys.time()

myTime()

start<-myTime()
runsum<-0
for(i in 1:100000){
  runsum<-runsum+i
}


finish<-myTime()
ttime=finish-start
cat("The sum was ",runsum)
cat("it took ",ttime," seconds to complete the task")



myTime <- function(){
  Sys.time()
}