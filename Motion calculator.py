
print("Hello welcome to Physics Calculator")
print("Enter the appropriate values")
print("If you dont have value for particular item put '0' as its value")

ok = input("Type 'ok' and hit enter to continue ('ok' in small): ")

if ok == 'ok':
    d = int(input("Enter distance:"))
    s = int(input("Enter displacement:"))
    v = int(input("Enter velocity:"))
    u = int(input("Enter initial velocity:"))
    a = int(input("Enter acceleration:"))

    th = int(input("Enter time in hours: "))
    tm = int(input("Enter time in minutes: "))
    ts = int(input("Enter time in seconds: "))

    total_seconds = th * 3600 + tm * 60 + ts


    def speed():
        print(d/total_seconds)
    def velocity():
        print(s/total_seconds)
    def displacement():
        print(v*total_seconds)
    def time():
        print(s/v)
    def acceleration():
        print((v-u)/total_seconds)  # Corrected parentheses


    select = input("speed=s,velocity=v,displacement=d,time=t,acceleration=a:")
    if select == 's':
        speed()
    elif select == 'v':
        velocity()
    elif select == 'd':
        displacement()
    elif select == 't':
        time()
    elif select == 'a':
        acceleration()

else :
    print("Sorry something went wrong")