candidatos = [
['candidato 1' , 'e5_t10_p8_s8'],
['candidato 2' , 'e10_t7_p7_s8'],
['candidato 3' , 'e8_t5_p4_s9'],
['candidato 4' , 'e2_t2_p2_s1'],
['candidato 5' , 'e10_t10_p8_s9'],
]

def buscar_candidato(candidatos, entrevista, teorico, pratico, soft):
    candidatos_aprovados = []
    for candidato, resultado in candidatos:
        notas = resultado.split('_')
        e = int(notas[0][1:])
        t = int(notas[1][1:])
        p = int(notas[2][1:])
        s = int(notas[3][1:])
        if e >= entrevista and t >= teorico and p >= pratico and s >= soft:
            candidatos_aprovados.append(candidato)
            return candidatos_aprovados
        
entrevista = int(input("Qual a nota mínima necessária da entrevista [e]? "))

teorico = int(input("Qual a nota mínima necessária para o teste teórico [t]? "))

pratico = int(input("Qual a nota mínima necessária para o teste prático [p]? "))

soft = int(input("Qual a nota mínima necessária para o soft skills [s]? "))

candidatos_aprovados = buscar_candidato(candidatos, entrevista, teorico, pratico, soft) # LISTA

if candidatos_aprovados:
   print("Candidatos Aprovados: ")
   for candidato in candidatos_aprovados:
      print(candidato)

else:
    print("Não há candidatos compatíveis: ")
 
