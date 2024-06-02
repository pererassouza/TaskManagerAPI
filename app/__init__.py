from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskmanager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    taks = db.relationship('Task', backref='user', lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='pendente')
    prioridade = db.Column(db.String(20), default='baixa')
    prazo = db.Column(db.DateTime, nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


with app.app_context():
    db.create_all()


@app.route('/task', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        data = request.json
        prazo_str = data.get('prazo')
        prazo = datetime.fromisoformat(prazo_str) if prazo_str else None
        new_data = Task(
            titulo=data['titulo'],
            descricao=data.get('descricao'),
            status=data.get('status', 'pendente'),
            prioridade=data.get('prioridade', 'baixa'),
            prazo=prazo,
        )
        db.session.add(new_data)
        db.session.commit()
        return jsonify(new_data.id), 201

    tasks = Task.query.all()
    return jsonify([{
        'id': task.id,
        'titulo': task.titulo,
        'descricao': task.descricao,
        'status': task.status,
        'prioridade': task.prioridade,
        'prazo': task.prazo,
        'usuario_id': task.usuario_id
    } for task in tasks])
