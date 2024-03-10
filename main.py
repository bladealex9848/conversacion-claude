import anthropic
import os

# Obtener la clave API de la variable de entorno
api_key = os.environ.get("ANTHROPIC_API_KEY")
#print(f"Clave API: {api_key}")  # Imprime el contenido de api_key

# Si la variable de entorno no está configurada, debes proporcionar la clave API directamente
if not api_key:
    api_key = "tu_clave_api_real_aqui"  # Reemplaza esta línea con tu clave API real

try:
    client = anthropic.Anthropic(api_key=api_key)
except Exception as e:
    print(f"Error al crear el cliente Anthropic: {e}")
    exit()

try:
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": "Hola, Claude"}
        ]
    )

    # Formatear el mensaje resultante
    message_content = ""
    for content_block in response.content:
        if content_block.type == "text":
            message_content += content_block.text
        elif content_block.type == "code":
            message_content += f"\n```\n{content_block.code}\n```\n"
        # Puedes agregar más casos para manejar otros tipos de bloques de contenido

    print(message_content)

except Exception as e:
    print(f"Error: {e}")