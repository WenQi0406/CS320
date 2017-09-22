def output(manlist):
    manlist.append(5)
def xplus(x):
    x = x+10
    return x

if __name__ == "__main__":
    manlist=[1,2]
    x=6
    xplus(x)
    while len(manlist) != 5:
        output(manlist)

    print(manlist)
    print(xplus(x))
    print(x)
    i = manlist.index(2)
    print(i)

    dic={'1':'a','2':'b','3':'c'}
    r=list(dic.keys())[list(dic.values()).index('b')]
    print(r)