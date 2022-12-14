
# CREAR ENTORNO VIRTUAL >>      virtualenv env (Posicionado en la carpeta que quiero crearlo)
# ACTIVAR ENTORNO VIRTUAL >>    env\Scripts\activate.bat
# DESACTIVAR ENTORNO VIRTUAL >>  deactivate
# --------------------------------------------------------------------------------------------- 

from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)