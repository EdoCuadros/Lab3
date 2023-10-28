# Laboratorio 3 de Robótica. Introduccipon a ROS
Integrantes:

***Eduardo Cuadros Montealegre***

***Oscar Javier Restrepo***

## Introducción
ROS (Robot Operating System) provee librerías y herramientas para ayudar a los desarrolladores de software a crear aplicaciones para robots. ROS provee abstracción de hardware, controladores de dispositivos, librerías, herramientas de visualización, comunicación por mensajes, administración de paquetes y más. ROS está bajo la licencia open source, BSD.

Un sistema ROS está compuesto por un número de nodos independientes, cada uno de los cuales puede comunicarse con otros nodos usando un modelo de mensajes
publish/subscribe

ROS inicia al levantar su elemento principal, el ROS master. El master permite que otros elementos de software (nodos) puedan encontrarse e intercambiar información. Para esto los nodos publican y se suscriben en tópicos.

Para poder entender el funcionamiento de ROS se puede usar turtlesim, el cual es un paquete que consiste en una pantalla en la que se carga una tortuga, la que se puede mover por la pantalla y otras cosas más.


## Conexión de ROS con Matlab:
Procedimiento:

Con Linux operando lanzar 2 terminales. En la primera terminal escribir el comando roscore para iniciar el nodo maestro.
![Inicio de nodo maestro](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/Ros1.png)
En la segunda terminal escribir rosrun turtlesim turtlesim node.
![Inicio de nodo maestro](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/Ros2.png)
Lanzar una instancia de Matlab para Linux (es imperativo que tenga el toolbox de robótica de Mathworks).
Crear un script con el siguiente código:
```
%%
rosinit; %Conexión con nodo maestro
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Creación publicador
velMsg = rosmessage(velPub) %Creación de mensaje
%%
velMsg.Linear.X = 2 %Valor del mensaje
velMsg.Linear.Y = 3
send(velPub,velMsg) %Envio
pause(1)
```
Ejecutar las tres secciones del script y observar los resultados con la pose de la tortuga.
![Inicio de nodo maestro](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/Ros3.png)

Crear un script en Matlab que permita suscribirse al tópico de pose de la simulación de turtle1. Tip: Usar la instrucción rossubscriber con los argumentos (’TOPICNAME’, ’MESSAGETY- PE’), luego utilizar la opción lattest message para captura el último mensaje obtenido.
```
%%
posPub = rospublisher('/turtle1/pose','turtlesim/Pose'); %Creación publicador
posMsg = rosmessage(posPub) %Creación de mensaje
```
![Inicio de nodo maestro](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/Ros4.png)
Crear un script en Matlab que permita enviar todos los valores asociados a la pose de turtle1. Tip: El tópico pose únicamente sirve para suscribirse, consultar los servicios de turtlesim para modificar la pose de la tortuga.
```
%%
posMsg.X = 2; %Valor del mensaje
posMsg.Y = 3;
posMsg.Theta=1.572;
posMsg.LinearVelocity=1;
posMsg.AngularVelocity=1;
send(posPub,posMsg) %Envio
pause(1)
```
![Inicio de nodo maestro](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/Ros5.png)
Consultar de qué manera se finaliza el nodo maestro en Matlab.
```
%% 
rosshutdown;  %Cierra la conexion con el maestro

```
![Inicio de nodo maestro](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/Ros6.png)

## Conexión de ROS con Python

Se nos pide escribir un código que permita modificar las velocidades lineales y angulares de la tortuga del paquete *turtlesim*. 

Primero se importan las librerías a manejar.Entre las más importantes esta *rospy* para la integración de ROS con python, *Twist* para el envío de comandos a *turtlesim*, *termios*, *sys* y *os* para el manejo del teclado y *Teleport Absolute* para el comando de teletransporte. 

```
import rospy  
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, Teleport Relative
import termios, sys, os
from numpy import pi, sin, cos
```

Se crea la función para la lectura del teclado

```
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
```

Y la función *rotate*, en la cual se tendrá todo el proceso para la modificación y el envío de las distintas velocidades de la tortuga.

Primero se  inicializa el nodo y se instancia el objeto Publisher con el tópico cmd_vel para la modificación de la velocidad.

```
rospy.init_node('my_turtle',anonymous=True) 
vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
vel_msg = Twist()
```
Luego se empieza el bucle infinito para la constante lectura de las teclas y el posterior movimiento de la tortuga acorde con lo deseado.

```
while True:
    key = get_key() # Cada iteración del bucle se lee la entrada de teclado
    key = key.decode('utf-8',errors='replace')  # Se convierte la variable hexadecimal a str
```

Luego se utiliza una secuencia *try /except* para la evaluación de la variable de entrada, en este caso se tiene un bloque condicional donde se evalúa y se toma una acción consecuente.

```
try:  
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
```

Luego se publica el mensaje con los parámetros modificados.


```
vel_pub.publish(vel_msg)
```

Para finalizar, se crea el metodo main donde se ejecuta la función *rotate()*

```
if __name__ == '__main__':
    try:
        rotate()
    except ROSInterruptException:
        pass     
```
![Movimiento de tortuga](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/turtlesim1.png)
