from math import *
from array import array
def Gelato (minput, uppercase = False, lowercase = False):
    #There's a possibility to put a lowercase text in uppercase by writing !uppercase [your text] you can do the opposite by writing !lowercase [your text]
    if ('!uppercase' in minput) == True :
        minput = minput.replace('!uppercase ', '')
        uppercase = True
    elif ('!lowercase' in minput) == True :
        minput = minput.replace('!lowercase ', '')
        lowercase = True
    minput = list(minput)
    res = []
    #We pass the elements of the list to ASCII
    for ele in minput:
        res.extend(ord(num) for num in ele)
    inputASCII = res
    i = 0
    code4real = ""
    h = 0
    #If the lowercase or uppercase options were selected they take effect here
    if uppercase == True :
        while h < len(inputASCII) :
            inputASCIIindex = inputASCII[h]
            if inputASCIIindex  >= 97 and inputASCIIindex  <= 122 :
                inputASCII[h] = inputASCIIindex - 32
            h = h + 1
    elif lowercase == True :
        while h < len(inputASCII) :
            inputASCIIindex = inputASCII[h]
            if inputASCII[h]  >= 65 and inputASCII[h]  <= 90 :
                inputASCII[h] = inputASCII[h] + 32
            h = h + 1
    #Now for each element of the input list (now in ASCII) we find 5 solutions in BrainFu**k
    while i < len(inputASCII) :
        tempsvalue = 0
        valuetoadd = 0
        codePLUS = ""
        codeSQUARE = ""
        codeMULTI = ""
        codeMULTIplus = ""
        codeSQUAREplus = ""
        msqrt = round(sqrt(inputASCII[i]))
        if msqrt**2 < inputASCII[i] :
            valuetoadd = inputASCII[i] - msqrt**2
            if i == 0 :
                codeSQUARE +=  ">"  +  "+"*msqrt + "[<" + "+"*msqrt + ">-]<" + "+"*valuetoadd + "."
            else :
                codeSQUARE +=  ">>"  +  "+"*msqrt + "[<" + "+"*msqrt + ">-]<" + "+"*valuetoadd + "."
        elif msqrt**2 > inputASCII[i] :
            valuetoadd = msqrt**2 - inputASCII[i]
            if i == 0 :
                codeSQUARE +=  ">"  +  "+"*msqrt + "[<" + "+"*msqrt + ">-]<" + "-"*valuetoadd + "."
            else :
                codeSQUARE +=  ">>"  +  "+"*msqrt + "[<" + "+"*msqrt + ">-]<" + "-"*valuetoadd + "."
        else : codeSQUARE +=  ">"  +  "+"*msqrt + "[<" + "+"*msqrt + ">-]<."
        j = 1
        h = 0
        mt = 0
        while j < 12 :
            if j == 11 :
                if i == 0 :
                    codeMULTI += ">"  +  "+"*int(mt) + "[<" + "+"*int(h) + ">-]<."
                    break
                else :
                    codeMULTI += ">>"  +  "+"*int(mt) + "[<" + "+"*int(h) + ">-]<."
                    break
            elif float(inputASCII[i])%j != 0 :
                j += 1
            else :
                mt = float(inputASCII[i])/j
                h = j
                if j*mt == float(inputASCII[i]) :
                    j += 1
        ordre4shit = [len(codeMULTI),len(codeSQUARE)]
        if i != 0 :
            if msqrt > inputASCII[i-1] :
                testvalue = msqrt - inputASCII[i-1]
                if msqrt**2 < inputASCII[i] :
                    codeSQUAREplus += "+"*testvalue + "[>" + "+"*msqrt + "<-]>" + "+"*valuetoadd +"."
                else :    codeSQUAREplus += "+"*testvalue + "[>" + "+"*msqrt + "<-]>" + "-"*valuetoadd +"."
            elif msqrt < inputASCII[i-1] :
                testvalue = inputASCII[i-1] - msqrt
                if msqrt**2 < inputASCII[i] :
                    codeSQUAREplus += "-"*testvalue + "[>" + "+"*msqrt + "<-]>" + "+"*valuetoadd +"."
                else :    codeSQUAREplus += "-"*testvalue + "[>" + "+"*msqrt + "<-]>" + "-"*valuetoadd +"."
            if inputASCII[i-1] > inputASCII[i] :
                tempvalue = inputASCII[i-1] - inputASCII[i]
                codePLUS += "-"*tempvalue + "."
            if inputASCII[i-1] < inputASCII[i] :
                tempvalue = inputASCII[i] - inputASCII[i-1]
                codePLUS += "+"*tempvalue + "."
            if inputASCII[i-1] == inputASCII[i] :
                codePLUS += "."
            h = int(h)
            mt = int(mt)
            tempvalue = []
            tempvalue1 = 0
            tempvalue2 = 0
            tempvalue3 = 0
            tempvalue4 = 0
            if inputASCII[i-1] > h :
                tempvalue1  = inputASCII[i-1] - h
                tempvalue.append(tempvalue1)
            if inputASCII[i-1] < h :
                tempvalue2  = h - inputASCII[i-1]
                tempvalue.append(tempvalue2)
            if inputASCII[i-1] > mt :
                tempvalue3  = inputASCII[i-1] - mt
                tempvalue.append(tempvalue3)
            if inputASCII[i-1] < mt :
                tempvalue4  = mt - inputASCII[i-1]
                tempvalue.append(tempvalue4)
            tempvalue.sort()
            multi = int(tempvalue[0])
            if multi == tempvalue1 :
                multi1 = mt
                codeMULTIplus += ">"+"+"*multi1 + "[<" + "-"*multi + ">-]<."
            if multi == tempvalue2 :
                multi1 = mt
                codeMULTIplus += ">"+"+"*multi1 + "[<" + "+"*multi + ">-]<."
            if multi == tempvalue3 :
                multi1 = h
                codeMULTIplus += ">"+"+"*multi1 + "[<" + "-"*multi + ">-]<."
            if multi == tempvalue4 :
                multi1 = h
                codeMULTIplus += ">"+"+"*multi1 + "[<" + "+"*multi + ">-]<."
    #  Now that we have our 5 solutions we try to find the shortest
            ordre4shit.append(len(codeSQUAREplus))
            ordre4shit.append(len(codePLUS))
            ordre4shit.append(len(codeMULTIplus))
        ordre4shit.sort()
        if ordre4shit[0] == len(codeMULTI) :
            code4real += codeMULTI
        elif ordre4shit[0] == len(codeSQUARE) :
            code4real += codeSQUARE
        elif ordre4shit[0] == len(codePLUS) :
            code4real += codePLUS
        elif ordre4shit[0] == len(codeMULTIplus) :
            code4real += codeMULTIplus
        elif ordre4shit[0] == len(codeSQUAREplus) :
            code4real += codeSQUAREplus
    # Now we have add the shortest solution to the code4real string which is the final code (which is shown at the end)
        i += 1
    return(code4real)

while True :
    minput = input()
    if "!uppercase" in minput == True :
        minput.remove('!uppercase')
        print(Gelato(minput,False,True))
    elif "!lowercase" in minput == True :
        minput.remove('!lowercase')
        print(Gelato(minput,True))
    else : print(Gelato(minput))
