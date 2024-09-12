print("Distance = d,Displacement = s,Velocity = v,"
      "(Inital velocity = u),Time = t,Accleration = a")
d = int(input("Enter distance:"))
s = int(input("Enter displacement:"))
v = int(input("Enter velocity:"))
u = int(input("Enter initial velocity:"))
t = int(input("Enter time:"))
a = int(input("Enter accleration:"))
def speed():
    print(d/t)
def velovity():
    print(s/t)
def displacement():
    print(v*t)
def time():
    print(s/v)
def accleration():
    print(v-u/t)
select = int(input("speed=1,velocity=2,""displacement=3,time=4,""accleration=5 :"))
if select == 1:
    print(speed())
elif select == 2:
    print(velovity())
elif select == 3:
    print(displacement())
elif select == 4:
    print(time())
elif select == 5:
    print(accleration())
