from pydantic import BaseModel, validator

class FoodRequirements(BaseModel):
    foods: list[str]
    cf: dict[str, float]
    nutrients: list[str]
    Nminn: dict[str,int]
    Nmaxn: dict[str,float]
    Vmax: int
    Vf: dict[str, int]
    afn: dict[str, float]

    @validator("cf")
    def validate_foods(cls, cf, values):
        for k in cf.keys():
          if not all([k in values["foods"]]):
                raise ValueError(f"Food {k} in cf is not valid")
          return cf
        
    @validator("Nminn")
    def validate_nutrients_min(cls, Nmin, values):
         for k in Nmin.keys():
            if not all([k in values["nutrients"]]):
                    raise ValueError(f"Nutrient {k} in Nmin is not valid")
            return Nmin 
         
    @validator("Nmaxn")
    def validate_nutrients_max(cls, Nmax, values):
         for k in Nmax.keys():
            if not all([k in values["nutrients"]]):
                    raise ValueError(f"Nutrient {k} in Nmin is not valid")
            return Nmax 
         
         
    @validator("Vf")
    def validate_volume_total(cls, Vf, values):
         for k in Vf.keys():
          if not all([k in values["foods"]]):
                raise ValueError(f"Food {k} in cf is not valid")
          return Vf
    
    @validator("afn")
    def validate_afn(cls, afn, values):
        for k in afn.keys():
            if not "," in k:
                raise ValueError("afn is not valid")
            return afn
    
        
    @validator("afn")
    def validate_afn_convert(cls, afn, values):
        afnn = {
            tuple([text.strip() for text in k.split(",")]):v for k,v in afn.items()
        }
        return afnn