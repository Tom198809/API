from fastapi import APIRouter
from src.model.explorer import Explorer
import src.fake.explorer as service

router = APIRouter(prefix = "/explorer")

@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    return service.get_one(name)

# all the remaining endpoints do nothing yet:
@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)

@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    return service.modify(explorer)


@router.put("/{name}")
def replace(name: str, explorer: Explorer) -> Explorer:
    return service.replace(name, explorer)


@router.delete("/{name}", response_model=bool)
def delete(name: str):
    return service.delete(name)