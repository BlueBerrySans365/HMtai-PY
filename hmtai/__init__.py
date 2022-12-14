"""
HMTAI PORT REWRITE - by @NMWIN_D (twitter) & NickSaltFoxu ( comeback, guys )
Used original port made by NickSaltFoxu
HMTAI is an Anime / Hentai (NSFW) Image API which simplifies how you fetch random images from the official REST API!\n
"""
from hmtai.hmfull import hmfull

class CategoryNotFound(Exception):
    def __init__(self, categoryn):
        self.categoryn = categoryn
        self.message = f"I don't found '{categoryn}' in list of categories. Please, check docs for right names."
        super().__init__(self.message)

class SourceNotFound(Exception):
    def __init__(self, source):
        self.source = source
        self.message = f"I don't found {source} in list of categories. Please, check docs for right names."
        super().__init__(self.message)

class NoSourceEntered(Exception):
    def __init__(self):
        self.message = f"Source name is empty."
        super().__init__(self.message)

class NoCategoryEntered(Exception):
    def __init__(self):
        self.message = f"Category name is empty."
        super().__init__(self.message)

def get(source = None, category = None):
    if source == None:
        raise NoSourceEntered
    if category == None:
        raise NoCategoryEntered
    if source == "hmtai":
        try:
            res = hmfull.hmtai(category)
            if res == 0:
                raise CategoryNotFound(category)
            else:
                return res
        except Exception as e:
            print(f"ERROR! Contact NickSaltFox#7273 (in discord) with this information!\nDetails: \n  Source: {source}\n Exception: {e}")
    elif source == "nekobot":
        try:
            res = hmfull.nekobot(category)
            if res == 0:
                raise CategoryNotFound(category)
            else:
                return res
        except Exception as e:
            print(f"ERROR! Contact NickSaltFox#7273 (in discord) with this information!\nDetails: \n  Source: {source}\n Exception: {e}")
    elif source == "nekos":
        try:
            res = hmfull.nekos(category)
            if res == 0:
                raise CategoryNotFound(category)
            else:
                return res
        except Exception as e:
            print(f"ERROR! Contact NickSaltFox#7273 (in discord) with this information!\nDetails: \n  Source: {source}\n Exception: {e}")
    elif source == "freaker":
        try:
            res = hmfull.freaker(category)
            if res == 0:
                raise CategoryNotFound(category)
            else:
                return res
        except Exception as e:
            print(f"ERROR! Contact NickSaltFox#7273 (in discord) with this information!\nDetails: \n  Source: {source}\n Exception: {e}")
    elif source == "nekolove":
        try:
            res = hmfull.nekolove(category)
            if res == 0:
                raise CategoryNotFound(category)
            else:
                return res
        except Exception as e:
            print(f"ERROR! Contact NickSaltFox#7273 (in discord) with this information!\nDetails: \n  Source: {source}\n Exception: {e}")

def useHM(version = None, category = None):
    return get("hmtai",f"{category}")
