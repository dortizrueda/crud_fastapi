import uvicorn
from argparse import ArgumentParser

parser = ArgumentParser("Crud API",description="Crud API")
parser.add_argument("-h","--host",default="127.0.0.1")
parser.add_argument("-p","--port",default=8080)

args=parser.parse_args()
uvicorn.run("crud_api_fast:app",host=args.host,port=args.port,reload=True)