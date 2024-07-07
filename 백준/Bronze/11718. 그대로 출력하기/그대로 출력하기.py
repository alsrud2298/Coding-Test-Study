flag = True
while(flag):
    try:
        print(input())
    except EOFError:
        break
    