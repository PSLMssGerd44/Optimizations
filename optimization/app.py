from fastapi import FastAPI

from model import create_solve_model
from schemas import FoodRequirements


app = FastAPI(
    title="my-first-fastapi-app",
    decription="my-description",
    version="0.0.01a",
)

@app.post("/solve-model")
def solve_model(food_requirements:FoodRequirements) -> dict[str,str]:
   data = dict(
    )
   
   data["FOODS"]= food_requirements.foods
   data["NUTRIENTS"]= food_requirements.nutrients
   data["cf"]= food_requirements.cf
   data["afn"]= food_requirements.afn
   data["Nminn"]= food_requirements.Nminn
   data["Nmaxn"]= food_requirements.Nmaxn
   data["Vmax"]= food_requirements.Vmax
   data["Vf"]= food_requirements.Vf



   return create_solve_model(data=data)
