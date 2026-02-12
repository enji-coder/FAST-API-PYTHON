from pydantic import BaseModel

class Product(BaseModel):
    id : int 
    name : str 
    description : str 
    price : int 
    qty : int 
    
    # def __init__(self,id:int,name:str,description:str,price:int,qty:int):
    #     self.id = id
    #     self.name = name
    #     self.description =description
    #     self.price = price
    #     self.qty = qty