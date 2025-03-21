import uvicorn
from argparse import ArgumentParser

parser = ArgumentParser("Crud API", description="Crud API")
parser.add_argument("--host", default="0.0.0.0")  # Definir host
parser.add_argument("-p", "--port", type=int, default=8080)  # Especificar tipo int para el puerto

args = parser.parse_args()
uvicorn.run("crud_api_fast:app", host=args.host, port=args.port, reload=True)
