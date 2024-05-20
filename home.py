from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        totalsin = cantidad * 9000
        if edad >= 18 and edad <= 30:
            peso="$"
            descuento = totalsin * 0.15
            totalcon = totalsin - descuento
        elif edad > 30:
            peso = "$"
            descuento = totalsin * 0.25
            totalcon = totalsin - descuento
        else:
            peso= ""
            descuento = "No aplica descuento"
            totalcon = totalsin
        return render_template('ejercicio1.html', nombre=nombre, totalsin=totalsin, descuento=descuento, totalcon=totalcon, peso=peso)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        clave = request.form['clave']
        if nombre == "juan" and clave == "admin" :
            mensaje = "Bienvenido Administrador Juan"
            return render_template('bienvenido.html', nombre=nombre, clave=clave, mensaje=mensaje)
        elif nombre == "pepe" and clave == "user" :
            mensaje = "Bienvenido Usuario Pepe"
            return render_template('bienvenido.html', nombre=nombre, clave=clave, mensaje=mensaje)
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', nombre=nombre, clave = clave, mensaje=mensaje)
    return render_template('ejercicio2.html')

@app.route('/bienvenido')
def bienvenido():
    return render_template('bienvenido.html')

if __name__ == '__main__':
    app.run(debug=True)
