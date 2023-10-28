#!/usr/bin/env python

# Script de python correspondiente a un nodo tipo Teleop_key

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from turtlesim.msg import Pose
import termios, sys, os
from numpy import pi,sin,cos
import termios, sys, os

TERMIOS = termios

def get_key():  
    # Función para leer entradas de teclado, retorna la tecla oprimida en hexadecimal
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd,TERMIOS.TCSANOW,new)
    c = None
    try:
        key = os.read(fd,1)
    finally:
        termios.tcsetattr(fd,TERMIOS.TCSAFLUSH,old)
    return key

def get_ang(data):
    return data.theta  # Aquí obtienes el ángulo de inc

def rotate():
    # Función de movimiento de tortuga

    rospy.init_node('my_turtle',anonymous=True) 

    # Se instancia el objeto Publisher con el tópico cmd_vel para modificar velocidad
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    
    # Se crea el objeto tipo Twist para enviar los comandos de velocidad al nodo de la tortuga
    vel_msg = Twist()
    ang = 0

    while True:
        key = get_key() # Cada iteración del bucle se lee la entrada de teclado
        key = key.decode('utf-8',errors='replace')  # Se convierte la variable hexadecimal a str

        try:    # Se utiliza try / except por si no hay entrada del teclado.
            if key.lower() == 'w':
                vel_msg.linear.x = 1
                vel_msg.angular.z = 0

            elif key.lower() == 'a':
                vel_msg.angular.z = pi/4
                vel_msg.linear.x = 0
                ang += pi/4

            elif key.lower() == 'd':
                vel_msg.angular.z = -pi/4
                vel_msg.linear.x = 0
                ang -= pi/4

            elif key.lower() == 's':     
                vel_msg.linear.x = -1
                vel_msg.angular.z = 0

            elif key.lower() == 'q':    # Para finalizar ejecución del código
                break

            elif key.lower() == ' ':
                turtle_teleport = rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
                turtle_teleport(5.5,5.5,0)  # Se usa el servicio teleport_absolute y
                                            # se manda la tortuga a las coordenadas del centro.

            elif key.lower() == 'r':
                vel_msg.linear.x = 0        # Rotación de 180° o sea pi radianes
                vel_msg.angular.z = pi


            vel_pub.publish(vel_msg)
        
        except:
            pass

# Metodo main para iniciar código
if __name__ == '__main__':
    try:
        rotate()
    except rospy.ROSInterruptException:
        pass


    