from config import app, migrate

from models import db

from helpers import *

def display_main_menu():
  print("1 View routine(s)")
  print("2 Create a new routine")
  print("3 Exit")

# inputs

def get_choice():
  return input("Please enter your selection: ")

def get_input(str):
  return input(str)

def exit():
  print("Enjoy your day with your Bubba(s)!")

def display_all_dogs():
  dogs = get_all_dogs()
  for dog in dogs:
    print(dog)

def create_new_dog():
  dog_name = get_input("What is the name of your dog? ")
  new_dog = Dog(name = dog_name)
  db.session.add(new_dog)
  db.session.commit()
  return new_dog

def create_day(dog, day):
  type = "GROOMING"
  print(f"Please add any {type} activities that you'll be doing with {dog.name.upper()} on {day}.")
  print("When you're finished, press C to continue.")
  activities = get_activities_by_type(type)
  for activity in activities:
    print(f"{activity.id} {activity.activity}")
  selection = input("Add an activity: ")
  new_routine = Routine(
    dog_id = dog.id,
    activity_id = selection,
    day = day,
     comment = ""
  )
  db.session.add(new_routine)
  db.session.commit()


if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    print("ROUTINE BUBBA")
    print("Hello!")
    display_main_menu()
    choice = get_choice()
    if choice == '1':
      print(choice)
    elif choice == '2':
      dog = create_new_dog()
      print(f"Great! Let's create a new routine for {dog.name.upper()}.")
      create_day(dog, "Monday")
    else:
      exit()