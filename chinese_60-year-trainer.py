#!/usr/bin/env python3

# heavenly stems 天干 tian1gan1 tiāngān
# 
# jiǎ
# yǐ
# bǐng
# dīng
# wù
# jǐ
# gēng
# xīn
# rén
# guǐ
# 

# earthly branches 地支 dìzhī
# 
# zǐ
# chǒu
# yín
# mǎo
# chén
# sì
# wǔ
# wèi
# shēn
# yǒu
# xū
# hài


heavenlyStemsDict = {
     1:["甲","jiǎ"],
     2:["乙","yǐ"],
     3:["丙","bǐng"],
     4:["丁","dīng"],
     5:["戊","wù"],
     6:["己","jǐ"],
     7:["庚","gēng"],
     8:["辛","xīn"],
     9:["壬","rén"],
     10:["癸","guǐ"]
}


earthlyStemsDict = {
     1:["子","zǐ"],
     2:["丑","chǒu"],
     3:["寅","yín"],
     4:["卯","mǎo"],
     5:["辰","chén"],
     6:["巳","sì"],
     7:["午","wǔ"],
     8:["未","wèi"],
     9:["申","shēn"],
     10:["酉","yǒu"],
     11:["戌","xū"],
     12:["亥","hài"]
}


class EncodedNumber:
    def __init__(self, rawNumber):
        rawHeaven = int(rawNumber)
        rawEarth = int(rawNumber)
        self.raw = rawNumber
        while rawHeaven > 10:
            rawHeaven = rawHeaven - 10
        self.heaven = heavenlyStemsDict[rawHeaven]
        while rawEarth > 12:
            rawEarth = rawEarth - 12
        self.earth = earthlyStemsDict[rawEarth]




# get user input and turn the input string into an integer
print("Hello and welcome to our training program for the Chinese 60-year calendar\n We are going to start with a very simple recall exercise.")

while True:
    try:
        arabicNumber = int(input("Please input an Arabic Number in the 1 to 60 range and write down the corresponding Chinese characters. Hit ENTER when you are finished.\n"))
        break
    except ValueError:
        print("This was not a number!")

target = EncodedNumber(arabicNumber)


input("Written down the characters? To see the solution, hit ENTER!\n")

print (target.heaven[0],target.earth[0], sep = '')

pOrEnter = input("[press p to see pinyin, ENTER to continue]\n")
if pOrEnter == "p":
    print(target.heaven[1],target.earth[1],"\n\n", sep = '') 

feedbackValues = [1,2,3,4]
    
while True:
   try:
       feedbackNumber = input("Please type 3 if your solution was correct, 1 if only the first character was correct, 2 if only the second characer was correct, and 3 if you just had no clue whatsoever.")
       feedbackValue = int(feedbackNumber)
       break
   except ValueError:
       print("Not a number!")

if feedbackValue in feedbackValues:
    if feedbackValue == 3:
        print("Great job!")
    if feedbackValue == 2:
       print("You are getting there!")
    if feedbackValue == 1:
       print("You are getting there!")    
    if feedbackValue == 4:
       print("Oh boy!")    
else:
   print("all good?")




      
