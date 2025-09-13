`1. Explique com suas palavras o que significa classificação supervisionada?`<br>
Classificação supervisionada é uma técnica de aprendizado de máquina em que o modelo é treinado usando um conjunto de dados.
Ou seja, cada amostra de treino possui seus atributos e também a classe correta (rótulo).
O objetivo do modelo é aprender a relação entre os atributos e os rótulos, para depois conseguir prever corretamente a classe de novas amostras nunca vistas.
**Por exemplo:** prever se um e-mail é spam ou não-spam com base em e-mails previamente classificados.

`2. Qual é a importância de dividir o dataset em conjunto de treino e teste?`<br>
O conjunto de treino serve para o modelo aprender os padrões existentes nos dados. O conjunto de teste é usado para verificar se o modelo realmente generaliza bem, se ele consegue fazer previsões corretas em dados que nunca viu antes.
Se Se usássemos os mesmos dados para treinar e testar, poderia ocorre de o modelo "decora" os exemplos em vez de aprender os padrões.

`3. Qual a diferença entre Decision Tree e KNN em termos de funcionamento?`<br>
A principal diferença é como eles tomam suas decisões e como aprendem com dados recebidos.
- **<u>Decision Tree:</u>** Ele cria uma estrutura em forma de árvore, onde em cada nó é feito uma pergunta sobre uma feature, em cada divisão os dados são separados de acordo com a resposta. A partir  dessas decisões o modelo segue um caminho até chegar na classificação final.
- **<u>KNN (K-Nearest Neighbors):</u>** O KNN não cria um modelo, para classificar um novo ponto, algoritmo olha para os "K" que são chamados de vizinhos mais próximos e decide com base nas classes desses vizinhos.
