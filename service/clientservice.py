import repository.database as db
from model.client import Client


def find_all():
    columns = db.select_all_clients()
    client_list = []
    for c in columns:
        client_list.append(Client(c[0], c[1], c[2]))
    return client_list


def find_custom(column, value):
    columns = db.select_by_column(column, value)
    client_list = []
    for c in columns:
        client_list.append(Client(c[0], c[1], c[2]))
    return client_list


def save(client):
    if has_numbers(client.name):
        return False
    db.save_client(client)
    return True


def delete(cnpj):
    db.delete_client(cnpj)
    return True


def update(client):
    db.update_client(cnpj=client.cnpj, name=client.name, address=client.address)


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

