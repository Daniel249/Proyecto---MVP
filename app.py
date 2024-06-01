from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Procesar el formulario de registro
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Aquí puedes guardar los datos en la base de datos o hacer cualquier otro procesamiento necesario

        return f"Usuario creado: {username}, Email: {email}, Password: {password}"
    else:
        # Renderizar el formulario de registro
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
