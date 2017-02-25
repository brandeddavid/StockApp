import re

from urllib import request

#GOOGLE FINANCE search url https://www.google.com/finance?q=

while True:
    
    try:
        url = "https://www.google.com/finance?q="
        
        stock = input("Enter Stock: ")
        
        url = url + stock.upper()
        
        data = request.urlopen(url).read()
        
        data = data.decode("utf-8")
        
        m = re.search('<meta itemprop="price"', data)
        
        start = m.start()
        
        end = m.end()
        
        data1 = data[end:end+50]
        
        s = re.search('content="', data1)
        
        start = s.start()
        
        end = s.end()
        
        data2 = data1[end:end+10]
        
        f = re.search('/', data2)
        
        price = data2[:f.end()-3]
                      
        print("The Stock Price for " + stock.upper() + " is $" + str(price))
    
    except:
        
        print("Stock Not Found")