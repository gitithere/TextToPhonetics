#
# All credit to Kevan Stannard dinopass website: http://www.dinopass.com
# Awesome password generator for kids
#
import urllib2
import time
count=0
count = raw_input('Enter number of times to generate a password: ')
count = int(count)
print " "
#except (TypeError, ValueError, NameError):
#             print('Oops! Invalid String Entered')
#             break
#except KeyboardInterrupt:
#             break
#else:
#
while (count > 0):
        response = urllib2.urlopen('http://www.dinopass.com/password/strong')
        html = response.read()
        print 'This is from Kevan Stannard-DinoPass strong password website: ' + html
#while True:
        try:
                dictionary = {']':']BRACKET]', '[':'[BRACKET[', '<':'<LESS_THAN<', '@':'@AT_SIGN@', '$':'$DOLLAR_SIGN$', '!':'!BANG!', ')':')PARENS)', '(':'(PARENS(','+':'+PLUS_SIGN+', '1':'#ONE#', '2':'#TWO#', '3':'#THREE#', '4':'#FOUR#','5':'#FIVE#', '6':'#SIX#', '7':'#SEVEN#', '8':'#EIGHT#', '9':'#NINE#', '0':'#ZERO#', 'a':'alpha',  'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliet', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa','q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu', 'A':'ALPHA', 'B':'BRAVO','C':'CHARLIE', 'D':'DELTA', 'E':'ECHO','F':'FOXTROT', 'G':'GOLF',"H":"HOTEL", 'I':'INDIA', 'J':'JULIET', 'K':'KILO','L':'LIMA', 'M':'MIKE', 'N':'NOVEMBER', 'O':'OSCAR', 'P':'PAPA', 'Q':'QUEBEC', 'R':'ROMEO', 'S':'SIERRA', 'T':'TANGO', 'U':'UNIFORM', 'V':'VICTOR', 'W':'WHISKEY', 'X':'X-RAY', 'Y':'YANKEE', 'Z':'ZULU'}
#                             inputtext = raw_input('Enter string to convert to phonetic: ')
        except (TypeError, ValueError, NameError):
               print('Oops! Invalid String Entered')
               break
        except KeyboardInterrupt:
               break
        else:
                print('phonetic alphabet: ' + ', '.join(map(dictionary.get,html)))
                count -= 1
                print " "
                print count
                print " "
                time.sleep(2) # delays for 2 seconds
                if int(count) == 0:
                        break
