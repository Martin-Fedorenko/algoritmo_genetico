# algoritmo_genetico


##Instalación de bibliotecas:

```
pip install deap numpy pandas openpyxl matplotlib
```

##Generación de ejecutable en la carpeta "dist"

```
cd algoritmo_genetico
```

```
pyinstaller --onefile --icon=icono.png --add-data="datos_originales.xlsx;." algoritmo.py
```