
# Conversación con Claude de Anthropic

Este proyecto es una interfaz de línea de comandos para mantener conversaciones con el asistente de Anthropic llamado Claude. Utiliza la API de Anthropic para enviar mensajes y recibir respuestas del asistente.

## Requisitos

- Python 3.6 o superior
- Biblioteca `anthropic`
- Biblioteca `colorama`

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/conversacion-claude.git
   ```
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Configura tu clave API de Anthropic:
   - Establece la variable de entorno `ANTHROPIC_API_KEY` con tu clave API, o
   - Reemplaza `"tu_clave_api_real_aqui"` en el script con tu clave API real.

## Uso

Ejecuta el script `conversation.py`:
```
python conversation.py
```
Escribe tus mensajes en el terminal y presiona Enter para enviarlos. El asistente responderá con una nueva línea.

Para finalizar la conversación, escribe 'salir'.

## Funcionamiento detallado

El script `conversation.py` utiliza la biblioteca `anthropic` para interactuar con la API de Anthropic y mantener una conversación con el asistente de IA Claude. Aquí se detalla el proceso:

1. Importa las bibliotecas necesarias: `anthropic`, `os`, `colorama` y `textwrap`.
2. Define la clase `Conversation`, que gestiona la conversación con Claude. Esta clase tiene métodos para agregar mensajes al historial, obtener el historial completo y enviar mensajes a Claude para recibir respuestas.
3. Utiliza la función `format_text` para formatear el texto de respuesta del asistente, dividiendo el texto en párrafos y ajustando el ancho de línea para una mejor legibilidad.
4. En la función principal `main`, obtiene la clave API de Anthropic de una variable de entorno o utiliza un valor predeterminado.
5. Crea una instancia del cliente de Anthropic y una instancia de la clase `Conversation`.
6. Inicia un bucle de conversación donde el usuario ingresa mensajes y recibe respuestas formateadas de Claude. Continúa hasta que el usuario escribe 'salir'.
7. Cada mensaje del usuario se envía a Claude utilizando el método `send_message` de la clase `Conversation`. La respuesta de Claude se formatea y se muestra en la terminal.
8. El script aplica colores y estilos al texto en la terminal utilizando la biblioteca `colorama`, mejorando la experiencia de usuario.

## Glosario de términos

- **API (Application Programming Interface):** Un conjunto de reglas y protocolos para la comunicación entre diferentes sistemas o aplicaciones de software.
- **Anthropic:** Empresa de investigación en inteligencia artificial, desarrolladora del asistente IA Claude.
- **Claude:** Asistente de IA capaz de mantener conversaciones y responder a consultas.
- **Clave API:** Cadena única utilizada para autenticar y autorizar el acceso a una API.
- **Biblioteca:** Conjunto de código que proporciona funcionalidades adicionales para facilitar el desarrollo de software.
- **Variable de entorno:** Variable dinámica en el entorno de ejecución del sistema operativo.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
