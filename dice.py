import random

def rolar_dado(faces, quantidade=1):
    return [random.randint(1, faces) for _ in range(quantidade)]

def rolar_dados():
    print("Bem-vindo ao rolagem de dados para RPG!")
    
    # Variável para armazenar os dados e quantidades
    dados_para_rolar = []
    
    # Pergunta o tipo e quantidade de dados até o usuário parar
    while True:
        try:
            # Receber a quantidade de faces
            faces = int(input("Digite o número de faces do dado (4, 6, 8, 10, 12, 20, 100) ou 0 para finalizar: "))
            if faces == 0:
                break
            if faces not in [4, 6, 8, 10, 12, 20, 100]:
                print("Número de faces inválido! Escolha entre 4, 6, 8, 10, 12, 20, 100.")
                continue
            
            # Receber a quantidade de dados do tipo escolhido
            quantidade = int(input(f"Quantos d{faces} você deseja rolar? "))
            dados_para_rolar.append((faces, quantidade))
        
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
    
    # Receber um modificador opcional
    try:
        modificador = int(input("Digite um modificador a ser somado ao total (ou 0 se não quiser): "))
    except ValueError:
        print("Entrada inválida! Usando modificador = 0.")
        modificador = 0
    
    # Rolar todos os dados
    total_geral = 0
    resultados = []
    
    for faces, quantidade in dados_para_rolar:
        rolagens = rolar_dado(faces, quantidade)
        total = sum(rolagens)
        resultados.append((faces, rolagens, total))
        total_geral += total
    
    # Adicionar o modificador ao total final
    total_geral += modificador
    
    # Exibir os resultados
    print("\n--- Resultados das Rolagens ---")
    for faces, rolagens, total in resultados:
        print(f"{quantidade}d{faces}: {rolagens} (Total: {total})")
    print(f"Modificador: {modificador}")
    print(f"Resultado Final (com modificador): {total_geral}")

# Executa a função
rolar_dados()