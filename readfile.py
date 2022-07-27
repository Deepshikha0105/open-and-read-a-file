with open("sysytem.txt",'r') as f:
    a= f.read()
    if "deepshikha" in a:
        print("present")
    else:
        print('absent')
