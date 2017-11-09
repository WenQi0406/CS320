if __name__ == '__main__':

    l=[(1,'a'),(1,'b'),(2,'a'),(2,'b'),(3,'a'),(4,'a'),(5,'a'),(5,'b')]
    q=[1]

    l=filter(lambda l:l[0] in q,l)
    print(list(l))
