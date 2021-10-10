while True:
    run_code = input("Would you like to see the 40 latest titles from Hacker news?\n"
                     "Please enter 'yes' or 'no'. ").lower()
    try:
        if run_code == "yes":
            import extract_titles
            break
        if run_code == "no":
            print("See you next time!")
            break
    except:
        pass
    else:
        print("Enter 'yes' or 'no'")

