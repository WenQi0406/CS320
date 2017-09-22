import json



if __name__ == "__main__":
    import time
    start_time = time.process_time()
    '''
    data
    datalen
    subdatalen
    mangroup
    man
    manprefer
    womangroup 
    woman
    womanprefer
    out
    
    /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Volumes/共享/cs320/gs/gs.py
datalen is: 2 
    ---means we have # stable matching table
        --- [[{'a0': ['b0', 'b1'], 'a1': ['b1', 'b0']}, {'b0': ['a0', 'a1'], 'b1': ['a1', 'a0']}], [{'j0': ['k2', 'k1', 'k0'], 'j1': ['k2', 'k1', 'k0'], 'j2': ['k0', 'k2', 'k1']}, {'k0': ['j1', 'j0', 'j2'], 'k1': ['j0', 'j2', 'j1'], 'k2': ['j2', 'j1', 'j0']}]]
subdatalen is [2, 2] 
    ---should alway be 2
        --- [{'a0': ['b0', 'b1'], 'a1': ['b1', 'b0']}, {'b0': ['a0', 'a1'], 'b1': ['a1', 'a0']}]
mangroup is:
 {'a0': ['b0', 'b1'], 'a1': ['b1', 'b0']}
we have mans:
 ['a0', 'a1']
manprefer is:
 ['b0', 'b1']
womangroup is:
 {'b0': ['a0', 'a1'], 'b1': ['a1', 'a0']}
we have woman:
 ['b0', 'b1']
womanprefer is:
 ['a0', 'a1']
new dict is:
 {}
woman_gs is:
 b0
manprefer list after mangroup[man[0]].remove(woman_gs) is:
 ['b1']
data[0] also be changed:
 [{'a0': ['b1'], 'a1': ['b1', 'b0']}, {'b0': ['a0', 'a1'], 'b1': ['a1', 'a0']}]
Ran in: 0.00031 secs
    '''
    outlis=[]
    with open("small_prob_input.json") as f:
        data=json.load(f)
    datalen=len(data)
    i = 0
    while(i < (datalen)):

        print('datalen is:',datalen,'\n    ---means we have # stable matching table')
        print('        ---',data)
    #we got data is the information which is a list[][]
    #we got length of data is datalen and length of data[group] is subdatalen
    #then I believe i can get each element in data
    #we image a is man b is woman
        mangroup=data[i][0]
        print('mangroup is:\n',mangroup)
        man=list(mangroup.keys())
        print('we have mans:\n',man)
        manprefer=mangroup[man[0]]
        print('manprefer is:\n',manprefer) #mangroup[man[1]][0]


        womangroup=data[i][1]
        print('womangroup is:\n',womangroup)
        woman=list(womangroup.keys())
        print('we have woman:\n',woman)
        womanprefer=womangroup[woman[0]]
        print('womanprefer is:\n',womanprefer)

    # creat a new dict and named it 'out'
        out = {}
    #out[man[0]] = manprefer[0]
    #if manprefer[0] in out.values():  # check the value in the out or not
    #    out.pop(man[0])
        print("new dict is:\n", out)
    #we can begin GS
    #---man is a list which include the key
    #---manprefer is the prefer list of man, which also a list

    #we can use basic case that man list goes to null and woman list goes to null
    #if not basic case, we put man and woman in the out dict as key and value. then use .remove() to remove.
    #use for loop or while loop? if use while, I belive is better
    #while(man==null && woman==null) out dict is finished.
    #precode is the question on the inclass work sheet

    #while(len(man) != 0):
    #woman_gs=mangroup[man[0]][0]
    #print('woman_gs is:\n',woman_gs)
    #mangroup[man[0]].remove(woman_gs)
    #print('manprefer list after mangroup[man[0]].remove(woman_gs) is:\n',manprefer)
    #print('data[0] also be changed:\n',data[0])


    #womanpeer is current man to the woman
        while (len(man) !=0):
            mangs=man[0]
            womangs=mangroup[man[0]][0]
            mangroup[man[0]].remove(womangs)
            man.remove(mangs)
            if(womangs in out.values()):
                womanpeer=list(out.keys())[list(out.values()).index(womangs)]
                womanlis=womangroup[womangs]
                if(womanlis.index(womanpeer) > womanlis.index(mangs)):
                    out.pop(womanpeer)
                    out[mangs]=womangs
                    man.append(womanpeer)
                else:
                    man.append(mangs)
            else:
                out[mangs]=womangs


        outlis.append(out)


        #name = "samll_prob_out" if 'samll_prob_out'.endswith('.json') else  'samll_prob_out'+ '.json'


        i = i+1

    print("stable matching is:", outlis)

    with open("samll_prob_out.json", mode='w') as f:
        json.dump(outlis, f)

    end_time = time.process_time()
    print("Ran in: {:.5f} secs".format(end_time - start_time))