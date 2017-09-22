import json
import pprint



if __name__ == "__main__":
    import time
    start_time = time.process_time()
    '''
    some params we created:
    
    data
    datalen
    mangroup
    man
    manprefer
    womangroup 
    woman
    womanprefer
    out
    
explan of params:

datalen is: 2 
---means we have # stable matching table

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
new dict named out is:
 {}
woman_gs is:
 b0
manprefer list after mangroup[man[0]].remove(woman_gs) is:
 ['b1']
data[0] also be changed:
 [{'a0': ['b1'], 'a1': ['b1', 'b0']}, {'b0': ['a0', 'a1'], 'b1': ['a1', 'a0']}]
Ran in: 0.00031 secs
    '''
    #use while loop, put data[i]'s dict in the outlis, the length of outlis is length of data
    outlis=[]
    with open("small_prob_input.json") as f:
        data=json.load(f)
    datalen=len(data)
    i = 0

    #data include datalen information need to be matched, so use while loop to match them one by one
    while(i < (datalen)):
        mangroup=data[i][0]
        man=list(mangroup.keys())
        manprefer=mangroup[man[0]]

        womangroup=data[i][1]
        woman=list(womangroup.keys())
        womanprefer=womangroup[woman[0]]

    # creat a new dict and named it 'out'
        out = {}
    #we can begin GS
        """
        we check len(man) and know is there still a man is free
        if it is
        pick that man as mangs, and take the man 1'st prefer woman as womangs
        
        then we pop the mangs from man(list)
        and pop the womangs form that man preferlist (avoid the man ask again)
        we can dict named out
        if womangs in out as a value, it means womangs in engaged current
        then 
        we let womanpeer be the womangs's current peer
        and check the index of mangs and womanpeer in womangs's prefer list
        if mangs is above
        womanpeer becomes free, mangs and womangs are engaged, put them in out dict
        other cause
        we put mangs at the back of the man list, and wait for ask next new woman again
        
        if the womangs is not in the out dict, which means the womangs is free current
        we can put mangs and womangs in the out dict directly
        """
        while (len(man) !=0):
            mangs=man[0]
            womangs=mangroup[man[0]][0]
            mangroup[man[0]].remove(womangs)
            man.remove(mangs)
            if(womangs in out.values()):
                # womanpeer is current man to the woman
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


    #ret is makesure the result print in right way, after run.
    ret = pprint.pformat(outlis, indent=1, width=100, compact=True).replace('(', '[').replace(')', ']').replace('\'','"')
    try:
        json.loads(ret)
    except ValueError:
        print("Tried to encode as: " + ret)
        raise


    print("stable matching is:", ret)

    with open("my_output_small.json", mode='w') as f:
        json.dump(outlis, f)

    end_time = time.process_time()
    print("Ran in: {:.5f} secs".format(end_time - start_time))