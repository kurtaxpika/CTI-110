import random
# Create the car class

class Car:
    # Create an initializer function
    def __init__(self, make, model , color, driver, max_speed, handling ):
        self.make = make
        self.model = model
        self.color = color
        self.driver = driver 
        self.max_speed = max_speed
        self.handling = handling
        self.miles_driven = 0

    def show_car_info(self):
        print(f"The {self.make} {self.model} {self.color} is driven by {self.driver}")
        print ()
    def drive_car(self, miles_to_win):
        self.miles_driven += random.randint(5, self.max_speed) + self.handling
    def show_stats(self):
        print(f"{self.driver}'s car has advanced to {self.miles_driven} ꔮ !!")

        print()
        if self.miles_driven > 100:
            print(f"{self.driver} has won the race ᕙ(  •̀ ᗜ •́  )ᕗ🏆🥇🌿:✧˚  !!")


    def fan_pop_up(self):
        pop_up = random.randint(1,3)
        if pop_up == 1:
            print(f"A fan stopped to get a pc signed by {self.driver} (¬_¬'') !")
            reduce_speed = random.randint
            self.max_speed -= reduce_speed
            print(f"The max speed was reduced by {reduce_speed} ∘ ∘ ∘ ( °ヮ° ) ?")
            print()
        else:
            print(f"The fan wasn't noticed ...  (˚ ˃̣̣̥⌓˂̣̣̥ ) so, {self.driver} continued!")

def main():
    miles_to_win = 100
    # Create a car object
    joongCar = Car("Mazda", "Miata", "Black", "Kim Hongjoong", 60, 11)
    print()
    # Create a second car 
    hwaCar = Car("Toyota", "Mercedes", "Gray", "Park Seonghwa", 50, 20)

    print("⚡︎ The match is starting!!🏎️𖦹 ׂ 𓈒 🏁 ／ ⋆ ۪")
    print()

    # Call the instance function show_car_info
    joongCar.show_car_info()
    print()
    hwaCar.show_car_info()

    while joongCar.miles_driven < 100 and  hwaCar.miles_driven < 100:


    # Drive both cars one time 
        joongCar.drive_car()
        hwaCar.drive_car()
    
    # Show the updated 
    joongCar.show_stats(miles_to_win)
    hwaCar.show_stats(miles_to_win)


    # Call the fan pop up method on both cars!!
    joongCar.fan_pop_up()
    hwaCar.fan_pop_up()






if __name__ == "__main__":
  main()