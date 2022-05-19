from enum import Enum

class FoodCategory(Enum):
  VEGETABLE = 1
  FRUIT = 2
  GRAIN = 3
  PROTEIN = 4
  DAIRY = 5
  OIL = 6 
  OTHER = 7

class FoodItem(object):
  def __init__(self, name, category, calories):
    if FoodCategory(category):
      self.category = category
    else:
      self.category = FoodCategory.OTHER
    self.calories = int(calories)
    self.name = name  
    
    #getter method
  def name(self):
    return self.name
  def category(self):
    return self.category
  def calories_per_100g(self):
    return self.calories 
  def __str__(self):
    return f"{self.name} ({self.category}) {self.calories}cal/100g"
    

class FoodServing (object):
  def __init__ (self, object, grams):#Food object and the amount of food in grams 
    self.foodIT = object
    self.grams = grams
    
  def food(self):
    return self.foodIT
    
  def amount(self):
    return self.grams

  def calories(self):
    serving = self.grams
    calorie_per_gram = (self.food()).calories_per_100g()
    total_calories = serving*(calorie_per_gram)/100
    return int(total_calories) 

  def __str__(self):
    return f"{self.grams}g of {self.foodIT}"



class Meal(object):
  def __init__(self):
    self.servings = []
  
  def addFood(self, FoodServing):
    (self.servings).append(FoodServing)
    
  def calories(self):
    total_calories = 0
    if len(self.servings) == 0:
      return total_calories
    for item in self.servings:
      current_calories = item.calories()
      total_calories += current_calories 
    return total_calories 

  def __str__(self):
    all_servings = ''
    for item in self.servings:
      all_servings += str(item) + '\n'
    return all_servings
      
    
    
    
    
    
    