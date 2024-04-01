# Definindo a lista de resultados dos candidatos
resultadosCandidatos = [
    ("candidato 1", "e5_t10_p8_s8"),
    ("candidato 2", "e10_t7_p7_s8"),
    ("candidato 3", "e8_t5_p4_s9"),
    ("candidato 4", "e2_t2_p2_s1"),
    ("candidato 5", "e10_t10_p8_s9")
]

# Função para buscar candidatos com notas maiores ou iguais às especificadas pelo usuário
def buscarCandidatos(notasMinimas):
    candidatosSelecionados = []
    for candidato, resultado in resultadosCandidatos:
        notasCandidato = resultado.split("_")
        notasCandidato = [int(nota[1:]) for nota in notasCandidato]  
        if all(notaCandidato >= notaMinima for notaCandidato, notaMinima in zip(notasCandidato, notasMinimas)):
            candidatosSelecionados.append(candidato)
    return candidatosSelecionados

# Função principal
def main():
    # Solicitando as notas mínimas ao usuário
    eMin = int(input("Digite a nota mínima de entrevista: "))
    tMin = int(input("Digite a nota mínima de teste teórico: "))
    pMin = int(input("Digite a nota mínima de teste prático: "))
    sMin = int(input("Digite a nota mínima de avaliação de soft skills: "))
    
    notasMinimas = [eMin, tMin, pMin, sMin]
    
    # Buscando candidatos com notas maiores ou iguais às especificadas
    candidatosSelecionados = buscarCandidatos(notasMinimas)
    
    # Exibindo os candidatos selecionados
    if candidatosSelecionados:
        print("Candidatos Selecionados: ")
        for candidato in candidatosSelecionados:
            print(candidato)
    else:
        print("Não há candidatos compatíveis com os critérios fornecidos. ")

if __name__ == "__main__":
    main()
