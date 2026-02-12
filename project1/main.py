from fastapi import FastAPI
from models import * 
app = FastAPI() 

products = [
    Product(id=1, name="Mobile", description="Iphone 16", price=68000, qty=20),
    Product(id=2, name="Laptop", description="Dell", price=57000, qty=40),
    Product(id=3, name="AC", description="Iphone 18", price=68000, qty=30)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{id}")
def get_specific_product(id : int):
    for product in products:
        if product.id == id:
            return product
    
    return "no records found !"


@app.post("/products")
def add_product(product:Product):
    products.append(product)
    return product


@app.put("/products")
def update_product(id : int,product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "detailed updated !!"
    return "no records found !"


@app.delete("/products")
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted !!!"
    return "no product found !!"