import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

# Carregando o dataset Iris
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("Primeiras linhas do dataset:")
print(df.head())

print("\nInformações gerais do dataset:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

print("\nClasses do alvo (0 = Setosa, 1 = Versicolor, 2 = Virginica):")
print(iris.target_names)

from sklearn.model_selection import train_test_split

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("\nTamanho do conjunto de treino:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


model_tree = DecisionTreeClassifier(random_state=42)
model_tree.fit(X_train, y_train)
y_pred_tree = model_tree.predict(X_test)

model_knn = KNeighborsClassifier(n_neighbors=5)
model_knn.fit(X_train, y_train)
y_pred_knn = model_knn.predict(X_test)

model_log = LogisticRegression(max_iter=200)
model_log.fit(X_train, y_train)
y_pred_log = model_log.predict(X_test)

models = {
    "Decision Tree": (y_pred_tree, accuracy_score(y_test, y_pred_tree)),
    "KNN": (y_pred_knn, accuracy_score(y_test, y_pred_knn)),
    "Logistic Regression": (y_pred_log, accuracy_score(y_test, y_pred_log))
}

print("\nResultado da Acurácia:")
for name, (pred, acc) in models.items():
    print(f"{name}: {acc:.4f}")
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, pred))
    print("Relatório de Classificação:")
    print(classification_report(y_test, pred, target_names=iris.target_names))
    print("-" * 50)

# Grafico

scores = [acc for (_, acc) in models.values()]
labels = list(models.keys())

plt.bar(labels, scores, color=['green', 'blue', 'violet'])
plt.ylabel("Acurácia")
plt.title("Comparação entre modelos")
plt.ylim(0,1.1)
plt.show()