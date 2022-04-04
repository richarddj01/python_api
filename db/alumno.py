class Alumno:
  cuenta = ""
  nombre = ""
  genero = ""
  correo = ""
  telefono = ""

  def getDict(self):
    return {
      'cuenta' : self.cuenta,
      'nombre' : self.nombre,
      'genero' : self.genero,
      'correo' : self.correo,
      'telefono' : self.telefono
    }
