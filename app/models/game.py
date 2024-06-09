import pathlib
from pydantic import BaseModel


class GameInfo(BaseModel):
    html_path:  pathlib.Path | None = None
    name: str
    description: str
    image_file: pathlib.Path | None = None
