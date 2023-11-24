from typing import Literal

IKilogramUnit = Literal["kg"]
IGramUnit = Literal["gr"]
IPieceUnit = Literal["piece"]
IIngredientUnit = Literal[IGramUnit, IKilogramUnit, IPieceUnit]
