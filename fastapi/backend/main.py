from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    loanamount: float
    creditscore: int

app = FastAPI()

@app.post("/riskrating/")
async def get_risk_rating(item: Item):
    if item.loanamount > 1000 and item.creditscore < 300:
        return {"risk":"high"}
    elif item.creditscore > 600:
        return  {"risk":"low"}
    else:
        return {"risk":"medium"}
    
