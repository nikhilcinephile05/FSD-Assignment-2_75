from django.shortcuts import render
from django.http import HttpResponse
from .logic import BMR, TEF, Exercise_Energy_Expenditure, Non_Exercise_Activity_Thermogenesis, Total_Daily_Energy_Expenditure, recommended_calories


def index(request):
    if request.method == "POST":
        weight = int(request.POST['weight'])
        goal = int(request.POST['goal'])
        workout = request.POST['workout']
        activity_level = request.POST['activity_level']
        bmr = BMR(weight)
        tef = TEF(bmr)
        EEE = Exercise_Energy_Expenditure(workout)
        NEAT = Non_Exercise_Activity_Thermogenesis(activity_level)
        TDEE = Total_Daily_Energy_Expenditure(bmr, tef, EEE, NEAT)
        rc = recommended_calories(TDEE, goal, weight)
        lose_half = rc[0]
        lose_one = rc[1]
        time_to_lose_half = rc[2]
        time_to_lose_one = rc[3]
        return render(request, "calorie_counter/index.html", {
            "bmr": bmr,
            "Total_Daily_Energy_Expenditure": TDEE,
            # "rate": rate,
            "lose_half": lose_half,
            "lose_one": lose_one,
            # "lose_one_half": lose_one_half,
            # "lose_two": lose_two,
            "goal": goal,
            "time_to_lose_half": time_to_lose_half,
            "time_to_lose_one": time_to_lose_one,
            # "time_to_lose_one_half": time_to_lose_one_half,
            # "time_to_lose_two": time_to_lose_two,
        })
    else:
        return render(request, "calorie_counter/index.html")


def register(request):
    return HttpResponse("HOLAAAA")
