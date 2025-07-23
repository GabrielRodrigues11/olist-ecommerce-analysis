import pandas as pd
import os

def carregar_csv(nome_arquivo, pasta='dados'):
    caminho = os.path.join(pasta, nome_arquivo)
    return pd.read_csv(caminho)

def carregar_todos():
    return{
        'orders': carregar_csv('olist_orders_dataset.csv'),
        'order_items': carregar_csv('olist_order_items_dataset.csv'),
        'customers': carregar_csv('olist_customers_dataset.csv'),
        'products': carregar_csv('olist_products_dataset.csv'),
        'sellers': carregar_csv('olist_sellers_dataset.csv'),
        'payments': carregar_csv('olist_order_payments_dataset.csv'),
        'reviews': carregar_csv('olist_order_reviews_dataset.csv'),
        'categories': carregar_csv('product_category_name_translation.csv')
    }