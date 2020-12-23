#!/usr/bin/env python3

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
# print("Please input the Arabic Number You want to convert.")
# print("Please input an Arabic Number in the 1 to 12 range and write down the corresponding Chinese characters.")






# arabic_number = int(input("Please input an Arabic Number in the 1 to 60 range and write down the corresponding Chinese characters.Hit ENTER when you are finished.\n"))

while True:
    try:
        arabicNumber = int(input("Please input an Arabic Number in the 1 to 60 range and write down the corresponding Chinese characters. Hit ENTER when you are finished.\n"))
        break
    except ValueError:
        print("This was not a number!")

target = EncodedNumber(arabicNumber)

# arabic_number = int(raw_input())
# arabic_number = int(input()) # python 3 version of raw_input
# print()
# introduce two separate variables for the heavenly stem and the earthly branches
# heaven_stem = arabic_number
# earth_branch = arabic_number


input("Written down the character? To see the solution, hit ENTER!\n")

# # loop until the correct integers for the mapping on the characters are available
# while heaven_stem > 10:
#  heaven_stem = heaven_stem - 10
# # print (heaven_stem) # just for error checking
# while earth_branch > 12:
#  earth_branch = earth_branch - 12
# # print (earth_branch) # just for error checking

# map the integers on the character strings

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


# # first the heavenly stems
# # if heaven_stem == 1:
# #  heaven_stem_character = u'甲'.encode('utf8')
# if heaven_stem == 1:
#  heaven_stem_character = '甲'
# if heaven_stem == 2:
# # heaven_stem_character = u'乙'.encode('utf8')
#  heaven_stem_character = '乙'
# if heaven_stem == 3:
# # heaven_stem_character = '丙'.encode('utf8')
#  heaven_stem_character = '丙'
# if heaven_stem == 4:
# # heaven_stem_character = u'丁'.encode('utf8')
#  heaven_stem_character = '丁'
# if heaven_stem == 5:
# # heaven_stem_character = u'戊'.encode('utf8')
#  heaven_stem_character = '戊'
# if heaven_stem == 6:
# # heaven_stem_character = u'己'.encode('utf8')
#  heaven_stem_character = '己'
# if heaven_stem == 7:
# # heaven_stem_character = u'庚'.encode('utf8')
#  heaven_stem_character = '庚'
# if heaven_stem == 8:
# # heaven_stem_character = u'辛'.encode('utf8')
#  heaven_stem_character = '辛'
# if heaven_stem == 9:
# # heaven_stem_character = u'壬'.encode('utf8')
#  heaven_stem_character = '壬'
# if heaven_stem == 10:
# # heaven_stem_character = u'癸'.encode('utf8')
#  heaven_stem_character = '癸'
# 
# # second the earthly branches
# if earth_branch == 1:
# # earth_branch_character = u'子'.encode('utf8')
#  earth_branch_character = '子'
# if earth_branch == 2:
# # earth_branch_character = u'丑'.encode('utf8')
#  earth_branch_character = '丑'
# if earth_branch == 3:
# # earth_branch_character = u'寅'.encode('utf8')
#  earth_branch_character = '寅'
# if earth_branch == 4:
# # earth_branch_character = u'卯'.encode('utf8')
#  earth_branch_character = '卯'
# if earth_branch == 5:
# # earth_branch_character = u'辰'.encode('utf8')
#  earth_branch_character = '辰'
# if earth_branch == 6:
# # earth_branch_character = u'巳'.encode('utf8')
#  earth_branch_character = '巳'
# if earth_branch == 7:
# # earth_branch_character = u'午'.encode('utf8')
#  earth_branch_character = '午'
# if earth_branch == 8:
# # earth_branch_character = u'未'.encode('utf8')
#  earth_branch_character = '未'
# if earth_branch == 9:
# # earth_branch_character = u'申'.encode('utf8')
#  earth_branch_character = '申'
# if earth_branch == 10:
# # earth_branch_character = u'酉'.encode('utf8')
#  earth_branch_character = '酉'
# if earth_branch == 11:
# # earth_branch_character = u'戌'.encode('utf8')
#  earth_branch_character = '戌'
# if earth_branch == 12:
# # earth_branch_character = u'亥'.encode('utf8')
#  earth_branch_character = '亥'

# print (heaven_stem_character,earth_branch_character, sep = '')
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

# if feedbackNumber in feedbackValues:
#     print("Thanks")   
# if feedbackNumber not in feedbackValues:
#     print("Please choose 1,2,3, or 4")



      
