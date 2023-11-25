<img style="display: block; margin-left: auto; margin-right: auto; width: 20%;" src="https://www.upc.edu.pe/static/img/logo_upc_red.png" alt="UPC Logo">

<main>
<section id="caratula" style="text-align: center; font-size: 17px; color: white;">
<p style="font-weight: bold;">UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS</p>
<p>Carrera de Ciencias de la Computación</p>
<p style="font-weight: bold;">" DAMOS SHELL"</p>
<p>Teoría de compiladores</p>
<p>Integrantes:<p>
<li>David Joaquín Niño Suárez</li>
<li>Mauro Imanol Obermeyer Adauto Angulo</li>
<li>Jair Stephano Rodríguez Calla</li>
<p>Link de Video de Exposición:</p>
<li>https://drive.google.com/file/d/1Qf1L6qiFtUb4g9PB8AREL9a03DW_kZeW/view?usp=sharing</li>
<p style="padding: 10px;">Lima, 2023</p>
</section>
<h2></h2>
<h2>Introducción</h2>
    <p>
        El presente informe detalla el desarrollo de una shell interactiva en el lenguaje de programación Python,
        implementada en el entorno del sistema operativo Debian 12. La shell proporciona una interfaz de línea de
        comandos que permite a los usuarios interactuar con el sistema mediante la ejecución de comandos,
        asignación de variables y otras funcionalidades avanzadas.
    </p>
<h2>Objetivos</h2>
    <ul>
        <li>Practicar la gestión del tiempo durante las presentaciones, asegurándose de cubrir todos los puntos importantes de manera adecuada y dejar tiempo para preguntas y discusiones.</li>
        <li>Integrar de manera efectiva el manejo de colores como característica adicional en el desarrollo de interfaces de usuario para aplicaciones de software, con el fin de mejorar la experiencia del usuario y facilitar la interpretación visual de la información.</li>
        <li>Fomentar la colaboración efectiva entre los miembros del equipo, asegurando una distribución equitativa de tareas, una comunicación clara y regular, y la implementación de buenas prácticas de desarrollo de software.</li>
        <li>Explorar y comprender a fondo las funcionalidades de las librerías OS de Python para asegurar una integración eficiente con el sistema operativo. Investigar las mejores prácticas para el manejo de procesos, manipulación de archivos, y gestión de variables de entorno.</li>
    </ul>
<h2>Desarrollo del programa</h2>
<h3>Caracteristicas principales</h3>
    <ul>
        <li><strong>Interactividad:</strong> La shell permite a los usuarios ingresar comandos de forma interactiva y ver los resultados en tiempo real.</li>
        <li><strong>Asignación de Variables:</strong> Permite asignar y gestionar variables dentro de la shell, facilitando el almacenamiento y reutilización de valores.</li>
        <li><strong>Ejecución de Comandos del Sistema:</strong>La shell es capaz de ejecutar comandos del sistema operativo, proporcionando una interfaz para interactuar con el entorno subyacente.</li>
    </ul>
<h3>Métodos</h3>
    <ul>
        <li><strong>run_command:</strong> Ejecuta un comando del sistema operativo.</li>
        <li><strong>parse_if_statement:</strong> Analiza una instrucción condicional y devuelve la condición evaluada.</li>
        <li><strong>parse_switch_statement:</strong> Analiza una instrucción de cambio y devuelve la expresión de cambio y la expresión del caso.</li>
        <li><strong>parse_assignment:</strong> Analiza una cadena que representa una asignación de variable y actualiza el diccionario de variables.</li>
        <li><strong>set_environment_variable:</strong> Establece una variable de entorno y actualiza el prompt si es necesario.</li>
        <li><strong>show_environment_variables:</strong> Muestra las variables de entorno actuales.</li>
        <li><strong>update_prompt:</strong> Actualiza el valor del prompt según la variable de entorno 'PROMPT'.</li>
        <li><strong>run_list:</strong> Ejecuta una lista de comandos.</li>
        <li><strong>run_list_save:</strong> Guarda una lista de comandos en un archivo binario.</li>
        <li><strong>run_list_load:</strong> Carga una lista de comandos desde un archivo binario.</li>
        <li><strong>run_for_loop:</strong> Ejecuta un bucle for con un rango dado y una lista de comandos.</li>
        <li><strong>run_script:</strong> Ejecuta un script almacenado en un archivo.</li>
        <li><strong>system_cmd:</strong> Permite ejecutar comandos de sistema.</li>
        <li><strong>interactive_mode:</strong> Modo interactivo que permite al usuario ingresar comandos y ejecutarlos.</li>
        <li><strong>main:</strong> Punto de entrada principal del programa.</li>
    </ul>
<h2>Conclusiones</h2>
    <ul>
        <li>Desarrollar un proyecto como una shell con un conjunto complejo de características requiere una colaboración efectiva y coordinada entre los miembros del grupo. En este sentido, hemos aprendido que la comunicación clara y la asignación adecuada de tareas son fundamentales para el éxito del proyecto. La distribución equitativa de responsabilidades según las fortalezas individuales ha permitido maximizar la eficiencia y la calidad del código producido. Además, la implementación de reuniones regulares y el uso de herramientas de gestión de proyectos han facilitado el seguimiento del progreso y la resolución oportuna de problemas.</li>
        <li>En conclusion, la habilidad de gestionar el tiempo durante las presentaciones no solo asegura la cobertura completa de puntos esenciales en proyectos de ingeniería de software, sino que también reserva tiempo valioso para preguntas y discusiones. Este enfoque eficiente no solo mejora la comunicación, sino que también fomenta la participación activa y la retroalimentación, promoviendo un ambiente colaborativo y enriquecedor para el desarrollo del proyecto. La gestión del tiempo no es solo práctica, sino una herramienta clave para el éxito en la comunicación y la colaboración efectiva.</li>
    </ul>
</main>
