# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
import time

try:
    client = OpenAI(api_key="sk-b006b3d70f714fb58fd4c204b50703dd", base_url="https://api.deepseek.com")
    print('Iniciando conexão com a API...')
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    ) #test commit
    print(response.choices[0].message.content)

except Exception as e:
    print("\nErro encontrado:")
    if "Insufficient Balance" in str(e):
        print("❌ Saldo insuficiente na sua conta da API DeepSeek")
        print("Por favor, adicione créditos à sua conta ou verifique seu saldo atual.")
    else:
        print(f"❌ Erro: {str(e)}")
    
    print("\nPressione qualquer tecla para tentar novamente...")
    time.sleep(2)  # Pequena pausa para melhor legibilidade