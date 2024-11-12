from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from USED_CAR_PRICES_PREDICTION import settings
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
def homepage(request):
    return render(request,"index.html")



def indexfn(list,data):
    for i in range(len(list)):
        if list[i]== data:
            return i
         
b=  ['Diesel', 'Petrol', 'LPG', 'CNG']
c = ['Individual', 'Dealer', 'Trustmark Dealer']
d = ['Manual', 'Automatic']
e=['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car']
model = RandomForestRegressor()
x_train = pd.read_csv(settings.DATASET_PATH1)
y_train = pd.read_csv(settings.DATASET_PATH2)
y_train = y_train.to_numpy()
y_train = y_train.flatten()
model.fit(x_train,y_train)

def pred(request):
    result =["Model error"]
    if request.method == "POST":
        try:
            list=[]
            list.append(request.POST["a2"])
            list.append(request.POST["a3"])
            list.append(request.POST["a4"])
            list.append(request.POST["a5"])
            list.append(request.POST["a6"])
            list.append(request.POST["a7"])
            list.append(request.POST["a8"])
            list.append(request.POST["a9"])
            list.append(request.POST["a10"])
            list.append(request.POST["a11"])
            inputdata = pd.DataFrame([list],columns=['year', 'km_driven', 'fuel', 'seller_type','transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])
            inputdata.loc[0, "fuel"] = indexfn(b, inputdata.loc[0, "fuel"])
            inputdata.loc[0, "seller_type"] = indexfn(c, inputdata.loc[0, "seller_type"])
            inputdata.loc[0, "transmission"] = indexfn(d, inputdata.loc[0, "transmission"])
            inputdata.loc[0, "owner"] = indexfn(e, inputdata.loc[0, "owner"])
            result=model.predict(inputdata)
            result=[round(result[0],2)]
        except:
            pass
        return JsonResponse({"result":result[0]})
