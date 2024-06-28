#ATIVIDADE 1013 Greatest

a, b , c = map(int,input().split())

maiorAB = (a + b + abs(a-b))/2                  #Esta equação vai descobrir o maior valor entre "a" e "b".
maior = (maiorAB + c + abs(maiorAB - c))/2      #Esta equação vai descobrir o maior valor entre o maiorAB e "c".
                                                #A parte abs(a - b) garante que a diferença entre a e b seja ->
print(f"{maior:.0f} eh o maior")                       #positiva, independentemente de qual seja o maior. Isso permite que a fórmula funcione corretamente

                    