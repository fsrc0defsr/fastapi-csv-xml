from fastapi import FastAPI, HTTPException, Response
from database import OracleDB
from xml_generator import generate_xml
import os


app = FastAPI()
db = OracleDB()
api_key = os.getenv("API_KEY")
view_name = os.getenv("VIEW_NAME")
xml_file = "data.xml"

def check_token(token: str = None):
    if token != api_key:
        raise HTTPException(status_code=401, detail="Access denied!")

def update_xml_file():
    data = db.read_data_from_view(view_name)
    generate_xml(data, xml_file)


@app.get("/data_xml")
def update_data_and_generate_xml(token: str):
    check_token(token)
    update_xml_file()
    response = Response(content=open(xml_file, "rb").read())
    response.headers["Content-Disposition"] = "attachment; filename=data.xml"
    return response

if __name__ == "__main__":
    # Запуск FastAPI
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
