import requests
from bs4 import BeautifulSoup
import time


def get_table_content(url, table_class):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Solicitação com Sucesso")
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', class_=table_class)
            if table:
                return str(table)
            else:
                print("Tabela não encontrada.")
                return None
        else:
            print("Falha ao obter o conteúdo da página. Status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Erro durante a solicitação:", e)
        return None


def main():
    url = "https://institutoconsulplan.org.br/getConc.aspx?key=ZREMx3O8jKI="
    table_class = "table"
    previous_table_content = get_table_content(url, table_class)
    if previous_table_content is None:
        return

    while True:
        time.sleep(60)
        current_table_content = get_table_content(url, table_class)
        if current_table_content != previous_table_content:
            print("A tabela mudou!")
            break


if __name__ == "__main__":
    main()
