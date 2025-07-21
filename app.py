from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuración de MongoDB (usando Mongo Atlas)
app.config["MONGO_URI"] = "mongodb+srv://actividadesitu:marcopolo89@micluster123.mjgzogc.mongodb.net/pruebaMongoDB?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de validación de login
        username = request.form['username']
        password = request.form['password']
        
        # Verificar el usuario en MongoDB
        user = mongo.db.users.find_one({'username': username})
        if user and user['password'] == password:
            return redirect(url_for('dashboard'))
        else:
            return "Usuario o contraseña incorrectos", 401

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Lógica de registro de usuario
        username = request.form['username']
        password = request.form['password']
        
        # Almacenar el usuario en MongoDB
        mongo.db.users.insert_one({'username': username, 'password': password})
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
