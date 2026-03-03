dentro de este main se tiene un codigo de python que peude crear, eliminar, listar y r clientes o usuarios, el cual usa un framework de fastapi para mirarlo en un entorno visual

¿Es seguro usar variable global?
No es seguro porque los datos son "volátiles", es decir, solo existen mientras el programa está encendido. Como vimos en tu terminal, cada vez que el código se reinicia o apagas el WSL, la lista de clientes y el contador vuelven a cero. En un banco real esto sería un desastre porque los saldos o datos de los clientes desaparecerían al primer apagón o actualización del sistema.

¿Dónde aparece el recurso compartido?
El recurso compartido aparece en la lista clientes y en la variable contador_creaciones. Se llaman así porque todas las funciones de tu aplicación (la que crea, la que borra y la que edita) intentan entrar al mismo "cajón" de memoria al mismo tiempo para manipular los datos. Cuando muchos usuarios usan la app a la vez, todos están compitiendo por modificar esos mismos archivos.

¿Se debería usar lock en producción?
Sí, se debería usar si decides guardar datos en la memoria del servidor, ya que el "lock" funciona como un semáforo que hace que los procesos esperen su turno para no chocar. Sin embargo, lo más común en el trabajo real no es usar un lock sobre variables, sino cambiar esas variables por una base de datos profesional. Las bases de datos ya traen sus propios sistemas de seguridad para que dos movimientos bancarios no se crucen ni generen errores.

<img width="885" height="907" alt="image" src="https://github.com/user-attachments/assets/8690c849-41e4-4bab-89a9-320e303fcf44" />

<img width="869" height="869" alt="image" src="https://github.com/user-attachments/assets/073f1fd2-90c9-4360-a38a-7f91f5dcc563" />

<img width="889" height="910" alt="image" src="https://github.com/user-attachments/assets/cc8461d3-1215-48d4-94af-c6bacdceb955" />

<img width="859" height="617" alt="image" src="https://github.com/user-attachments/assets/0e2e5cbd-fd32-4179-a16c-5f14b7f3e63c" />
