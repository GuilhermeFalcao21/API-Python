from flask import Flask, jsonify

app = Flask(__name__)

# Dicionário de usuários
usuarios = {
    1: {
        'nome': 'Guilherme',
        'idade': 22,
        'profissao': 'Programador'
    },
    2: {
        'nome': 'Kelvin',
        'idade': 30,
        'profissao': 'Advogado'
    },
    3: {
        'nome': 'Pedro',
        'idade': 28,
        'profissao': 'Professor'
    }
}

# para buscar usuários por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = usuarios.get(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'erro': 'Usuário não encontrado.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
