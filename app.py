# coding: utf-8

import random
from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel


api = FastAPI("github actions demo")


class GreetingStyle(str, Enum):
    Affable = "affable"
    Unpleasant = "unpleasant"
    Aggressive = "aggressive"
    Diffident = "diffident"


_STYLE_NAMES = tuple(entry.value for entry in GreetingStyle)
_GREETING_FOR_STYLE = {
    GreetingStyle.Affable: "Well hey there, {name}!",
    GreetingStyle.Unpleasant: "Oh. It's you again, {name}.",
    GreetingStyle.Diffident: "Oh! Hi, uh... hi {name}...",
    GreetingStyle.Aggressive: "Well? What do you want, {name}?",
}


class GreetingResponseModel(BaseModel):
    greeting: str
    name: str
    style: GreetingStyle


@api.get("/api/v1/greet", response_model=GreetingResponseModel)
def get_greeting(name: str = Query(..., description="Name to greet")):
    """Greet a user by name, with a randomly-chosen greeting style.
    """
    if name.lower() == "joe":
        style = GreetingStyle.Aggressive
    else:
        style = random.choice(list(GreetingStyle))
    return {
        "greeting": _GREETING_FOR_STYLE[style].format(name=name),
        "style": style,
        "name": name,
    }
