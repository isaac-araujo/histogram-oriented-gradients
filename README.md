# histogram-oriented-gradients

Individual - Valor 1.0 ponto.
Formato da entrega: repositorio git.
Data da entrega:
08/06/2023 - 23:59
Para este trabalho o aluno pode escolher uma das duas opções de entrega que deseja fazer.
Implementação do algoritmo para descritor HoG sem utilização de bibliotecas e métodos prontos.
Implementação de um classificador utilizando a biblioteca pronta para HoG.

Especificação do HoG (SEM BIBLIOTECA)

IImplementação do algoritmo para descritor HoG (não utilizar bibliotecas prontas para o algoritmo - magnitude, orientação e histogramas precisam ser feito manualmente)
Seguir o algoritmo proposto para gerar o descritor para as imagens.
Salve os valores finais do descritor HoG.
Salve 5 imagens com as orientações nos histogramas das células mapeadas no começo do algoritmo.
Todo o código e as imagens precisam estar versionadas.
Passo a passo para construção do algoritmo AQUI no slide 41

---



1. Redimensione a imagem (altura e largura) para um múltiplo de 8.
2. Achar a magnitude e orientação de cada pixel
3. 1. Magnitude => Dx e Dy com os filtros 1x3 e 3x1
   2. Orientação => Função arctan (Dx/Dy)
4. Dividir a imagem em células de 8x8 pixels
5. A cada célula pega a magnitude e orientação (128 valores por célula)
6. Para cada célula 8x8, calcula-se um histograma de orientações.
7. Padrão: 9 faixas (passos de 20 graus).
8. Distribua o valor da magnitude de cada pixel da célula em até 2 faixas do histograma (exemplo slide 34)
9. Agrupe 4 células em um bloco 16x16 (2 células de largura e 2 de altura)
10. Bloco => 4 histogramas, com 9 faixas cada = 36 valores por bloco
11. Normalize os valores de cada bloco utilizando L2
12. Calcular a raiz da soma de todos os valores ao quadrado, e então dividir todos os valores por este resultado
13. Descrito Hog é a concatenação dos valores normalizados de cada bloco.
14. Para visualizá-lo utiliza-se as orientações nos histogramas das células, feito no passo 3.
