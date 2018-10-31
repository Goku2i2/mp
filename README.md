# Mis-Perris
Requisitos:  
-Python  
-get-pip.py  

### Instalación  
-#pip Install Django  
-#pip install django-multiselectfield  

V2  
Reset password completado.

### Crear reporte de Pruebas unitarias:  
-#pip install coverage==4.4  
-Agregar 'coverage' en settings.py  
-#coverage run manage.py test perris -v 2  
-#coverage html  

### Ver los reportes de las pruebas:  
-Ir a la carpeta htmlcov y dentro clickear en el archivo index.html para ver los resultados de las pruebas.  

### Casos de pruebas  

Caso de prueba 1  
ID: CP-01  
Nombre de caso: Validar campos vacíos del registro  
Descripción: Que al registrar usuario se validen todos los campos vacíos del formulario, la cual no pueda registrar atributos null.  
Datos: - Nombre de usuario: Pedro  
       - Rut: 12546789-4  
       - Email:  
       - Teléfono: +56976541290  
       - Región: Valparaíso  
       - Comuna:  
       - Fecha de nacimiento: 21-09-88  
       - Tipo vivienda: Casa con patio pequeño  
       - Contraseña1: ********  
       - Contraseña2: ********  
Resultado esperado: No registrar usuario en la base de datos si hay campos vacíos.  
Resultado obtenido: Validó los campos vacíos, por la cual no registró en la base de datos.  
Resultado de la prueba: Exitoso.  


Caso de prueba 2  
ID: CP-02  
Nombre de caso: Agregar perros en la página.  
Descripción: Registrar satisfactoriamente todos los atributos de los perros rescatados.  
Datos: - Fotografía: spike.jpg  
       - Nombre de perro: Spike  
       - Raza: Boxer  
       - Descripción: Es muy tranquilo dentro de casa, le gusta jugar con su hueso favorito.  
       - Estado: Disponible  
Resultado esperado: Añadir perro a la base de datos y se muestre perfectamente en la página.  
Resultado obtenido: Todos los atributos fueron registrados satisfatoriamente en la base de datos y se muestra perfectamente en la página web.  
Resultado de la prueba: Exitoso.   