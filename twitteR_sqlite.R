# load twitter library
library("twitteR")


# set up authentication
# you need to substitute these keys with your own

setup_twitter_oauth(consumer_key="QWxBzzr1r55FN7ZlyxFg1VgeG",
                    consumer_secret="ezDbcIStUkogt9ijnJfCGsFbz8wVc2p4VKBmBLXTODzjpoId55",
                    access_token="2805580770-TKHgMmd8jtuEpNBd1JbzducTifZfhZdUlF97U3z",   
                    access_secret="vENMVaRYYXYf1n4mvXeEJcoVPMae7PCMUim8uEEPQmi1q")



# Register the db with twitteR
# this will automatically load the RSQLite library, so you don't have to
# the single parameter is the file location of the sqlite file. It will
# create it if it does not exist

register_sqlite_backend("d:/data/ps_tweets.sqlite")


# Find some Tweets and store them in a table
#similar to th search_twitter function but includes a table name.
# Again created if needed and appends to otherwise

search_twitter_and_store("UKDataService", table_name = "UKDS", lang='en')

# Retrieve the table and put into a dataframe
tweets_table <- load_tweets_db(as.data.frame = TRUE, table_name = "UKDS")

