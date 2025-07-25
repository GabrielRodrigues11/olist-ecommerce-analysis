# 📦 Análise de Dados - Olist E-commerce

Este projeto tem como objetivo analisar o comportamento de vendas do e-commerce brasileiro utilizando o dataset público da Olist. Através de Python e bibliotecas de análise de dados, foram extraídas informações valiosas sobre clientes, pedidos, vendedores, produtos e pagamentos.

---

## 📊 Objetivos

- Investigar o comportamento de vendas no e-commerce.
- Analisar desempenho dos vendedores e categorias.
- Entender padrões de pagamento e atrasos nas entregas.

---

## 📁 Estrutura do Projeto

```
olist_projeto/
├── notebooks/
│ ├── 01_analise_inicial_olist.ipynb
│ └── dados/
│   └── *.csv
├── outputs/
│ └── *.png
├── scripts/
│ ├── carregar_dados.py
│ └── pycache/
└── README.md
```

---


## 🧰 Tecnologias Utilizadas

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📊 Análises Realizadas

As análises foram divididas em etapas organizadas e reproduzíveis:

### 1. 📥 Carregamento de Dados

Todos os arquivos CSV foram importados com tratamento de tipos e dados nulos usando um script modular `scripts/carregar_dados.py`.

### 2. 🔍 Exploração e Limpeza

- Verificação e remoção de valores nulos
- Conversão de tipos de dados (como datas)
- Merge de tabelas para análise integrada

### 3. 📈 Análises e Gráficos

Abaixo os principais gráficos gerados (todos estão salvos na pasta `/outputs`):

| Gráfico | Descrição |
|--------|-----------|
| `top_10_vendedores_por_numeros_de_pedidos.png` | Top 10 vendedores com mais pedidos |
| `pagamentos_por_tipo.png` | Distribuição dos meios de pagamento utilizados |
| `top_10_cidades_por_pedidos.png` | Cidades com maior volume de pedidos |
| `top_10_produtos_mais_pedidos.png` | Produtos mais vendidos por ID e categoria |
| `top_10_categorias_pedidos.png` | Categorias mais pedidas |
| `pedidos_com_sem_atrasos.png` | Comparativo entre pedidos entregues no prazo e com atraso |
| `volume_pedidos_mensais.png` | Evolução do volume de pedidos ao longo dos meses |

---

## 📖 Fonte dos Dados

- Dataset: [Brazilian E-Commerce Public Dataset by Olist - Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data)

---

## 📌 Principais Insights

- A maioria dos pagamentos são feitos com **cartão de crédito**.
- Grande parte dos atrasos ocorre em pedidos de certas **cidades mais remotas**.
- Algumas **categorias de produtos** são extremamente populares, mesmo com alto índice de devolução.
- O volume de pedidos tem **tendência de crescimento** constante ao longo dos meses analisados.

---

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/GabrielRodrigues11/olist-ecommerce-analysis.git
```

## 💼 Autor

**Gabriel Rodrigues**  
Analista de TI em transição para a área de dados. Apaixonado por tecnologia e por transformar dados em soluções visuais e práticas.
