from json import dumps

pessoa = {
    'nome': 'Creiso',
    'sobrenome': 'Cardosao',
    'dta_nascimento': '19/02/1998',
    'peso': 85.9,
    'sexo': 'F'
}

print(dumps(pessoa))
