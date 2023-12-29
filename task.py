import calendar
import statistics


expenses = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": []
        }
    },
    "2023-04": {}
}


def month_first_week(year):
    month_first_week_dict = {}
    for i in range(1, 13):
        first_week_days = calendar.monthcalendar(year, i)[0]
        days_list = [f"{day:02d}" for day in first_week_days if day != 0]
        month_str = f"{year}-{i:02d}" if i >= 10 else f"{year}-0{i}"
        month_first_week_dict[month_str] = days_list
    return month_first_week_dict


def get_median_of_first_week_expenses(expenses, month_first_week_dict):
    expenses_median = []
    for year_month, day_details in expenses.items():
        for day, day_expenses in day_details.items():
            if year_month in month_first_week_dict.keys():
                if day in month_first_week_dict[year_month]:
                    food = day_expenses["food"]
                    fuel = day_expenses["fuel"]
                    if food is not None and food != []:
                        expenses_median.extend(food)
                    if fuel is not None and fuel != []:
                        expenses_median.extend(fuel)
    result = statistics.median(expenses_median)
    return result

print(get_median_of_first_week_expenses(expenses, month_first_week(2023)))



