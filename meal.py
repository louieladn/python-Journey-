def main():
    solution = input("What time is it?: ")
    time = convert(solution)
    # breakfast 7 to 8 
    if time >= 7 and time <= 8:
        print("breakfast")
    # lunch 12:00 and 13:00
    if time >= 12 and time <= 13:
        print("lunch")
    # dinner 18:00 and 19:00
    if time >= 18 and time <= 19:
        print("dinner")


def convert(time):
    hours, minutes = time.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes


if __name__ == "__main__":
    main()