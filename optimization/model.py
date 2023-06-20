import pyomo.environ as pyo


def create_solve_model(data:dict) -> dict:

    model = pyo.ConcreteModel(name="Diet problem", doc="Diet problem")

    model.F = pyo.Set(initialize=data["FOODS"], doc = "Food set")
    model.N = pyo.Set(initialize=data["NUTRIENTS"], doc = "Nutrients set")

    model.cf= pyo.Param(model.F, within=pyo.NonNegativeReals, initialize=data["cf"], doc="cost per serving")
    model.afn = pyo.Param(model.F, model.N, initialize=data["afn"])
    model.Nminn = pyo.Param(model.N, initialize=data["Nminn"], doc="Minimum nutrients per serving")
    model.Nmaxn = pyo.Param(model.N, initialize=data["Nmaxn"], doc="Maximun nutrients per serving")
    model.Vmax = pyo.Param(initialize=data["Vmax"])
    model.Vf = pyo.Param(model.F, initialize=data["Vf"], doc="Volume consumption per saving")
    model.xf = pyo.Var(model.F, domain=pyo.NonNegativeReals, doc="Amount of food serving")

    #objective 

    def cost_function(model):
        return sum( model.cf[f]*model.xf[f] for f in model.F)

    model.objective = pyo.Objective(rule=cost_function, sense=pyo.minimize)


    def nutrient_limit_min(model, n):
        return model.Nminn[n] <= sum(model.afn[f,n]*model.xf[f] for f in model.F)

    def nutrient_limit_max(model, n):
     return sum(model.afn[f,n]*model.xf[f] for f in model.F) <= model.Nmaxn[n]

    model.nutrient_constraint_min = pyo.Constraint(model.N, rule=nutrient_limit_min, doc="nutrient limit constraint min")
    model.nutrient_constraint_max = pyo.Constraint(model.N, rule=nutrient_limit_max, doc="nutrient limit constraint max")


    def max_rule(model):
        return sum(model.xf[f]*model.Vf[f] for f in model.F) <= model.Vmax

    model.volume_contraint= pyo.Constraint(rule=max_rule, doc="volume constraint" )

    solver = pyo.SolverFactory('appsi_highs')

    solver.solve(model, tee=False)


    return {
        var: val.value for var,val in model.xf.items()
    }


