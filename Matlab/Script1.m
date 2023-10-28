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
%% 
rosshutdown;  %Cierra la conexion con el maestro
