from typing import Union

def analiza_wzorca(data: Union[list,tuple]):
    match data:
        case []:
            print("Pusta lista")
        case (a,b) if isinstance(data, tuple):
            print("Jest to krotka z dwoma elementami")


analiza_wzorca((10,20))
analiza_wzorca([])