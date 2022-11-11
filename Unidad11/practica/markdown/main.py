# importacion
import markdown as mk

# texto a convertir
string = """# Titulo
## Subtitulo

* Una viñeta

* Otra viñeta

*letra en cursiva*

1. item de una lista
2. item de una lista
"""

# conversion a HTML
html = mk.markdown(string)
html

# ahora guardamos el contenido de la variable a un archivo .HTML
with open("test_markdown.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(html)