from backwork.dddirection import *
class Cam:
    def __init__(cam, dobo):
        cam.x= 0
        cam.y = 0.1
        cam.z =-10
        cam.d = dobo.d
        cam.v = 0
        cam.Ma=0
        cam.En=0
        cam.St=0
        cam.comp_a = 0
        cam.comp_e = 0
        cam.comp_8 = 0
        cam.dobo = dobo
    
    def place(cam):
        X,Y,Z = avixyz(-100,cam.d, cam.v)
        X += cam.dobo.x
        Y += cam.dobo.y
        Z += cam.dobo.z
        cam.x = X+avix(10,cam.d-pi/2)
        cam.y = Y+aviy(10,cam.d-pi/2)
        cam.z = -abs(Z)-10

    def recup_pos(cam):
        a, b, c = cam.dobo.test()
        return([int(cam.d*1000)/1000, int(cam.v*1000)/1000, int(cam.dobo.stun*10)/10, int(cam.dobo.En*10)/10, int(cam.dobo.Ma*10)/10, int(a), int(b), int(c)])
    
    def propriete(cam, mess):
        cam.d = float(mess[1])
        cam.v = float(mess[2])
        cam.St = float(mess[3])
        cam.En = float(mess[4])
        cam.Ma = float(mess[5])
        cam.comp_a = int(mess[6])
        cam.comp_e = int(mess[7])
        cam.comp_8 = int(mess[8])
