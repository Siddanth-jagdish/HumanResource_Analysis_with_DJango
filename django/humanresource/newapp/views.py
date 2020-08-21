from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

import joblib
reloadModel = joblib.load('./models/randomforestmodel.pkl')

from pymongo import MongoClient

client = MongoClient('localhost',27017)

print(client.database_names())

db = client['employee']

collectionD = db['employeereview']
# Create your views here.

def index(request):
    temp={}
    temp['Age']=32
    temp['Gender']=0
    temp['EducationBackground']=5
    temp['MaritalStatus']=1
    temp['EmpDepartment']=5
    temp['EmpJobRole']=8
    temp['BusinessTravelFrequency']=2
    temp['DistanceFromHome']=2
    temp['EmpEducationLevel']=3
    temp['EmpEnvironmentSatisfaction']=4
    temp['EmpHourlyRate']=55
    temp['EmpJobInvolvement']=3
    temp['EmpJobLevel']=2
    temp['EmpJobSatisfaction']=4
    temp['NumCompaniesWorked']=1
    temp['OverTime']=0
    temp['EmpLastSalaryHikePercent']=12
    temp['EmpRelationshipSatisfaction']=4
    temp['TotalWorkExperienceInYears']=10
    temp['TrainingTimesLastYear']=2
    temp['EmpWorkLifeBalance']=2
    temp['ExperienceYearsAtThisCompany']=10
    temp['ExperienceYearsInCurrentRole']=7
    temp['YearsSinceLastPromotion']=0
    temp['YearsWithCurrManager']=8
    temp['Attrition']=0
    context={'temp':temp}
    return render(request,'index.html',context)



def predictemp(request):
    print(request)
    if request.method == 'POST':

        temp={}
        temp['Age']=request.POST.get('ageval')
        temp['Gender']=request.POST.get('gndrval')
        temp['EducationBackground']=request.POST.get('educbkgval')
        temp['MaritalStatus']=request.POST.get('mrtstsval')
        temp['EmpDepartment']=request.POST.get('empdptval')
        temp['EmpJobRole']=request.POST.get('empjbval')
        temp['BusinessTravelFrequency']=request.POST.get('bsnstrvlfrqval')
        temp['DistanceFromHome']=request.POST.get('disthomeval')
        temp['EmpEducationLevel']=request.POST.get('educlvlval')
        temp['EmpEnvironmentSatisfaction']=request.POST.get('empenvsatval')
        temp['EmpHourlyRate']=request.POST.get('emphrval')
        temp['EmpJobInvolvement']=request.POST.get('empjobinval')
        temp['EmpJobLevel']=request.POST.get('empjbval')
        temp['EmpJobSatisfaction']=request.POST.get('empjbsatval')
        temp['NumCompaniesWorked']=request.POST.get('cmpworkdval')
        temp['OverTime']=request.POST.get('ovrtimval')
        temp['EmpLastSalaryHikePercent']=request.POST.get('hikeprcntval')
        temp['EmpRelationshipSatisfaction']=request.POST.get('emprelatsatval')
        temp['TotalWorkExperienceInYears']=request.POST.get('workexpval')
        temp['TrainingTimesLastYear']=request.POST.get('traintimlstyrval')
        temp['EmpWorkLifeBalance']=request.POST.get('wrklifbalval')
        temp['ExperienceYearsAtThisCompany']=request.POST.get('expyrsatcmpval')
        temp['ExperienceYearsInCurrentRole']=request.POST.get('expyrscurrolval')
        temp['YearsSinceLastPromotion']=request.POST.get('yrssinlastprval')
        temp['YearsWithCurrManager']=request.POST.get('yrscurmngval')
        temp['Attrition']=request.POST.get('attrval')

    for _key in temp:
        try:
            temp[_key] = [float(temp[_key])]
        except ValueError:
            pass

    testtdata = pd.DataFrame.from_dict(temp)
    print(testtdata)
    scoreval = reloadModel.predict(testtdata)[0]
    context = {'scoreval': scoreval, 'temp': temp}
    return render(request,'index.html',context)

def viewDataBase(request):
    countofrow = collectionD.find().count()
    context = {'countofrow':countofrow}
    return render(request,'viewDB.html',context)

def updateDataBase(request):
    temp={}
    temp['Age']=request.POST.get('ageval')
    temp['Gender']=request.POST.get('gndrval')
    temp['EducationBackground']=request.POST.get('educbkgval')
    temp['MaritalStatus']=request.POST.get('mrtstsval')
    temp['EmpDepartment']=request.POST.get('empdptval')
    temp['EmpJobRole']=request.POST.get('empjbval')
    temp['BusinessTravelFrequency']=request.POST.get('bsnstrvlfrqval')
    temp['DistanceFromHome']=request.POST.get('disthomeval')
    temp['EmpEducationLevel']=request.POST.get('educlvlval')
    temp['EmpEnvironmentSatisfaction']=request.POST.get('empenvsatval')
    temp['EmpHourlyRate']=request.POST.get('emphrval')
    temp['EmpJobInvolvement']=request.POST.get('empjobinval')
    temp['EmpJobLevel']=request.POST.get('empjbval')
    temp['EmpJobSatisfaction']=request.POST.get('empjbsatval')
    temp['NumCompaniesWorked']=request.POST.get('cmpworkdval')
    temp['OverTime']=request.POST.get('ovrtimval')
    temp['EmpLastSalaryHikePercent']=request.POST.get('hikeprcntval')
    temp['EmpRelationshipSatisfaction']=request.POST.get('emprelatsatval')
    temp['TotalWorkExperienceInYears']=request.POST.get('workexpval')
    temp['TrainingTimesLastYear']=request.POST.get('traintimlstyrval')
    temp['EmpWorkLifeBalance']=request.POST.get('wrklifbalval')
    temp['ExperienceYearsAtThisCompany']=request.POST.get('expyrsatcmpval')
    temp['ExperienceYearsInCurrentRole']=request.POST.get('expyrscurrolval')
    temp['YearsSinceLastPromotion']=request.POST.get('yrssinlastprval')
    temp['YearsWithCurrManager']=request.POST.get('yrscurmngval')
    temp['Attrition']=request.POST.get('attrval')
    temp['emp']=request.POST.get('empval')
    collectionD.insert_one(temp)
    countofrow=collectionD.find().count()


    context={'countofrow':countofrow}
    return render(request,'viewDB.html',context)
