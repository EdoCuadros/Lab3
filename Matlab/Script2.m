%
rosinit; %Conexión con nodo maestro
%%
posPub = rospublisher('/turtle1/pose','turtlesim/Pose'); %Creación publicador
posMsg = rosmessage(posPub) %Creación de mensaje
%%
posMsg.X = 2; %Valor del mensaje
posMsg.Y = 3;
posMsg.Theta=1.572;
posMsg.LinearVelocity=1;
posMsg.AngularVelocity=1;
send(posPub,posMsg) %Envio
pause(1)
%% 
rosshutdown;  %Cierra la conexion con el maestro

