import os
import glob
from pprint import pprint as pp

counntries_to_capitals = { "United Kingdom" : "London",
                            "Egypt" : "Cairo",
                            "Sweden" : "Stockholm",
                            "Brazil" : "Brazilia",
                            "Moroco" : "Rabat"}
capitals_to_countries = { capital : country for country, capital in counntries_to_capitals.items()}
pp(capitals_to_countries)


file_sizes = {os.path.realpath(p) : str(os.stat(p).st_size) + " b" for p in glob.glob("*.py")}
pp(file_sizes)
