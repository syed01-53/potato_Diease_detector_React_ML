from typing import Annotated
import numpy as np
from fastapi import FastAPI, File, UploadFile
import uvicorn 

from io import BytesIO
#  pil is a module that are read file in python 
from PIL import Image

app = FastAPI()

@app.get('/')
async def hello():
    return {"message": "Welcome After"}
# reading file in bytes 
def read_file_as_img(data)-> np.ndarray:
    image=np.array(Image.open(BytesIO(data)))
    return image
@app.post("/predict")
async def predict(file: UploadFile=File(...)):
    img=read_file_as_img(await file.read())
    print(img)
    return img 


    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=8000)