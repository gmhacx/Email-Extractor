import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from Get_Email import Get_Email


class Core(object):
    # Constructor
    def __init__(self, _All_Links):
        # All Links [Private]
        self.__All_Links = _All_Links

        # Get_Email Class Instance [Private]
        self.__Email = Get_Email()

    # Links
    def Links(self):
        try:
            # Iterating over references in a loop
            for _Link in tqdm(self.__All_Links, desc="Progress"):
                # True if the link starts with HTTP or WWW
                if _Link.startswith(("http", "www")):
                    # Get HTML
                    _HTML = BeautifulSoup(requests.get(_Link).text, "html.parser")

                    # Search Email
                    self.__Email.Search_Email(_HTML)

            print("\nResult:")
            for _Email in set(self.__Email._Get_Email__Emails):
                print(_Email)
        except Exception:
            pass