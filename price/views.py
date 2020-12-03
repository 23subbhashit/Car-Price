from django.shortcuts import render
import pickle

def index(request):
    return render(request,'price/index.html')
def result(request):
    pkl_path = "Car.pkl"
    with open(pkl_path, 'rb') as f:
        model = pickle.load(f)
    l=[]
    l.append(request.GET['1'])
    l.append(request.GET['2'])
    l.append(request.GET['3'])
    l.append(request.GET['4'])
    l.append(request.GET['5'])
    l.append(request.GET['6'])
    l.append(request.GET['7'])
    l.append(request.GET['8'])
    l.append(request.GET['9'])
    l.append(request.GET['10'])
    l.append(request.GET['11'])
    l.append(request.GET['12'])
    l.append(request.GET['13'])
    l.append(request.GET['14'])
    l.append(request.GET['15'])
    l.append(request.GET['16'])
    l.append(request.GET['17'])
    l.append(request.GET['18'])
    l.append(request.GET['19'])
    l.append(request.GET['20'])
    l.append(request.GET['21'])
    l.append(request.GET['21'])
    l.append(request.GET['22'])
    l.append(request.GET['23'])
    res=model.predict([l])
    

    return render(request,'price/result.html',{'res':res})