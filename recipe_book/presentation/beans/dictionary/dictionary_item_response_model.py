from dataclasses import dataclass

from ...interfaces.dictionary.dictionary_item_response_model import IDictionaryItemResponseModel


@dataclass
class DictionaryItemResponseModel(IDictionaryItemResponseModel):
    code: str
    title: str
