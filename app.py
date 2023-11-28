from fastapi import FastAPI, Depends, Request, Form, status, File, UploadFile
from typing import List, Dict
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from models import *

# from sqlalchemy.orm import Session
# import models
# from database import SessionLocal, engine

# models.Base.metadata.create_all(bind= engine) 

app = FastAPI()

client=MongoClient("mongodb://localhost:27017")

# def get_db():
#     db= SessionLocal
#     try:
#         yield db
#     finally:
#         db.close()

templates = Jinja2Templates(directory= "templates")

# @app.get("/")
# def home(request: Request, db: Session = Depends(get_db)):
#     details = db.query(models.detail).all()
#     return templates.TemplateResponse("base.html", {"request": request, "detail_list": details})

# @app.get("/form/", response_class=HTMLResponse)
# async def form(request: Request, BU: str, App: str, CPU: int, Memory: int):
#    return templates.TemplateResponse("form.html", {"request": request, "BU": BU, "App": App, "CPU": CPU, "Memory": Memory})


# @app.post("/submit")
# def details(BU: Annotated[str, Form()], App: Annotated[str, Form()], CPU :Annotated[int, Form()], Memory : Annotated[int, Form()]):
#     return {"BU": BU, "App": App, "CPU": CPU, "Memory": Memory}



@app.get("/", response_class=HTMLResponse)
async def write_detail(request: Request):
   return templates.TemplateResponse("form.html", {"request": request})

# @app.post("/submit", status_code=status.HTTP_201_CREATED )
# async def details(BU: str = Form(...), App: str = Form(...), CPU :int = Form(...), Memory : int = Form(...), storage :int = Form(...), environment :str = Form(...), capacity:date = Form(), cycleid :str = Form(...)):
#    return {"BU": BU, "App": App, "CPU": CPU, "Memory": Memory, "storage": storage, "environment": environment, "capacity": capacity, "cycleid": cycleid}

@app.post("/Requirement", status_code=status.HTTP_201_CREATED)

# async def thank(request: Request):
#    return templates.TemplateResponse("thank.html", {"request": request})

async def details(BU: str = Form(...), App: str = Form(...), CPU :int = Form(...), Memory : int = Form(...), storage :int = Form(...), environment :str = Form(...), capacity:date = Form(), cycleid :str = Form(...)):
   return {"BU": BU, "App": App, "CPU": CPU, "Memory": Memory, "storage": storage, "environment": environment, "capacity": capacity, "cycleid": cycleid}
   #print(BU, App, CPU, Memory, storage, environment, capacity, cycleid)

def add_detail(d1: Detail):
   
   """Post a new message to the specified channel."""
   with MongoClient() as client:
      Requirement = client['DB']['DETAILS']
      result = Requirement.distinct(d1.__dict__)
      ack = result.acknowledged
      return {"insertion": ack}
   

# @app.get("/detail", response_model=List[str])
# def get_details():
#    """Get all detail in list form."""
#    with MongoClient() as client:
#       requirement = client[DB][DETAILS]
#       detail_list = requirement.distinct("title")
#       return detail_list