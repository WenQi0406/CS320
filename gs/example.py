import json


if __name__ == "__main__":


    # use while loop, put data[i]'s dict in the outlis, the length of outlis is length of data
    with open("small_prob_input.json") as f:
        data = json.load(f)
    print(type(data))
    print(data[0])
    print(data[1])
    print(("first data is :",data[0][0]))
    print(type(data[0][0]))
    dic=data[0][0]

    manlist=[]
    manlist = list(dic.keys())
    print(manlist)
    manpreferlist=dic[manlist[0]]
    print(manpreferlist)
    dic={'a':'1','b':'2','c':'3'}
    dic['d']='4'
    print(dic)
    dic.pop('b')
    print(dic)