
# Select a voice: Allison, Ava (Default), Evelyn, Samantha, Susan, Zoe
voice = "Zoe"
# Test voices
"""
voices = ("Allison", "Ava", "Evelyn", "Samantha", "Susan", "Zoe")
for v in voices:
    say("{} thanks you for calling Butch Bando's Fantasy of Lights.".format(v), {
        "voice":v
    })
"""

# Select peak-season (True) or off-season (False)
peak_season = True

# Select simple outbound message or complex options
simple = False

# Set hours
weekdays = "Monday through Thursday"
weekends = "Friday through Sunday"
weekday_start = "5:30pm"
weekday_end = "9:30pm"
weekend_start = "5:30pm"
weekend_end = "10:30pm"

# Set costs
weekday_car = "$20"
weekend_car = "$30"
prices_dict = {
    "Cars, {}".format(weekdays):"$20",
    "Cars, {}".format(weekends):"$30",
    "Limos, Large Vans, and Motorhomes":"$40",
    "Motor Coaches, up to 30 people":"$60",
    "Buses and Large Motor Coaches":"$100"
}
prices = (
    "For Cars, {}, the cost is $20".format(weekdays),
    "For Cars, {}, the cost is $30".format(weekends),
    "For Limos, Large Vans, and Motorhomes, the cost is $40",
    "For Motor Coaches, up to 30 people, the cost is $60",
    "For Buses and Large Motor Coaches, the cost is $100"
    )

# Outbound call forward number
outbound_number = "+16145601371"
outbound_enable = True

# Default greeting
def greeting(peak_season):
    if peak_season == True:
        say("Thank you for calling Butch Bando's Fantasy of Lights.", {
            "voice":voice
        })
        say("Come see our new, all L.E.D. light display, now through January 1st, at the Alum Creek State Park Campgrounds.", {
            "voice":voice
        })
        return True
    else:
        say("Thank you for calling Butch Bando's Fantasy of Lights.", {
            "voice":voice
        })
        say("We hope you enjoyed the twenty-seventeen show. Please come back and see us next year.", {
            "voice":voice
        })
        return False

# Return to main menu
def main_menu():
    selection = ask("Please press star to return to the main menu.", {
        "choices":"*",
        "voice":voice,
        "timeout":5.0
    })
    if selection.value == "*":
        return True
    else:
        return False

# Simple script
def main_simple():
    say("{} we are open from {} until {}, and the cost is {} per car.".format(weekdays, weekday_start, weekday_end, weekday_car), {
        "voice":voice
    })
    say("{} we are open from {} until {}, and the cost is {} per car.".format(weekends, weekend_start, weekend_end, weekend_car), {
        "voice":voice
    })
    say("For group rates and available discounts, please stay on the line for more information.", {
        "voice":voice
    })
    if outbound_enable == True:
        selection = ask("If you would like to speak to someone, please press 0 now.", {
            "voice":voice,
            "choices":"0",
            "timeout":10.0
        })
        if selection.value == "0":
            say("Ok, we are transfering you now.", {
                "voice":voice
            })
            transfer(outbound_number, {
                "onTimeout": lambda event : say("Sorry, but nobody answered.", {"voice":voice})
            })


# Main Script
def main():
    exit = False
    while exit == False:
        wait(1000)
        selection = ask("For hours, please press 1. For show prices, please press 2. For location and directions, please press 3. To speak to someone, please press 0.", {
            "voice":voice,
            "choices":"1,2,3,0",
            "timeout":10.0
        })
        if selection.value == "1":
            say("{} we are open from {} until {}.".format(weekdays, weekday_start, weekday_end), {
                "voice":voice
            })
            say("{} we are open from {} until {}.".format(weekends, weekend_start, weekend_end), {
                "voice":voice
            })
            wait(1000)
            if main_menu() == False:
                exit = True
        elif selection.value == "2":
            say("Our show prices are as follows:", {
                "voice":voice
            })
            for p in prices:
                say("{}".format(p), {
                    "voice":voice
                })
            say("Senior living and assisted living homes may be eligible for discounted rates. When prompted, return to the main menu to speak to someone about discounts.", {
                "voice":voice
            })
            wait(1000)
            if main_menu() == False:
                exit = True
        elif selection.value == "3":
            say("Our show is located at the Alum Creek State Park Campgrounds, at 3311 South Old State Road, in Delaware Ohio.", {
                "voice":voice
            })
            say("Cars, please enter through the service entrance, a half mile south of the campground's main entrance.", {
                "voice":voice
            })
            say("Buses, please use the campground's main entrance.", {
                "voice":voice
            })
            wait(1000)
            if main_menu() == False:
                exit = True
        elif selection.value == "0":
            say("Ok, we are transfering you now.", {
                "voice":voice
            })
            transfer(outbound_number, {
                "timeout":30.0,
                "onTimeout": lambda event : say("Sorry, but nobody answered.", {"voice":voice}),
            })
            exit = True
        else:
            pass


    say("Thank you for calling Butch Bando's Fantasy of Lights. Please come see us soon.", {
        "voice":voice
    })

# Execute main script
if greeting(peak_season) == True:
    if simple == True:
        main_simple()
    else:
        main()
