class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        for i in range(len(s)-1):
            if s[i] == 'I':
                if s[i+1] =='V' or  s[i+1] =='X':
                    total -=1
                else:
                    total +=1

            elif s[i] == 'V':
                total +=5

            elif s[i] == 'X':
                if  s[i+1] =='L' or  s[i+1] =='C':
                    total -= 10
                else:
                    total +=10

            elif s[i] == 'L':
                total +=50

            elif s[i] == 'C':
                if  s[i+1] =='D' or  s[i+1] =='M':
                    total -=100
                else:
                    total +=100
            elif s[i] == 'D':
                total += 500

            elif s[i] == 'M':
                total +=1000
        
        if s[-1] == 'I':
            total +=1

        elif s[-1] == 'V':
            total +=5

        elif s[-1] == 'X':
            total +=10

        elif s[-1] == 'L':
            total +=50

        elif s[-1] == 'C':
            total +=100
        elif s[-1] == 'D':
            total += 500
        elif s[-1] == 'M':
            total +=1000

        return total