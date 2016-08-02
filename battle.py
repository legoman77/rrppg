def battle():
    
    # Player's stats
    
    p_health = 100
    p_offense = 15
    p_defense = 0
    
    # Enemies' stats
    
    e_health = 20
    e_offense = 10
    e_defense = 5
    
    # Battle
    
    print("You encounter a Slime!")
      while True:
        print("Health: " + str(p_health))
        print("Offense: " + str(p_offense))
        print("Defense: " + str(p_defense))
        print("What will you do?")
        print("1: Fight")
        print("2: Run")
        command = input("> ")
        print(c.clear)
                
        # Fight
    
        if command == "1":
          p_damage = p_offense - e_defense
          e_health -= p_damage
          print("You attack the Slime!")
          print("The Slime takes " + str(p_damage) + " damage!")
          if e_health <= 0:
            print("The Slime was defeated!")
            print("You won the battle!")
            break
          e_damage = e_offense - p_defense
          p_health -= e_damage
          print("The Slime attacks you!")
          print("You take " + str(e_damage) + " damage!")
          if p_health <= 0:
            print("You died!")
            print("GAME OVER")
            break
                
        # Run
    
        elif command == "2":
          pass
                
        # Invalid command
    
        else:
          print("That is not a valid command.")
