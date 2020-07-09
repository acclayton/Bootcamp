{
shoppinglist<-list()

x<- readline(prompt="What item do you want on your Shopping list?")


while(x!='Quit'){
  shoppinglist<-append(shoppinglist,x)
  x<-readline(prompt="What else do you want to buy? (type Quit to stop)")
}
}

for (x in shoppinglist){
  print(x)
}
