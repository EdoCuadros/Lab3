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

## Utilizando Python

## Análisis

## Conclusiones
