# entregaFinalCoder

El orden en el que se deben probar las cosas es: primero, cargando datos en la base de datos, mediante los formularios los cuales se pueden acceder desde el menú horizontal en la app. Hay un formulario para agregar un usuario, otro para agregar un perfil y otro para agregar un blog. El html respectivo de cada form son: formulario.html, donde agrega un usuario a la base de datos, profile_form.html, donde agrega un perfil a la base de datos, y por último blog_form.html, donde se agrega el título y la descripción del blog. 
En el menú también se encuentra la opción "Buscar Usuario", donde se puede buscar un usuario previamente cargado en la base de datos. Los templates que usa la búsqueda de usuario, son: search_user.html para ingresar el nombre del usuario que se desea buscar y user_list.html donde lista el resultado de la búsqueda.

Por último, en urls.py se encuentran las urls a cada vista, antes de la url se debe agregar App_Components/, y en views están los métodos correspondientes. La rama donde se encuentra lo pedido para la entrega está en la rama Develop.


