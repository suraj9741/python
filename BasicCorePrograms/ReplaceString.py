def main():
    UserName = input("Enetr the User Name : ")
    Lenght = len(UserName)
    if Lenght > 3 :
        print (f'Hello {UserName}, How are you?')
    else :
        print('Enter min 3 char')
    x=1+2j
    print(type(x))
    a = {5, 2, 3, 1, 4}
    print("a = ", a)

if __name__ == '__main__':
    main()
