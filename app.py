from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Tu interfaz HTML Dinámica en Modo Oscuro integrada directamente
    html_dinamico = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Bitácora en la Nube</title>
        <style>
            body { 
                background-color: #1e1e2e; 
                color: #cdd6f4; 
                font-family: sans-serif; 
                text-align: center; 
                padding: 50px; 
            }
            .tarjeta {
                background: #252538;
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
                box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            }
            h1 { color: #89b4fa; }
            span { color: #a6e3a1; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="tarjeta">
            <h1>⚔️ Bitácora de Rey ⚔️</h1>
            <p>Estado del Servidor: <span>¡EN LÍNEA DESDE PYTHON Y RENDER!</span></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_dinamico)

if __name__ == '__main__':
    # Captura el puerto que Render le asigne automáticamente
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto)