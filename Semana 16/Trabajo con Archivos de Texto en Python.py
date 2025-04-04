# Escritura en el archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("1. Aprender Python mejora mis habilidades de programación.\n")
    file.write("2. La manipulación de archivos es esencial en muchos proyectos.\n")
    file.write("3. Practicar con GitHub me ayuda a gestionar mejor mis proyectos.\n")

# Lectura del archivo de texto línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # Se usa strip() para eliminar espacios o saltos de línea adicionales

# Nota: No es necesario cerrar el archivo manualmente cuando se usa "with open()",
# ya que Python se encarga de hacerlo automáticamente.
