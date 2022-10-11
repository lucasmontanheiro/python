# Dataclasses are useful to expand objects in classes
# So instead of adding the objects to every single function, it construct below the class

import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
  return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass
class Person:
  name: str
  address: str
  active: bool = True  # default = True
  email_addresses: list[str] = field(default_factory=list)
  id: str = field(init=False, default_factory=generate_id) #init=False makes it not initiated


  # __init__, __repr__ is automatically generated
  
  def main() -> None:
    person = Person(name="Lucas", address="1500 Noe St")
    print(person)

Person.main()