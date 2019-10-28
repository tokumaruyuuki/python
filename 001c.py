deg,dis = map(int,input().split())
 
force = round(dis/60+0.00001,1)
f_n = 0
 
if force <= 0.2:
    print('C 0')
    exit()
elif force <= 1.5:
    f_n = 1
elif force <= 3.3:
    f_n = 2
elif force <= 5.4:
    f_n = 3
elif force <= 7.9:
    f_n = 4
elif force <= 10.7:
    f_n = 5
elif force <= 13.8:
    f_n = 6
elif force <= 17.1:
    f_n = 7
elif force <= 20.7:
    f_n = 8
elif force <= 24.4:
    f_n = 9
elif force <= 28.4:
    f_n = 10
elif force <= 32.6:
    f_n = 11
elif force >= 32.7:
    f_n = 12
 
d_n = 0
 
if deg/10 <= 11.24 or deg/10 >= 348.75:
    d_n = 'N'
elif deg/10 <= 33.74:
    d_n = 'NNE'
elif deg/10 <= 56.24:
    d_n = 'NE'
elif deg/10 <= 78.74:
    d_n = 'ENE'
elif deg/10 <= 101.24:
    d_n = 'E'
elif deg/10 <= 123.74:
    d_n = 'ESE'
elif deg/10 <= 146.24:
    d_n = 'SE'
elif deg/10 <= 168.74:
    d_n = 'SSE'
elif deg/10 <= 191.24:
    d_n = 'S'
elif deg/10 <= 213.74:
    d_n = 'SSW'
elif deg/10 <= 236.24:
    d_n = 'SW'
elif deg/10 <= 258.74:
    d_n = 'WSW'
elif deg/10 <= 281.24:
    d_n = 'W'
elif deg/10 <= 303.74:
    d_n = 'WNW'
elif deg/10 <= 326.24:
    d_n = 'NW'
elif deg/10 <= 348.74:
    d_n = 'NNW'
    
print(d_n,f_n)