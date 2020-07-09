library(hunspell)


spellcheck<-function(){
  word<-readline("Type a word ")
  while (!hunspell_check(word)){
    word<-readline("Check your spelling and try again")
  }
  cat("Congratulations on spelling",word,"correctly")
}


getName<- function(){
  name<-readline(prompt="What is your name?")
  cat("Hello", name, "have a nice day")
}