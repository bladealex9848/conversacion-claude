# Import necessary libraries
# Importar las bibliotecas necesarias
import anthropic
import os
from colorama import Fore, Style
import textwrap

# Conversation class to manage the conversation with Claude
# Clase Conversation para manejar la conversación con Claude
class Conversation:
    def __init__(self, client):
        self.client = client
        self.history = []

    # Add a message to the conversation history
    # Agregar un mensaje al historial de la conversación
    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    # Get the conversation history
    # Obtener el historial de la conversación
    def get_history(self):
        return self.history

    # Send a message to Claude and receive a response
    # Enviar un mensaje a Claude y recibir una respuesta
    def send_message(self, message):
        self.add_message("user", message)
        response = self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4096,
            messages=self.get_history()
        )
        message_content = ""
        for content_block in response.content:
            if content_block.type == "text":
                message_content += content_block.text
            elif content_block.type == "code":
                message_content += f"\n```\n{content_block.code}\n```\n"
        self.add_message("assistant", message_content)
        return message_content

# Format the assistant's response text
# Formatear el texto de respuesta del asistente
def format_text(text, width=80):
    paragraphs = text.split("\n")
    formatted_paragraphs = []
    for paragraph in paragraphs:
        formatted_paragraph = textwrap.fill(paragraph, width=width)
        formatted_paragraphs.append(formatted_paragraph)
    return "\n".join(formatted_paragraphs)

# Main function to run the conversation
# Función principal para ejecutar la conversación
def main():
    # Get the API key from the environment variable or use a default value
    # Obtener la clave API de la variable de entorno o usar un valor predeterminado
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        api_key = "tu_clave_api_real_aqui"

    # Create an Anthropic client and a Conversation instance
    # Crear un cliente de Anthropic y una instancia de Conversation
    client = anthropic.Anthropic(api_key=api_key)
    conversation = Conversation(client)

    # Print a welcome message
    # Imprimir un mensaje de bienvenida
    print(Fore.YELLOW + "¡Bienvenido a la conversación con Claude! Escribe 'salir' para finalizar." + Style.RESET_ALL)

    # Main conversation loop
    # Bucle principal de la conversación
    while True:
        # Get user input
        # Obtener la entrada del usuario
        user_input = input(Fore.GREEN + "Usuario: " + Style.RESET_ALL)
        if user_input.lower() == 'salir':
            break

        # Send user message to Claude and receive a response
        # Enviar el mensaje del usuario a Claude y recibir una respuesta
        assistant_response = conversation.send_message(user_input)
        
        # Format the assistant's response and print it
        # Formatear la respuesta del asistente e imprimirla
        formatted_response = format_text(assistant_response)
        print(Fore.CYAN + "Asistente: " + Style.RESET_ALL + formatted_response)

# Run the main function if the script is executed directly
# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()