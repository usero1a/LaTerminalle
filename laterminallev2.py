import time
import random
import math
import os

apps = {
    "calculator": (
        "import math\n"
        "allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith('__')}\n"
        "print('📐Calculator — type \"exit\" to quit')\n"
        "while True:\n"
        "    expr = input('>> ')\n"
        "    if expr.lower() in ['exit', 'quit']:\n"
        "        break\n"
        "    try:\n"
        "        result = eval(expr, {'__builtins__': None}, allowed_names)\n"
        "        print('= ', result)\n"
        "    except Exception as e:\n"
        "        print('Error:', e)"
    ),

    "pybot": (
        "import time\n"
        "name = input('💬 What is your name? ')\n"
        "print(f'Hello {name}! Nice to meet you!')\n"
        "time.sleep(1)\n"
        "age = int(input('How old are you? '))\n"
        "sure = input(f'💬 So you are {age} years old? ')\n"
        "cool = input(f'💬 So.. {name}, What do you like doing? ')\n"
        "print(cool + ', I like that too.')\n"
        "time.sleep(2)\n"
        "print('bye! 👋')"
    ),

    "dice": (
        "import random\n"
        "print(f'🎲 You rolled a {random.randint(1,6)}')"
    ),

    "random-article": (
        "import random\n"
        "r = [\n"
        "    '📰 News: Robot marathon - https://news.sky.com/story/china-hosts-worlds-first-half-marathon-race-between-humans-and-robots-13351485',\n"
        "    '📰 News: Bear slide - https://apnews.com/article/bear-slide-connecticut-1f64b1e5fe5541d1f3985fe161956201',\n"
        "    '📰 Fun fact: Buffalo sentence - https://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo',\n"
        "    '📰 Fun fact: Longest word - https://en.wikipedia.org/wiki/Longest_word_in_English'\n"
        "]\n"
        "t = input('Do you want a random article? (y/n) ')\n"
        "if t.lower() == 'y':\n"
        "    print(random.choice(r))"
    ),

    "random-games": (
        "import random\n"
        "r = [\n"
        "    '📰 News: Robot marathon - https://news.sky.com/story/china-hosts-worlds-first-half-marathon-race-between-humans-and-robots-13351485',\n"
        "    '📰 News: Bear slide - https://apnews.com/article/bear-slide-connecticut-1f64b1e5fe5541d1f3985fe161956201',\n"
        "    '📰 Fun fact: Buffalo sentence - https://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo',\n"
        "    '📰 Fun fact: Longest word - https://en.wikipedia.org/wiki/Longest_word_in_English'\n"
        "]\n"
        "t = input('Do you want a random article? (y/n) ')\n"
        "if t.lower() == 'y':\n"
        "    print(random.choice(r))"
    ),

    "python-vim": (
        "print('***************** Welcome to Python Vim *****************')\n"
        "print('***************** Vi Improved *****************')\n"
        "print('Type to code')\n"
        "print('Enter to save.')\n"
        "code = input('')"
    ),

    "python-nano": (
        "print('***************** Welcome to Python Nano *****************')\n"
        "print('^G help   ^O Write Out   ^W Where Is   ^K Cut    ^T Execute   ^Location')\n"
        "print('Type your text below. Type \"^O\" to quit and save.')\n"
        "text = []\n"
        "while True:\n"
        "    line = input('')\n"
        "    if line.upper() == '^O':\n"
        "        print('Saving your work...')\n"
        "        break\n"
        "    text.append(line)\n"
    ),  

    "python-rps": (
        "import time\n"
        "import random\n"
        "print('Rock, Paper, Scissors! ')\n"
        "print(' ')\n"
        "plaything = input('Would you like to play? (y/n) > ')\n"
        "if plaything == 'y':\n"
        "    while True:\n"
        "        print('Choose difficulty: Easy, Medium, UNBEATABLE ')\n"
        "        difficulty = input('> ')\n"
        "        if difficulty == 'easy':\n"
        "            exprmove = input('Choose your action, (Rock, Paper, Scissors) > ')\n"
        "            if exprmove == 'rock':\n"
        "                print('AI Chose Scissors, You win!')\n"
        "            elif exprmove == 'scissors':\n"
        "                print('AI Chose paper, You win!')\n"
        "            elif exprmove == 'paper':\n"
        "                print('AI chose Rock, You win!')\n"
        "        elif difficulty == 'medium':\n"
        "            exprmove = input('Choose your action, (Rock, Paper, Scissors) > ')\n"
        "            if exprmove in ['rock', 'paper', 'scissors']:\n"
        "                list = ['Rock', 'Paper', 'Scissors']\n"
        "                print('AI is thinking...')\n"
        "                time.sleep(3)\n"
        "                ai_choice = random.choice(list)\n"
        "                print('AI chose ' + ai_choice)\n"
        "                if exprmove == 'rock':\n"
        "                    if ai_choice == 'Paper':\n"
        "                        print('AI won, you lost!')\n"
        "                    elif ai_choice == 'Scissors':\n"
        "                        print('AI Lost, you win!')\n"
        "                    else:\n"
        "                        print('It\\'s a tie!')\n"
        "                elif exprmove == 'paper':\n"
        "                    if ai_choice == 'Paper':\n"
        "                        print('It\\'s a tie!')\n"
        "                    elif ai_choice == 'Scissors':\n"
        "                        print('AI won, you lost!')\n"
        "                    else:\n"
        "                        print('AI lost, you win!')\n"
        "                elif exprmove == 'scissors':\n"
        "                    if ai_choice == 'Paper':\n"
        "                        print('AI lost, you win!')\n"
        "                    elif ai_choice == 'Rock':\n"
        "                        print('AI won, you lost!')\n"
        "                    else:\n"
        "                        print('It\\'s a tie!')\n"
        "            else:\n"
        "                print('Invalid move. Try again.')\n"
        "        elif difficulty == 'unbeatable':\n"
        "            exprmove = input('Choose your action, (Rock, Paper, Scissors) > ')\n"
        "            if exprmove == 'rock':\n"
        "                print('AI is thinking...')\n"
        "                time.sleep(7)\n"
        "                print('AI Chose Paper, You lost!')\n"
        "            elif exprmove == 'scissors':\n"
        "                print('AI is thinking...')\n"
        "                time.sleep(7)\n"
        "                print('AI Chose Rock, You lost!')\n"
        "            elif exprmove == 'paper':\n"
        "                print('AI is thinking...')\n"
        "                time.sleep(7)\n"
        "                print('AI chose Scissors, You lost!')\n"
        "            else:\n"
        "                print('Invalid move. Try again.')\n"
    )
}

installed_apps = []
users = {}
app = "💬 available commands: echo, say-hi, compliment, app-store, la install, device-info, register, login"
app_store = "🔧 Available apps in store: " + ", ".join(apps.keys())

try:
    with open('users.txt', 'r') as f:
        for line in f:
            if line.strip():
                username, password = line.strip().split(':', 1)
                users[username] = password
except FileNotFoundError:
    pass

print("loading...")
time.sleep(3)
print("NEWS: 🧑‍💻 LaTerminalle has been updated to version 2.0!")
print("Welcome to 🧑‍💻  LaTerminalle! Made by Ufan")
y = input("Do you want to install MegaTerminal by Ufan? (y/n) > ")

if y == "y":
    print("Installing 🧑‍💻 LaTerminalle...")
    time.sleep(4)
    
    choice = input("Do you have an account? (login/register/local) > ").lower()
    
    if choice == "register":
        username = input("Enter new username > ")
        if username in users:
            print("❌ Username already exists!")
            x = input("Please enter a guest username > ")
        else:
            password = input("Enter password > ")
            users[username] = password
            with open('users.txt', 'a') as f:
                f.write(f"{username}:{password}\n")
            print(f"✅ User {username} registered successfully!")
            x = username
            
    elif choice == "login":
        username = input("Enter username > ")
        password = input("Enter password > ")
        if username in users and users[username] == password:
            print(f"✅ Welcome back, {username}!")
            x = username
        else:
            print("❌ Invalid username or password!")
            x = input("Please enter a guest username > ")
            
    elif choice == "local":
        x = input("Please enter a guest username > ")
        
    else:
        x = input("Please enter your username > ")
    
    print("Now optimizing your experience, " + x)
    time.sleep(2)
    print("Installing apps...")
    time.sleep(3)
    print("LaTerminalle has been installed")
    print("Hint: type help for available commands")
    print("")
    time.sleep(2)

while True:
    m = input("$"+ x + " > ")

    if m == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    elif m == "say-hi":
        print("👋 Greetings " + x)

    elif m == "echo":
        echo = input("What do you want me to say? >> ")
        print(echo)

    elif m == "help":
        print(app)
        if installed_apps:
            print("Installed apps: " + ", ".join(installed_apps))

    elif m == "compliment":
        list = ["Your hair looks nice.", "You're very smart", "You're pretty cool",
                "Watch https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=0gcJCdgAo7VqN5tD",
                "Watch this too.. https://www.google.com/search?q=realistic-wallace"]
        print("💬 " + random.choice(list))

    elif m == "app-store":
        print(app_store)

    elif m.startswith("la install "):
        app_name = m.replace("la install ", "")
        if app_name in apps:
            if app_name not in installed_apps:
                installed_apps.append(app_name)
                print(f'installing {app_name}...')
                time.sleep(2.5)
                print(f"✅ Installed {app_name}\nTo use it type '{app_name}'")
            else:
                print("⚠️ App already installed!")
        else:
            print("❌ App not found in store\nTo check what apps are run 'app-store'")

    elif m in installed_apps:
        exec(apps[m])

    elif m == "device-info":
        print("🧑‍💻 LaTerminalle\nVersion: 2.0.0\nAvailable commands: " + app)
        print("Installed apps: " + ", ".join(installed_apps))

    elif m == "register":
        username = input("Enter new username > ")
        if username in users:
            print("❌ Username already exists!")
        else:
            password = input("Enter password > ")
            users[username] = password
            with open('users.txt', 'a') as f:
                f.write(f"{username}:{password}\n")
            print(f"✅ User {username} registered successfully!")

    elif m == "login":
        username = input("Enter username > ")
        password = input("Enter password > ")
        if username in users and users[username] == password:
            print(f"✅ Welcome back, {username}!")
            x = username
        else:
            print("❌ Invalid username or password!")

    else:
        print(m + " not found")
