from fastapi import FastAPI, Path , HTTPException, Query
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse

app=FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description='ID of the patient')]
    name: Annotated[str,Field(...,description='Name of the patient')]
    city: Annotated[str,Field(...,description='City of the patient')]
    age: Annotated[int,Field(...,gt=0,lt=120,description='Age  of the patient')]
    gender: Annotated[Literal['male','Female','Others'],Field(...,description='Gender of patient')] 
    height: Annotated[float,Field(...,description="Height of the patient in meters")]
    weight: Annotated[float,Field(...,description="Weight of the patient in kg")]   

    @computed_field
    @property
    def bmi(self)->float:
       bmi=round(self.weight/(self.height**2),2)
       return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
       if self.bmi<18.5:
          return 'underweight'
       elif 18.5<self.bmi<25:
          return 'healthy'
       else:
          return "Obese"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

def data_load():
  with open('patients.json','r') as f:
    data=json.load(f)
    return data

def save_data(data):
   with open('patients.json','w') as f:
      json.dump(data,f)


@app.get("/")
def hello():
  return {"message":"Patients management system"}

@app.get("/home")
def home():
  return {"message":"A fully functional API to manage your patient records"}

@app.get("/view")
def view():
  data=data_load()
  return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str= Path(...,examples="P001",description="ID of the Patient", )):
  data=data_load()
  
  if patient_id in data:
    return data[patient_id]
  # return {"error":"Patient does not exist"}
    raise HTTPException(status_code=404,detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by:str=Query(...,description='sort on the basis of height, weight, bmi'),Order:str=Query('asc',description='sort in asc or des order')):

    valid_fields=['height','weight','bmi']

    if sort_by not in valid_fields:
       return HTTPException(status_code=400, detail=f'invalid values selected from {valid_fields}')

    if Order not in ['asc','desc']:
       return HTTPException(status_code=400, detail=f'invalid values selected between asc and desc')

    sort_order= True if Order=="desc" else False

    data=data_load()

    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0), reverse=sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient:Patient):
   #load all data
   data=data_load()
   #check if new patient id exist in DB
   if patient.id  in data:
      raise HTTPException(status_code=400,detail="Patient already exist")
   

   #new patient add to DB
   data[patient.id]=patient.model_dump(exclude=['id'])

  #save data in json file
   save_data(data)

   return JSONResponse(status_code=201,content={"message":"Patient Created successfully"})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data= data_load()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True) #will only fetch updates values

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = data_load()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})