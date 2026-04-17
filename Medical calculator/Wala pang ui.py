import math

def IVFlowRate():
    try:
        Volume = float(input("Volume(mL): "))
        Time = float(input("Time(Hours): "))
        
        if Time == 0:
            print("Time cannot be zero!")
            return
        
        Macrodrip = math.ceil((Volume/Time)/3)
        Microdrip = math.ceil((Volume/Time))
        PumpRate = round(Volume/Time, 2)
        
        print("DF:20 = " + str(Macrodrip) + " gtts/min")
        print("DF:60 = " + str(Microdrip) + " gtts/min")
        print("Pump Rate = " + str(PumpRate) + " mL/hr")
    
    except:
        print("Invalid input! Please enter numbers only.")

def Titration():
    try:
        Type = input("Type (dopamine/dobutamine/custom): ").lower()
        
        Dose = float(input("Dose: "))
        Weight = float(input("Weight(Kg): "))   
        
        if Type == "dopamine":
            result = math.ceil((Dose * Weight)/13.3)
        elif Type == "dobutamine":
            result = math.ceil((Dose * Weight)/16.6)
        else:
            concentration = float(input("Concentration: "))
            
            if concentration == 0:
                print("Concentration cannot be zero!")
                return
            
            result = math.ceil((Dose * Weight * 60)/concentration)
        
        print(str(result) + " gtts/min")
    
    except:
        print("Invalid input!")

def DrugDose():
    try:
        dose_per_kg = float(input("Ordered dose (mg/kg): "))
        weight = float(input("Weight (kg): "))
        stock_mg = float(input("Stock (mg): "))
        stock_ml = float(input("Stock Volume (mL): "))
        
        if stock_mg == 0:
            print("Stock mg cannot be zero!")
            return
        
        total_dose = dose_per_kg * weight
        volume_to_give = (total_dose / stock_mg) * stock_ml
        
        print("Total Dose = " + str(total_dose) + " mg")
        print("Give = " + str(round(volume_to_give,2)) + " mL")   
    
    except:
        print("Invalid input!")

def InfusionTime():
    try:
        volume = float(input("Volume (mL): "))
        rate = float(input("Rate (mL/hr): "))
        
        if rate == 0:
            print("Rate cannot be zero!")
            return
        
        time = volume / rate
        
        print("Time = " + str(round(time,2)) + " hours")
    
    except:
        print("Invalid input!")

def Conversions():
    print("1 = kg to lbs")
    print("2 = lbs to kg")
    print("3 = mg to g")
    
    choice = input("Choice: ")
    
    try:
        match choice:
            case "1":
                kg = float(input("kg: "))
                print(str(round(kg * 2.2,2)) + " lbs")
            case "2":
                lbs = float(input("lbs: "))
                print(str(round(lbs / 2.2,2)) + " kg")
            case "3":
                mg = float(input("mg: "))
                print(str(mg / 1000) + " g")
            case _:
                print("Invalid choice")
    
    except:
        print("Invalid input!")

while True:
    print("\nNURSING CALCULATOR")
    print("1 = IV Flow Rate")
    print("2 = Titration")
    print("3 = Drug Dose")
    print("4 = Infusion Time")
    print("5 = Conversions")
    print("0 = Exit")
    
    choice = input("Choice: ")
    
    match choice:
        case "1":
            IVFlowRate()
        case "2":
            Titration()
        case "3":
            DrugDose()
        case "4":
            InfusionTime()
        case "5":
            Conversions()
        case "0":
            break
        case _:
            print("Invalid choice")