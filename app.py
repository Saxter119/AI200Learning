
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from html import escape

app = FastAPI()

pixels = """
..........KKKKKK..........
.........KSSSSSSK.........
........KSSKKKSKKK........
........KSSSSSSSSSK.......
.......KSSS...S.SSK.......
.......KSS..KKSK.SK.......
.......KSS..KKSK.SK.......
........KSS...S.SSK.......
......KKKSSSSSSSSSKK.KKKK.
.....KK.KKSSKKKKSKKKKRRRRK
....KK..KYKSSSSSKK.KRRRRRK
....KYYYYYYKKKKKKYYRRRKRRK
...KRRRYKYYYYGYYYYYKKKKKK.
...KRRKKKYYYYGYYKKKK......
...KRRRKKYYYYYYYK..K......
...KRRRKKYYYYYYYK..K......
....KKK.KKKKGKKKK..K......
.....K.KYYYYYYYYK..K......
.....KKYYYYYYYYYYKKK......
.....KKRYYYYKYYYRRKK......
...KKRRRRRYK.KYRRRRRKK....
..KRRRRRRRK...KRRRRRRRK...
..KKKKKKKKK...KKKKKKKKK...
.....K.............K......
.....KKKKKKKKKKKKKKK......
""".strip().splitlines()

colors = {
    ".": "⬜",  # Fondo, capa y ojos
    "K": "⬛",  # Contornos
    "S": "🟧",  # Piel
    "Y": "🟨",  # Traje
    "R": "🟥",  # Guantes y botas
    "G": "🟫",  # Cremallera y hebilla
}

# Conservamos la impresión original de Saitama en los logs de Azure.
for row in pixels:
    print("".join(colors[pixel] for pixel in row))

print("\nHello, World! 👊")

# Y también lo mostramos en el navegador mediante FastAPI.
@app.get("/", response_class=HTMLResponse)
def inicio():
    dibujo = "\n".join(
        "".join(colors[pixel] for pixel in row)
        for row in pixels
    )

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saitama — Hello, World!</title>
    <style>
        body {{
            margin: 0;
            min-height: 100vh;
            background: #111827;
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
        }}
        pre {{
            font-size: 16px;
            line-height: 1.1;
            overflow-x: auto;
            max-width: 95vw;
        }}
        h1 {{ margin-top: 20px; }}
    </style>
</head>
<body>
    <pre>{escape(dibujo)}</pre>
    <h1>Hello, World! 👊</h1>
</body>
</html>"""
