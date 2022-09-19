from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from emp.models import Employee
import xlrd
from django.core.files.storage import FileSystemStorage
from .fusioncharts import FusionCharts
import openpyxl
import psycopg2



# # Create your views here.


def home(request):

    return render(request, 'home.html')


def new_employee_details(request):

    print(request.method)
    if request.method == 'GET':
        return render(request, 'new_employee.html')

    elif request.method == 'POST':
        employeecode = request.POST.get("employee_code")
        name = request.POST.get("name")
        emailid = request.POST.get("email_id")
        contactno = request.POST.get("contact_no")
        new = Employee(employee_code=employeecode, name=name,
                       email_id=emailid, contact_no=contactno)
        new.save()
        messages.success(request, 'Profile Saved ')
        return redirect("/newemployee")


def search_employee_details(request):

    if request.method =='GET':
        return render(request, "search_employee.html")
    elif request.method =='POST':
        name_to_search = request.POST.get("name")
        employees = Employee.objects.filter(name__iregex=name_to_search)
    return render(request, "search_employee.html",context={"data":employees})

def show_employee_details(request):

    data = {}
    details = Employee.objects.all()
    for d in details:
        data = {'details': details}
    return render(request, 'show_employee.html', context=data)


def edit_employee_details(request, id):

    if request.method == 'GET':
        employee = Employee.objects.get(id=id)
        show = {
            "employee_code": employee.employee_code,
            "name": employee.name,
            "email_id": employee.email_id,
            "contact_no": employee.contact_no}
        return render(request, 'edit_employee.html', context=show)

    elif request.method == 'POST':
        name  = request.POST.get("name")
        email_id = request.POST.get("email_id")
        contact_no = request.POST.get("contact_no")
        employee = Employee.objects.get(id=id)
        employee.name  = name
        employee.email_id = email_id
        employee.contact_no = contact_no
        employee.save()
        return redirect("/showemployee")

def delete_employee_details(request, id):

    details = Employee.objects.get(id=id)
    details.delete()
    return redirect('/showemployee')

def upload(request):

    if "GET" == request.method:
        return render(request, 'upload_excel_file.html', {})
    else:
        excel_file = request.FILES['excel_file']
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Sheet1"]
        print(worksheet)
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
            detail = Employee(
                employee_code=row_data[0], name=row_data[1], email_id=row_data[2], contact_no=row_data[3])
            detail.save()
        details = Employee.objects.all()

        return render(request, 'show_employee.html', context={'details': details})    

def chart(request):
   chartObj = FusionCharts( 'doughnut3d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Top 5 Years of Revenue",
    "enablesmartlabels": "1",
    "showlabels": "1",
    "numbersuffix": " %",
    "usedataplotcolorforlabels": "1",
    "plottooltext": "$label, <b>$value</b> MMbbl",
    "theme": "fusion"
  },
  "data": [
    {
      "label": "2014",
      "value": "90"
    },
    {
      "label": "2015",
      "value": "60"
    },
    {
      "label": "2016",
      "value": "80"
    },
    {
      "label": "2017",
      "value": "55"
    },
    {
      "label": "2018",
      "value": "85"
    }
  ]
}""")
   return render(request, 'chart.html', {'output': chartObj.render()})

