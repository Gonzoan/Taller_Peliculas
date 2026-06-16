import pandas as pd

#leo los datos
df = pd.read_csv('input/peliculas.csv')
#hago una copia por las dudas
tabla_cambios = df[["titulo","genero","calificacion","anio"]].copy()

#creo la columna de clasica
tabla_cambios["clasica"] = tabla_cambios["anio"] < 1995;
#quito la columna de años
tabla_cambios = tabla_cambios.drop(columns=["anio"])

#definimos las resenas
nota = [0.0,3.0,5.0,7.0,8.5,10.0]
resena = ["Pesima","Mala", "Regular", "Buena", "Excelente"]
#creamos la columna
tabla_cambios["apreciacion"] = pd.cut(
    tabla_cambios["calificacion"],
    bins=nota,
    labels=resena,
    right=True,
    include_lowest=True
)
#pasar la tabla a .csv
tabla_cambios.to_csv("output/TablaActualizada.csv", index=False)
print(tabla_cambios)

#calcular el promedio y cantidad por genero
Tabla_Promedio = (
    df.groupby("genero")
    .agg(
        Promedio = ("calificacion","mean"),
        Cantidad = ("titulo", "count")
    )
    .reset_index()
)

Tabla_Promedio["Promedio"] = Tabla_Promedio["Promedio"].round(2)
print(Tabla_Promedio)

#Pasar la tabla a exel .xlsx
Tabla_Promedio.to_excel("output/AnalisisDatos.xlsx", index=False)