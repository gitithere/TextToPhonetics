#
# All credit to Kevan Stannard dinopass website: http://www.dinopass.com
# Awesome password generator for kids
# Added BOLD, CAPS, AND COLORS to passwords generated
import urllib2
import time
import sys
count=0
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m" 
print CYAN
print ' ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ '
print '||K |||e |||v |||a |||n |||       |||S |||t |||a |||n |||n |||a |||r |||d |||'' |||s ||'
print '||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||'
print '|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|'
print '____ ____ ____ ____ ____ ____ ____ ____'                                              
print '||D |||i |||n |||o |||P |||a |||s |||s ||'                                             
print '||__|||__|||__|||__|||__|||__|||__|||__||'                                             
print '|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|'
print ' '
#print RED
#print "RED"
#print BLUE
#print "BLUE"
#print CYAN
#print "CYAN"
#print GREEN
#print "GREEN"
#print RESET
#print "RESET"
#print BOLD
#print "BOLD"
#print REVERSE
#print "REVERSE"
print GREEN
count = raw_input('Enter number of times to generate a strong password from Kevan Stannard Dinopass website: ')
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
        print GREEN
        print 'This is from Kevan Stannard-DinoPass strong password website: \033[0;0m ' + html
#while True:
        try:
                print RESET
		dictionary1 = {' ':'\033[;1m ', '_':'\033[;1m_', '=':'\033[;1m =', ']':'\033[;1m]', '[':'\033[;1m[', '<':'\033[;1m<', '@':'\033[;1m@', '$':'\033[;1m$', '!':'\033[;1m!', ')':'\033[;1m)', '(':'\033[;1m(', '+':'\033[;1m+', '1':'\033[1;31m1', '2':'\033[1;31m2', '3':'\033[1;31m3', '4':'\033[1;31m4','5':'\033[1;31m5', '6':'\033[1;31m6', '7':'\033[1;31m7', '8':'\033[1;31m8', '9':'\033[1;31m9', '0':'\033[1;31m0', 'a':'\033[0;0ma',  'b':'\033[0;0mb', 'c':'\033[0;0mc', 'd':'\033[0;0md', 'e':'\033[0;0me', 'f':'\033[0;0mf', 'g':'\033[0;0mg', 'h':'\033[0;0mh', 'i':'\033[0;0mi', 'j':'\033[0;0mj', 'k':'\033[0;0mk', 'l':'\033[0;0ml', 'm':'\033[0;0mm', 'n':'\033[0;0mn', 'o':'\033[0;0mo', 'p':'\033[0;0mp','q':'\033[0;0mq', 'r':'\033[0;0mr', 's':'\033[0;0ms', 't':'\033[0;0mt', 'u':'\033[0;0mu', 'v':'\033[0;0mv', 'w':'\033[0;0mw', 'x':'\033[0;0mx', 'y':'\033[0;0my', 'z':'\033[0;0mz', 'A':'\033[;1mA', 'B':'\033[;1mB','C':'\033[;1mC', 'D':'\033[;1mD', 'E':'\033[;1mE','F':'\033[;1mF', 'G':'\033[;1mG',"H":"\033[;1mH", 'I':'\033[;1mI', 'J':'\033[;1mJ', 'K':'\033[;1mK','L':'\033[;1mL', 'M':'\033[;1mM', 'N':'\033[;1mN', 'O':'\033[;1mO', 'P':'\033[;1mP', 'Q':'\033[;1mQ', 'R':'\033[;1mR', 'S':'\033[;1mS', 'T':'\033[;1mT', 'U':'\033[;1mU', 'V':'\033[;1mV', 'W':'\033[;1mW', 'X':'\033[;1mX', 'Y':'\033[;1mY', 'Z':'\033[;1mZ'}
		dictionary2 = {' ':'\033[;1m^SPACE^','_':'\033[;1m_UNDERSCORE_', '=':'\033[;1m=EQUALS=', ']':'\033[;1m]BRACKET]', '[':'[\033[;1mBRACKET[', '<':'\033[;1m<LESS_THAN<', '@':'\033[;1m@AT_SIGN@', '$':'\033[;1m$DOLLAR_SIGN$', '!':'\033[;1m!BANG!', ')':'\033[;1m)PARENS)', '(':'\033[;1m(PARENS(', '+':'\033[;1m+PLUS_SIGN+', '1':'\033[1;31m#ONE#', '2':'\033[1;31m#TWO#', '3':'\033[1;31m#THREE#', '4':'\033[1;31m#FOUR#','5':'\033[1;31m#FIVE#', '6':'\033[1;31m#SIX#', '7':'\033[1;31m#SEVEN#', '8':'\033[1;31m#EIGHT#', '9':'\033[1;31m#NINE#', '0':'\033[1;31m#ZERO#', 'a':'\033[0;0malpha',  'b':'\033[0;0mbravo', 'c':'\033[0;0mcharlie', 'd':'\033[0;0mdelta', 'e':'\033[0;0mecho', 'f':'\033[0;0mfoxtrot', 'g':'\033[0;0mgolf', 'h':'\033[0;0mhotel', 'i':'\033[0;0mindia', 'j':'\033[0;0mjuliet', 'k':'\033[0;0mkilo', 'l':'\033[0;0mlima', 'm':'\033[0;0mmike', 'n':'\033[0;0mnovember', 'o':'\033[0;0moscar', 'p':'\033[0;0mpapa','q':'\033[0;0mquebec', 'r':'\033[0;0mromeo', 's':'\033[0;0msierra', 't':'\033[0;0mtango', 'u':'\033[0;0muniform', 'v':'\033[0;0mvictor', 'w':'\033[0;0mwhiskey', 'x':'\033[0;0mx-ray', 'y':'\033[0;0myankee', 'z':'\033[0;0mzulu', 'A':'\033[;1mALPHA', 'B':'\033[;1mBRAVO','C':'\033[;1mCHARLIE', 'D':'\033[;1mDELTA', 'E':'\033[;1mECHO','F':'\033[;1mFOXTROT', 'G':'\033[;1mGOLF','H':'\033[;1mHOTEL', 'I':'\033[;1mINDIA', 'J':'\033[;1mJULIET', 'K':'\033[;1mKILO','L':'\033[;1mLIMA', 'M':'\033[;1mMIKE', 'N':'\033[;1mNOVEMBER', 'O':'\033[;1mOSCAR', 'P':'\033[;1mPAPA', 'Q':'\033[;1mQUEBEC', 'R':'\033[;1mROMEO', 'S':'\033[;1mSIERRA', 'T':'\033[;1mTANGO', 'U':'\033[;1mUNIFORM', 'V':'\033[;1mVICTOR', 'W':'\033[;1mWHISKEY', 'X':'\033[;1mX-RAY', 'Y':'\033[;1mYANKEE', 'Z':'\033[;1mZULU'}
#                             inputtext = raw_input('Enter string to convert to phonetic: ')
        except (TypeError, ValueError, NameError):
               print('Oops! Invalid String Entered')
               break
        except KeyboardInterrupt:
                print "\n\n[*] User Requested An Interrupt"
                sys.exit(3)
        else:
                print REVERSE
                print ('Copy to MS-WORD to get BOLD, CAPS, and COLORS: \033[0;0m ' + ''.join(map(dictionary1.get,html)))
                print REVERSE
                print('Phonetic Alphabet: \033[0;0m ' + ', '.join(map(dictionary2.get,html)))
                count -= 1
                print " "
                showcount = str(count)
                print BOLD
                print ("website passwords left to generate: " + "\033[1;31m" + showcount)
                print " "
                time.sleep(2) # delays for 2 seconds
                if int(count) == 0:
                        break
