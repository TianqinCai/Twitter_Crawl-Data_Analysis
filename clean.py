import string
punc = string.punctuation

candidates = ["AubichonMaynard","LetsFixHousing","gzlfb","Drpingchan","DavidChenTweets",
              "vancitycrime","Realfredharding","rollergirl2014","sshottha",
              "kensimformayor","kennedystewart","ShaunaSylvester","johnmyano","WaiYoung"]

for candidate in candidates:
    inputfilename = candidate
    outputfilename = candidate+"_withouthttp"
    outputfile = open(outputfilename+".txt","w")
    inputfile=open(inputfilename+".txt","r")
    
    for line in inputfile.readlines():
        ls = line.split()
        for item in ls:
            item = item.replace('b\'','')
            item = item.replace('b\"','')
            item = item.replace('b\"\'','')
            #first remove b', b", b"', then do then punctuation for cleaning
            item=item.translate(str.maketrans("","",punc))
            if(item.endswith("\'") or item.endswith("\"")):
                item = item[:-1]
            if not (item.startswith("http")):
                outputfile.write(item.lower()+" ")
        outputfile.write("\n")