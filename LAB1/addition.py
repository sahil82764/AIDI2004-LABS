def addition(x,y):
    return x + y

if __name__ == '__main__':
    str1 = input('Enter two number separated by spaces:: ')
    print(addition(int(str1.strip().split()[0]),int(str1.strip().split()[1])))