
# Python program to generate WordCloud 
  
# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

def printCloud(file):
    file_content=open (file).read()
    stopwords = set(STOPWORDS) 
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(file_content)                       
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    plt.show() 
    
# candidates = ["AubichonMaynard","LetsFixHousing","gzlfb","Drpingchan","DavidChenTweets",
#               "vancitycrime","Realfredharding","rollergirl2014","sshottha",
#               "kensimformayor","kennedystewart","ShaunaSylvester","johnmyano","WaiYoung"]
candidates = ["WaiYoung"]
for candidate in candidates:
    printCloud(candidate+"_withouthttp.txt")

# for val in file_content: 
    
#     # typecaste each val to string 
#     val = str(val) 
#     # split the value 
#     tokens = val.split() 
      
#     # Converts each token into lowercase 
#     for i in range(len(tokens)): 
#         tokens[i] = tokens[i].lower() 
          
#     for words in tokens: 
#         comment_words = comment_words + words + ' '