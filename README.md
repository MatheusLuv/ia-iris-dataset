<h1 align="center">📘 Atividade de Inteligência Artificial – UNIRIOS</h1>

**Disciplina:** Inteligência Artificial<br>
**Professor:** Ronierison de Souza Maciel<br>
**Aluno:** Anthony dos Santos Martins<br>
**Curso:** Sistemas de Informação – VI Período, Noturno<br>

### Objetivo da Atividade

Implementar e comparar algoritmos de **classificação supervisionada** utilizando um dataset real, aplicando técnicas de pré-processamento, modelagem e avaliação de desempenho.

## 📊 Dataset Escolhido

Fonte: `sklearn.datasets.load_iris`

Descrição: O dataset contém medidas de 150 flores, divididas em três espécies: *Setosa*, *Versicolor* e *Virginica*.

Tamanho: 150 amostras × 4 features.

Variável alvo: espécie da flor (3 classes).

Features: 
- Comprimento da sépala (cm)  
- Largura da sépala (cm)  
- Comprimento da pétala (cm)  
- Largura da pétala (cm) 

Justificativa da escolha:
O Iris é um dos datasets clássicos mais utilizados em aprendizado de máquina. Ele é bom também para quem tá começando a estudar a área de dataset e IA.

## 📈 Resultados Obtidos

***Decision Tree:***

    Acurácia: 0.933
    Precisão média: 0.94
    Matriz de Confusão:
    [15  0  0]
    [ 0 12 13]
    [ 0  0 15]

***KNN:***

    Acurácia: 0.978
    Precisão média: 0.98
    Matriz de Confusão:
    [15  0  0]
    [ 0 15  0]
    [ 0  1 14]

***Logistic Regression:***

    Acurácia: 0.933
    Precisão média: 0.93
    Matriz de Confusão:
    [15  0  0]
    [ 0 14  1]
    [ 0  2 13]

## 📝 Conclusão (resumida)

O modelo com melhor desempenho no dataset Iris foi o **KNN**, que alcançou a maior acurácia (**97,8%**) entre os algoritmos testados.  

Esse resultado faz sentido, pois o dataset é pequeno, balanceado e apresenta classes bem separáveis no espaço das variáveis. O KNN funciona bem nesse cenário, já que a classificação é feita com base na proximidade entre amostras.  

Para melhorar os modelos, poderiam ser aplicadas:
- **Normalização dos dados** (especialmente para o KNN).  
- **Tuning de hiperparâmetros** (número de vizinhos no KNN, profundidade da árvore, regularização na regressão logística).  
- **Validação cruzada** para maior robustez na avaliação.

## 💻 Como Executar

### Clone este repositório:

    git clone https://github.com/MatheusLuv/ia-iris-dataset.git


### Instale as dependências:

    pip install pandas matplotlib seaborn



### Execute no Terminal:

    py iris_classificacao.py