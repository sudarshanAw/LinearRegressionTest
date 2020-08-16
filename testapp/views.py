from django.shortcuts import render
import joblib
from testapp.form import Customer_Form
from django.contrib import messages

# Create your views here.

def predict_salary(experience):
    predictor = joblib.load('linear_model.pkl')
    results = predictor.predict([[experience]])
    return results

def salary_view(request):
    if request.method == 'POST':
        form = Customer_Form(request.POST)
        if form.is_valid():
            exp = form.cleaned_data['experience']
            print(exp)
            salary = predict_salary(exp)
            messages.success(request,"your salary is : {}".format(salary))

    else:
        form = Customer_Form();
    return render(request,'testapp/employee_form.html', {'form': form})



