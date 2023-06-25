import pandas as pd

#getting the liks from the file with the links
class Importer():
    def __init__(self,filename):
        with open (filename, "r") as file:
            df = pd.read_csv(file)
            self.list_of_inputted_links = list(df.Profile_link)
    


