import numpy as np

def f_x(x):
    return (3*x**2)*(x**3+2)**2

def namafungsi(f, a, b, n, pilihan):
    delta_x = (b - a) / float(n)
    if(pilihan == 1):
        x_left = np.linspace(a, b-delta_x, n)
        area_left = f_x(x_left).sum() * delta_x
        print ("Reiman Kiri : "+str(area_left))
    elif(pilihan == 2):
        x_right = np.linspace(a+delta_x, b, n)
        area_right = f_x(x_right).sum() * delta_x
        print("Reiman kanan : "+str(area_right))
    elif(pilihan == 3):
        x_mid = np.linspace(a+delta_x/2., b-delta_x/2., n)
        area_mid = f_x(x_mid).sum() * delta_x
        print("Reiman Tengah : "+str(area_mid))
    elif(pilihan == 4):
        integration = f_x(a) + f_x(b)
        for i in range(1,n):
            k = a + i*delta_x
            integration = integration + 2 * f_x(k)
        integration = integration * delta_x/2
        print("Trapesium : "+str(integration))
    elif(pilihan == 5):
        integration = f_x(a) + f_x(b)
        for i in range(1,n):
            k = a + i*delta_x
            if i%2 == 0:
                integration = integration + 2 * f_x(k)
            else:
                integration = integration + 4 * f_x(k)
        integration = integration * delta_x/3
        print("Parabola : " +str(integration))

namafungsi(f_x, 0, 2, 4, 5)