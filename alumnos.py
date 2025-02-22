class alumnos():
    def __init__(self, nombre, paterno, materno,año_nac ):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.año_nac = año_nac
A1 = alumnos('Yuly', 'Guerrero', 'Sandoval', '2004')
A2 = alumnos('Yolanda', 'Gutierrez', 'Saltillo', '2003')
A3 = alumnos('Miranda', 'Torrez', 'Poetillo', '2005')

print("\Hola, soy:", A1.nombre, "mis apellidos son:", A1.paterno, A1.materno)
print("Soy del año: ", str (A1.año_nac))

print("\Hola, soy:", A2.nombre, "mis apellidos son:", A2.paterno, A2.materno)
print("Soy del año: ", str (A2.año_nac))

print("\Hola, soy:", A3.nombre, "mis apellidos son:", A3.paterno, A3.materno)
print("Soy del año: ", str (A3.año_nac))
