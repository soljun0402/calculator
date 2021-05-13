from django.shortcuts import render

def calculate(request):
  return render(request, "calculate.html")

def result(request):
  number1 = request.GET['number1']
  number2 = request.GET['number2']
  signiture = request.GET['sign']

  for signiture in signiture:
    if signiture == "+":
      result = int(number1) + int(number2)

    elif signiture == "-":
      result = int(number1) - int(number2)

    elif signiture == "*":
      result = int(number1) * int(number2)

    elif signiture == "/":
      if number2 == "0":
        result = "division by zero"
      else:
        result = int(number1) / int(number2)

  return render(request, "result.html", {'result': result})