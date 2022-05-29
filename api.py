from typing import Optional
from fastapi import FastAPI, Path

from fakeData import menu

app = FastAPI()

@app.get('/')
async def main():
  return {
    'message': 'Hello World'
  }
  

@app.get('/get-item/{item_id}')
async def get_item(
  item_id: int = Path(
    None,
    description = 'Fill with id of item')):
  
  search = list(filter(lambda x: x['id'] == item_id, menu))
  
  if search == []:
    return {'error': 'Item does not exists'}
  
  return {'item': search[0]}


@app.get('/get-by-name')
async def get_item_by_name(name: Optional[str] = None):
  
  search = list(filter(lambda x: x['name'] == name, menu))
  
  if search == []:
    return {'error': 'Item does not exists'}
  
  return search[0]


@app.get('/list-menu')
async def list_menu():
  return menu