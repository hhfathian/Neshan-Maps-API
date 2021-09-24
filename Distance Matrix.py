import pandas as pd
import numpy as np
import requests

origin_lat=36.3177579
origin_lon=59.5323219

desnination_lat=36.35067
destination_lon=59.5451965

requests.get("https://api.neshan.org/v1/distance-matrix?origins="+str(origin_lat)+','+str(origin_lon)+'&destinations='+str(desnination_lat)+','+str(destination_lon),
                                           headers={"Api-Key": "please inter your API key here"}).json()['rows'][0]['elements'][0]['duration']['text']