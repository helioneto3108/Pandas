def gerar_histograma(
    data_frame,
    variavel,
    bins=30,
    color="red",
    xlabel="Variável",
    ylabel="Frequência",
    titulo="Histograma",
    fontsize=15,
    fontweight="bold",
    figsize=(8, 5),
):
    fig, ax = plt.subplots(figsize=figsize)
    ax.hist(data_frame[variavel], bins=bins, color=color)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    ax.set_title(titulo, fontsize=fontsize, fontweight=fontweight)


def gerar_painel_barra(
    data_frame,
    var,
    hue,
    title="",
    title_subplot_1="",
    title_subplot_2="",
    legend_subplot_2="",
    xlabel="Quantidade",
    ylabel="",
    figsize=(12, 6),
):
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    sns.countplot(data=data_frame, y=var, ax=ax[0])
    sns.countplot(data=data_frame, y=var, hue=hue, ax=ax[1])
    ax[0].set(ylabel=ylabel, xlabel=xlabel, title=title_subplot_1)
    ax[1].set(ylabel=ylabel, xlabel=xlabel, title=title_subplot_2)
    ax[1].legend(title=legend_subplot_2)
    fig.suptitle(title)
    fig.tight_layout(pad=4)


def box_plot(data, title, xlabel, ylabel, figsize=(12, 5)):
    fig, ax = plt.subplots(figsize=figsize)
    sns.boxplot(data=data, ax=ax)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)


def boxplot_por_filtro(filtro, data_frame, order=None):
    "Gera um boxplot com filtro para o eixo x e a variável no eixo y."
    provas = ["MATEMATICA", "CIENCIAS_NATUREZA", "LINGUAGENS", "HUMANAS", "REDACAO"]
    filtro_tratado = " ".join(filtro.split("_")).capitalize()

    for prova in provas:
        prova_nome_minusculo = prova.lower()
        fig, ax = plt.subplots(figsize=(15, 5))
        sns.boxplot(x=filtro, y=prova, data=data_frame, ax=ax, order=order)
        ax.set(
            xlabel=filtro_tratado,
            ylabel=f"Nota em {prova_nome_minusculo}",
            title=f"Nota em {prova_nome_minusculo} filtrada por {filtro_tratado}",
        )


def check_missing(df):
    import pandas

    if isinstance(df, pandas.core.frame.DataFrame):
        return (((df.isnull().sum() / df.shape[0]) * 100).round(2)).sort_values(
            ascending=False
        )
    return None


def show_percentage_missing(df):
    import matplotlib.pyplot as plt

    missing = check_missing(df)
    plt.figure(figsize=(10, 20))
    plt.barh(
        y=missing.index,
        width=missing.values,
        color="darkgray",
        height=0.7,
        align="edge",
    )
    plt.xlabel("% of missing values", size=10)
    plt.ylabel("Columns", size=10)
    plt.title(
        "Missing Values", fontdict={"color": "gray", "weight": "bold", "size": 12}
    )
    plt.grid(alpha=0.5)
    plt.show()


def feature_plot_stat(feature, data):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f"Univariate analysis for {feature}")
    sns.histplot(data[feature], kde=True, ax=ax[0])
    ax[0].set_xlabel("Distribution of " + feature)
    sns.boxplot(y=data[feature], ax=ax[1])
    sns.violinplot(x=data[feature], ax=ax[2])
    fig.tight_layout(pad=3)


def univariate_analysis(features: list, data=pd.DataFrame):
    for feature in features:
        feature_plot_stat(feature, data)
