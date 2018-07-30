list1=[None]#LISTA,0000;CLA;CLL;DCA LIST1
list2=[None]#LISTB,0020;CLA;CLL;TAD LISTB;DCA LIST2
length=0#CLA;CLL;DCA @length
while True:
    try:
        list1[0]=int(input("enter element"))#ENTRY,HLT;OSR;DCA *LIST1
    except KeyboardInterrupt:
        for i in list2:
            print(i)
        break
    pos=1#CLA;CLL;IAC;DCA POS
    lengtht=-length#TAD @LENGTH;CIA;DCA LENGTHT
    length+=1
    while lengtht!=0:#LOOP1,ISZ LENGTHT;SKP;JMP END
        lengtht+=1
        list1.append(None)
        list1[pos]=list2[pos-1]-list1[pos-1]#TAD 9999;TAD LIST1;TAD POS;DCA LOAD;TAD *LOAD;MQL;TAD 9999;TAD LIST2;TAD POS;DCA LOAD;TAD *LOAD;SAM;MQL;TAD LIST1;TAD POS;DCA LOAD;MQA;DCA *LOAD
        pos+=1#TAD POS;IAC;DCA POS
    list1,list2=list2,list1#END,TAD LIST1;MQL;TAD LIST2;DCA LIST1;MQA;DCA LIST2;JMP ENTRY
##    try:
##        list2[0]=int(input("enter element"))
##    except KeyboardInterrupt:
##        for i in list1:
##            print(i)
##        break
##    pos=0
##    lengtht=-length
##    while lengtht!=0:
##        lengtht+=1
##        list2[pos]=list1[pos-1]-list2[pos-1]
##        pos+=1
