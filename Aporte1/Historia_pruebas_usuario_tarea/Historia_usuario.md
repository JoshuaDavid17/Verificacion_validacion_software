## Historia de usuario:

### JIRA BD001 – Registro de usuarios

Como visitante de la plataforma, <br>
quiero registrarme creando una cuenta <br>
para poder acceder a las funcionalidades del sistema.

### Criterios de aceptación:

- El sistema debe solicitar datos obligatorios: nombre, apellido, correo y contraseña.
- El correo debe ser validado para evitar duplicados.
- La contraseña debe cumplir con reglas mínimas de seguridad.
- El sistema debe enviar un correo de confirmación después del registro.
- El usuario debe ser notificado si algún dato es inválido.

Tipo de usuario: Visitante / Nuevo usuario <br>
Prioridad: Alta <br>
Valor: Permite que nuevos usuarios ingresen y utilicen los servicios del sistema.

### JIRA BD002 – Página de Login

Como usuario registrado, <br> 
quiero iniciar sesión con mi correo y contraseña <br> 
para acceder a mi cuenta de manera segura.

### Criterios de aceptación:

- La página debe permitir ingresar correo y contraseña.
- El sistema debe validar credenciales antes de iniciar sesión.
- Debe existir un enlace para recuperar contraseña.
- Si las credenciales son incorrectas, el sistema debe mostrar un mensaje claro al usuario.
- El login debe redirigir al usuario a la página principal del sistema.

Tipo de usuario: Usuario registrado <br>
Prioridad: Alta  <br>
Valor: Permite el acceso seguro a las funcionalidades personalizadas del sistema.

### JIRA BD003 – Funcionalidad de la página

Como usuario, <br> 
quiero que la página principal muestre las funcionalidades disponibles <br> 
para poder navegar y usar el sistema fácilmente.

### Criterios de aceptación:

- La página debe mostrar un menú con las principales opciones (ej. Dashboard, Perfil, Configuración, etc.).
- Los elementos del menú deben ser visibles según el rol del usuario.
- Las secciones deben cargarse correctamente al seleccionarlas.
- El diseño debe ser responsivo en dispositivos móviles y escritorio.
-Los mensajes de error deben mostrarse claramente si alguna funcionalidad falla.

Tipo de usuario: Usuario registrado  <br>
Prioridad: Media  <br>
Valor: Facilita el uso del sistema de manera intuitiva y ordenada.

### JIRA BD004 – Navegación

Como usuario, <br> 
quiero poder navegar entre las diferentes páginas del sistema de forma rápida y sencilla <br> 
para encontrar lo que necesito sin complicaciones.

### Criterios de aceptación:

- El sistema debe permitir ir hacia atrás o adelante sin perder información.
- El menú debe ser accesible desde cualquier página del sistema.
- Cada sección debe cargarse en menos de 3 segundos.
- Los enlaces deben estar correctamente etiquetados y funcionar sin errores.
- Debe existir una ruta clara de navegación.

Tipo de usuario: Usuario registrado  <br>
Prioridad: Media  <br>
Valor: Mejora la experiencia del usuario al facilitar el desplazamiento dentro del sistema.
