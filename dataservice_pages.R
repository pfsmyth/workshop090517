# The jsonlite library contains the functions we will use  to process the JSON
library(jsonlite)

#Loading and saving the ukdataservice home page

#This is the API call we are going to make
lookup <- "https://www.ukdataservice.ac.uk/"


rd <- readLines(lookup, warn = "F")

fileConn<-file("ukdataservice.html")
writeLines(rd, fileConn)
close(fileConn)


#Loading and saving a ukdataservice blog page

#This is the API call we are going to make
lookup <- "http://blog.ukdataservice.ac.uk/ethics-and-the-alleged-misuse-of-social-media-data/"


rd <- readLines(lookup, warn = "F")

fileConn<-file("blog.html")
writeLines(rd, fileConn)
close(fileConn)

# what is the type of rd

print(typeof(rd))  

# what is in rd?
rd
