def findMin(hour,min):
    var1=(hour*360)/12+(min*360)/(12*60)
    var2= (min*360)/60
    angle=abs(var1-var2)
    if angle>180:
        angle=360-angle
    return angle
if __name__ == "__main__":
    
    a=int(input())
    b=float(input())
    k=(a/360)*b
    h=int(k)
    m=float(k-h)
    m=m*60
    h=h%12
    if(h!=0):
      h=h
    else:
      h=12
    print("%.2f" % findMin(h,m))

