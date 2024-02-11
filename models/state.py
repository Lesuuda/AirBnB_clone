#!/usr/bin/python3
"""
class that defines the state
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    Public class attributes:
        name: string - empty string
    """
    state_id = ""
    name = ""