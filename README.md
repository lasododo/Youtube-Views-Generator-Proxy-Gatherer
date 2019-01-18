#Youtube Views Generator + Proxy gatherer

*THIS PROJECT IS AN OLD PROJECT OF MINE, SO IT CAN BE MESSY / NOT WORK AT ALL*

#Proxy Gatherer:

###ProxyGathering.py

All you have to do is start it (how to start it you will find at the end of this Readme)

What does program do in steps:
 1. Go to each website that it was programmed for
 2. Get the proxy IP
 3. Put proxy IP in text file

#Youtube Proxy views Generator:

###YoutubeProxyViewsGen.py

Amount - How many of them should run at a same time. 
( This program uses threading, which allows you to run multiple browsers at a same time. )
```
amount = 4
```
links - Add here links to videos you want to use views generator on.
```
links = [
    'https://www.youtube.com/......',
]
```

What program does in steps:
 1. Creates Browser from IP's gathered using `ProxyGathering.py`
 2. Opens youtube link from `links` ( works for all websites, not just Youtube)
 3. Opens `amount` browsers and waits around a minute and then closes all of them
  
##Requirements :
    Python 3.6 or higher
    Python libraries - Selenium

## After you install libraries:
    python ProxyGathering.py
    python YoutubeProxyViewsGen.py
    
-------------
This project was created for educational purposes.
  
  
  

