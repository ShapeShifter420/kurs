from typing import List

from pydantic import BaseModel


class Image(BaseModel):
    path: str


class ColorSpaces(BaseModel):
    image: str
    color_spaces: List[str]


class RectanglesCords(BaseModel):
    image: str
    color_range: str


class FrequencyFiltering(BaseModel):
    image: str
    filtration_purity: int


class Images(BaseModel):
    images: List[str]
