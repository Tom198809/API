from src.model.explorer import Explorer

# fake data, replaced in Chapter 10 by a real database and SQL
_explorers = [
    Explorer(name="Claude Hande",
             country="FR",
             description="Scarce during full moons"),
    Explorer(name="Noah Weiser",
             country="DE",
             description="Myopic machete man"),
    ]

def get_all() -> list[Explorer]:
    """Return all explorers"""
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _explorers list:
def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Partially modify an explorer"""
    return explorer

def replace(name: str, explorer: Explorer) -> Explorer:
    # Здесь можно сделать замену объекта по name или просто вернуть explorer
    return explorer


def delete(name: str) -> bool:
    return any(_explorer.name == name for _explorer in _explorers)