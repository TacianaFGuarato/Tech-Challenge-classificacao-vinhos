from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


def treinar_regressao_logistica(X_train, y_train):
    """
    Treina um modelo de Regressão Logística.
    """

    modelo = LogisticRegression(
        random_state=42,
        max_iter=1000
    )

    modelo.fit(X_train, y_train)

    return modelo


def treinar_knn(X_train, y_train, n_neighbors=5):
    """
    Treina um modelo KNN.
    """

    modelo = KNeighborsClassifier(
        n_neighbors=n_neighbors
    )

    modelo.fit(X_train, y_train)

    return modelo


def treinar_random_forest(X_train, y_train):
    """
    Treina um modelo Random Forest.
    """

    modelo = RandomForestClassifier(
        random_state=42
    )

    modelo.fit(X_train, y_train)

    return modelo


def realizar_predicao(modelo, X_test):
    """
    Retorna as classes previstas.
    """

    return modelo.predict(X_test)


def calcular_probabilidades(modelo, X_test):
    """
    Retorna as probabilidades da classe positiva.
    """

    return modelo.predict_proba(X_test)[:, 1]