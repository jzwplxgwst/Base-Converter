#Loop 5 times
i=1
while 1<10:

#Input of values
    print('______________________________________________________')
    print(' ')
    num = str(input('Enter the number to convert: '))
    basex = int(input('Enter the base of that number: '))
    basey = int(input('Enter the base of the new base number: '))

#Determines the final print
    t = 1
    
#Verification
    if basex > 17 or basex < 1 or basey > 17 or basey <1 :
        print('Error, base of the number may be too large or too small (maximum base: 2-16)')
        print('______________________________________________________')
    else :

#Base x to base 10
        decimal = 0
        power = len(num) - 1
        for x in num :
            if x.isnumeric() :
                decimal = decimal + (int(x) * (basex**power))
            elif x == 'A' :
                decimal = decimal + (10 * (basex**power))
            elif x == 'B' :
                decimal = decimal + (11 * (basex**power))
            elif x == 'C' :
                decimal = decimal + (12 * (basex**power))
            elif x == 'D' :
                decimal = decimal + (13 * (basex**power))
            elif x == 'E' :
                decimal = decimal + (14 * (basex**power))
            elif x == 'F' :
                decimal = decimal + (15 * (basex**power))
            else :
                print('Error, base may be larger then 16 or less then 2 (max base: 2-16)')
                print('______________________________________________________')
                #Determines the final print
                t = 0
                
            power = power - 1

#Base 10 to base y
        var = ['0','1','2','3','4','5' ,'6','7','8','9','A','B','C','D','E','F']

        final = 0
        txt = ''
        y = decimal
        while y > 0 :
            final = (decimal%basey)
            decimal = (decimal//basey)    
            txt = txt + (var[final])
            y = decimal

#Output of values
        if t > 0.9 :
            print(num, 'in base', basex, 'is ', end='')
            print(txt[::-1], end='')
            print(' in base', basey)
            print('______________________________________________________')

#End of loop
    i+=1
else :
    print('Restart Program')
