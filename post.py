from flask import Flask, request

app = Flask(__name__)

# Dicionário de livros
livros = {
    "1": {
        "título": "O Segredo do Vale",
        "autor_id": "1",
        "ano_publicacao": 2018,
        "gênero": "Ficção",
        "preco": 45.90
    },
    "2": {
        "título": "Viagem ao Espaço",
        "autor_id": "2",
        "ano_publicacao": 2020,
        "gênero": "Ficção Científica",
        "preco": 59.90
    },
    "3": {
        "título": "Histórias Perdidas",
        "autor_id": "3",
        "ano_publicacao": 2015,
        "gênero": "Mistério",
        "preco": 35.50
    }
}

# Dicionário de autores
autores = {
    "1": {
        "nome": "Clara Mendes",
        "nacionalidade": "Brasileira",
        "ano_nascimento": 1980,
        "obras_notáveis": ["O Segredo do Vale", "Noites de Verão"]
    },
    "2": {
        "nome": "Marco Russo",
        "nacionalidade": "Italiano",
        "ano_nascimento": 1975,
        "obras_notáveis": ["Viagem ao Espaço", "O Código das Estrelas"]
    },
    "3": {
        "nome": "Elena Torres",
        "nacionalidade": "Mexicana",
        "ano_nascimento": 1990,
        "obras_notáveis": ["Histórias Perdidas", "O Enigma do Passado"]
    }
}

# Dicionário de clientes
clientes = {
    "1": {
        "nome": "João Silva",
        "email": "joao@email.com",
        "data_cadastro": "2020-05-15",
        "gêneros_favoritos": ["Ficção", "Mistério"],
        "livros_comprados": ["1", "3"]
    },
    "2": {
        "nome": "Ana Souza",
        "email": "ana.s@mail.com",
        "data_cadastro": "2019-08-20",
        "gêneros_favoritos": ["Ficção Científica"],
        "livros_comprados": ["2"]
    },
    "3": {
        "nome": "Carlos Lima",
        "email": "carlos.l@email.com",
        "data_cadastro": "2021-01-10",
        "gêneros_favoritos": ["Aventura", "Mistério"],
        "livros_comprados": ["3"]
    }
}

########################################### METODO GET ############################################################

@app.route("/livro", methods=["get"])
def livro():
    return livros

@app.route("/cliente", methods=["get"])
def cliente():  
    return clientes

@app.route("/autor", methods=["get"])
def autor():
    return autores


########################################### METODO DELETE ############################################################

@app.route("/delete_livro/<string:id>", methods=["delete"])
def delete_livro(id):
    print(f"\n\n--->> {id}\n\n")
    print(livros[id])    
    del livros[id]
    return livros

############################################## METODO POST #########################################################

@app.route("/add_livro", methods=["post"])
def add_livro():
    data = request.get_json()
    livros[f"{len(livros) + 1}"] = data
    return livros

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

############################################## METODO POST #########################################################

