from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import Employee
from .serializer import EmployeeSerializer

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer


# serializer = SnippetSerializer()


@csrf_exempt
def employee_list(request):

    if request.method == 'GET':
        emps = Employee.objects.all()
        serializer = EmployeeSerializer(emps, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def employee_detail(request, pk):

    try:
        employee = Employee.objects.get(pk=pk)

    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = EmployeeSerializer(data=data)
    #     # serializer = EmployeeSerializer(
    #     #     data=data, many=False, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)

    #     return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(Employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)
