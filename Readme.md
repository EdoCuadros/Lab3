# Laboratorio 3 de Robótica. Introduccipon a ROS
Integrantes:

***Eduardo Cuadros Montealegre***

***Oscar Javier Restrepo***

## Introducción
ROS (Robot Operating System) provee librerías y herramientas para ayudar a los desarrolladores de software a crear aplicaciones para robots. ROS provee abstracción de hardware, controladores de dispositivos, librerías, herramientas de visualización, comunicación por mensajes, administración de paquetes y más. ROS está bajo la licencia open source, BSD.

## Conexión de ROS con Matlab:
Procedimiento:

Con Linux operando lanzar 2 terminales. En la primera terminal escribir el comando roscore
para iniciar el nodo maestro.
![Inicio de nodo maestro](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/Ros1.png)
En la segunda terminal escribir rosrun turtlesim turtlesim node.
![Inicio de nodo maestro](https://github.com/EdoCuadros/Lab3/blob/main/Imágenes/Ros2.png)
Lanzar una instancia de Matlab para Linux (es imperativo que tenga el toolbox de robótica
de Mathworks).
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
