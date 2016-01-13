# purpose : wordclout in R 

# initialisation
library(tm)
library(wordcloud)
library(RColorBrewer)
library(SnowballC)
library(sqldf)

# read the file and only keep comments row
comments <- read.csv("angry_birds_2_comments.csv")
comments <- comments[,3]

# data preparation
corpus <- Corpus(DataframeSource(data.frame(comments)))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, function(x) removeWords(x, stopwords("english")))
 
# compute freq
tdm <- TermDocumentMatrix(corpus)
m <- as.matrix(tdm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)

# Porter stemming
d$word <- wordStem(d$word, language = "porter")

# sum group words by freq
freq <- sqldf(" select word, sum(freq) as sum_freq
        from d 
        group by word
        order by 2 desc")

# only keep interesting words
df_freq <- subset(freq, subset = word %in% c("crash","fun","like","great","good",
                                             "rovio","love","wait","enjoy","addict","delet",
                                             "ruin","annoi","disappoint","bad","shame",
                                             "frustrat","hate","level","time"))
# wordcloud 
pal <- brewer.pal(9, "BuGn")
pal <- pal[-(1:2)]
png("angry.png", width=1280,height=800)
wordcloud(df_freq$word,df_freq$sum_freq, scale=c(8,.5), 
          random.order=F, colors=pal, vfont=c("sans serif","plain"))
dev.off()
