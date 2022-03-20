#A quick thing to help me get used to and familiar with dictionaries :) 
#Notes: Keys have to be unique!! 

monthConversion = { 
    "Jan." : "January",
    "Feb." : "Fevruary",
    "Mar." : ",March",
    "Apr" : "April",
    "May" : "May",
    "Jun." : "June",
    "Jul." : "July",
    "Aug." : "August", 
    "Sep." :"September",
    "Oct." : "October",
    "Nov." : "November" ,
    "Dec." : "December"
    }
#diffrent ways to call it 
print (monthConversion["Jul."])

print (monthConversion.get("Dec."))



