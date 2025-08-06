import time


         
                   
    

def guess_game():
    import random
    
    list = ["goku", "naruto", "luffy", "ichigo", "tanjiro", "zenitsu", "inosuke",
    "nezuko", "gojo", "sukuna", "megumi", "itadori",
    "lucy", "zoro", "sanji", "nami","ace", "yamato", "kakashi", "obito",
    "madara", "itachi", "sasuke", "sakura", "jiraiya", "minato", "boruto",
    "sarada", "hinata", "nagato", "pain", "konan", "deidara",
    "gaara", "rocklee", "shikamaru", "ino", "neji", "tenten", "tsunade",
    "orochimaru", "aizen", "rukia", "yuno", "asta",
    "todoroki", "midoriya",  "dazai","vegeta", "bulma", "piccolo", "beerus", "whis", "cell",
    "freiza", "gohan", "trunks","l","light"]
 
    def difficulty():              
       lives = input("   Choose Lives:(8💀/5💀💀/3💀💀💀) ")
       if lives == "8":
           return 8 
       elif lives == "3":
            return 3
       else:
     	   return 5
 
    word = random.choice(list)
    guess = ["_"for _ in word]
    guessed_list = []
    lives = difficulty()
    print(" " * 11 + "Guess the anime character")    
        
        
    while lives > 0:
        print(f"\n                     👉{" ".join(guess)}👈")
        print(f"\n   Lives left: {'♥️' * lives}")
        print(f"   Guessed Letters:{" ".join(guessed_list)}")
        
        new = input("   Enter a letter:\n   ").lower()
        
        if new in guessed_list:
            print("   This letter is already present😶")
            continue 
        
        guessed_list.append(new)    
        
        if new in word:
            print("   Correct 💯") 
            time.sleep(0.8)
            for i in range(len(word)):
                if word[i] == new:
                    guess[i] = new
        
        
        else:
            print("   ❌Wrong Try again")  
            lives -= 1
            time.sleep(0.8)
            
        if "_" not  in guess:
           print(f"\n                     👉{" ".join(guess)}👈")
           print("   congrats🎉 you have won🏆")             
           break                    
    
    
    
    else:
        print(f"   you're out of tries😛.\n   The word was {word}")
        time.sleep(1)
            
def play_again():
   again = input("   Play Again?(yes/no)").lower().lstrip()
   time.sleep(1)
   return again == "yes" 
   
                                         
while True:
    guess_game()
    if not play_again():
        print("🫂Good Bye...👋")               