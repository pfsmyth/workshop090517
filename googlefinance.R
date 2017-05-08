# The jsonlite library contains the functions we will use  to process the JSON
library(jsonlite)

#This is the API call we are going to make
lookup <- "https://finance.google.com/finance/info?client=nasdaq&q=AAPL"


rd <- readLines(lookup, warn = "F")
rd
