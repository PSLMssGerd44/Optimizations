

data = dict(
        FOODS = {"Cheeseburger", "Fries", "Coke"},
        NUTRIENTS = {"Calories", "Carbs", "Proteins", "Sugars"},
        cf = {
            "Cheeseburger": 1.84,
            "Fries":0.67,
            "Coke":1,
        },

       afn = {
            ("Cheeseburger", "Calories"): 510,
            ("Cheeseburger", "Carbs"): 34,
            ("Cheeseburger", "Proteins"): 28,
            ("Cheeseburger", "Sugars"): 5,
            ("Fries", "Calories"): 220,
            ("Fries", "Carbs"): 26,
            ("Fries", "Proteins"): 3,
            ("Fries", "Sugars"): 2,
            ("Coke", "Calories"): 120,
            ("Coke", "Carbs"): 10,
            ("Coke", "Proteins"): 1,
            ("Coke", "Sugars"): 15,
        },

        Nminn = {
            "Calories":2000,
            "Carbs":120,
            "Proteins":50,
            "Sugars":44,
        },

        Nmaxn = {
            "Calories":200000,
            "Carbs":2000000,
            "Proteins":20000000,
            "Sugars":2000000,
        },

        Vmax = 70,


        Vf = {
            "Cheeseburger":5, 
            "Fries":5, 
            "Coke":5,
        },
    )

afn: dict[tuple[str, str], float]

