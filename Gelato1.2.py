from math import *
from array import array
minput = input()
#print(minput)
uppercase = False
lowercase = False
if ('!uppercase' in minput) == True :
    minput = minput.replace('!uppercase ', '')
    uppercase = True
elif ('!lowercase' in minput) == True :
    minput = minput.replace('!lowercase ', '')
    lowercase = True
minput = list(minput)
#print("The original list : " + str(minput))
res = []
for ele in minput:
    res.extend(ord(num) for num in ele)
#print("The ascii list is : " + str(res))
inputASCII = res
i = 0
code4real = ""
h = 0
if uppercase == True :
#    print('test1.0')
    while h < len(inputASCII) :
#        print('test2.0')
        inputASCIIindex = inputASCII[h]
        if inputASCIIindex  >= 97 and inputASCIIindex  <= 122 :
            inputASCII[h] = inputASCIIindex - 32
        h = h + 1
elif lowercase == True :
#    print('test1.1')
    while h < len(inputASCII) :
#        print('test2.1')
        inputASCIIindex = inputASCII[h]
        if inputASCII[h]  >= 65 and inputASCII[h]  <= 90 :
            inputASCII[h] = inputASCII[h] + 32
        h = h + 1
while i < len(inputASCII) :
    tempsvalue = 0
    valuetoadd = 0
    codePLUS = ""
    codeSQUARE = ""
    codeMULTI = ""
    codeMULTIplus = ""
    codeSQUAREplus = ""
    msqrt = round(sqrt(inputASCII[i]))
#    print(inputASCII[i])
    if msqrt**2 < inputASCII[i] :
        valuetoadd = inputASCII[i] - msqrt**2
        #print(inputASCII[i], "->",msqrt**2+valuetoadd)
        if i == 0 :
            #print(msqrt," ", valuetoadd)
            codeSQUARE +=  ">"  +  "+"*msqrt + "[<" + "+"*msqrt + ">-]<" + "+"*valuetoadd + "."
        else :
            #print(msqrt, " ", valuetoadd)
            codeSQUARE +=  ">>"  +  "+"*msqrt + "[<" + "+"*msqrt + ">-]<" + "+"*valuetoadd + "."
    elif msqrt**2 > inputASCII[i] :
        valuetoadd = msqrt**2 - inputASCII[i]
        #print(inputASCII[i], "->",msqrt**2-valuetoadd)
        if i == 0 :
            #print(msqrt, " ", valuetoadd)
            codeSQUARE +=  ">"  +  "+"*msqrt + "[<" + "+"*msqrt + ">-]<" + "-"*valuetoadd + "."
        else :
            #print(msqrt, " ", valuetoadd)
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
                #print(h,"*",mt,"=",inputASCII[i])
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
#        print(inputASCII[i-1],"+/-",testvalue,"*",msqrt,"+/-",valuetoadd,"=",inputASCII[i],)
        if inputASCII[i-1] > inputASCII[i] :
            tempvalue = inputASCII[i-1] - inputASCII[i]
            #print(inputASCII[i-1],"-",inputASCII[i],"=",tempvalue)
            codePLUS += "-"*tempvalue + "."
        if inputASCII[i-1] < inputASCII[i] :
            tempvalue = inputASCII[i] - inputASCII[i-1]
            #print(inputASCII[i-1],"-",inputASCII[i],"=",tempvalue)
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
#    print("codeMULTIplus ->",codeMULTIplus,"---",len(codeMULTIplus))
#    print("codeMULTI -> ",codeMULTI,"---",len(codeMULTI))
#    print("codePLUS -> ",codePLUS,"---",len(codePLUS))
#    print("codeSQUARE -> ",codeSQUARE,"---",len(codeSQUARE))
#    print("codeSQUAREplus ->",codeSQUAREplus,"---",len(codeSQUAREplus))
#    print(code4real)
    i += 1
print(code4real)
