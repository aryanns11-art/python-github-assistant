import random

class assistant:
    def __init__(self, name):
        self.name = name

    user_response = ["hi", "hello", "hey", "how are you", "hola"]
    
    exit_response = ["bye", "goodbye", "see you later"]

    github_dataset = {
    "what is git": "Git is a distributed version control system.",
    "what is github": "GitHub is a platform for hosting Git repositories.",
    "what is repository": "A repository is a project folder tracked by Git.",
    "what is commit": "A commit is a snapshot of your project at a specific point in time.",
    "what is branch": "A branch allows you to work on features independently.",
    "what is merge": "Merging combines changes from one branch into another.",
    "what is clone": "git clone downloads a remote repository to your computer.",
    "what is pull": "git pull fetches and merges changes from a remote repository.",
    "what is push": "git push uploads local commits to a remote repository.",
    "what is fork": "A fork is a copy of someone else's repository.",
    "how to create repository": "Create a repository on GitHub and connect it using git remote add origin.",
    "git init": "Initializes a new Git repository.",
    "git add": "Stages changes for the next commit.",
    "git commit": "Saves staged changes to the repository history.",
    "git status": "Shows the current state of your repository.",
    "git log": "Displays commit history.",
    "git checkout": "Switches branches.",
    "git branch": "Lists or creates branches.",
    "git merge": "Combines branches.",
    "git pull origin main": "Downloads and merges changes from the main branch.",
    "git push origin main": "Uploads local commits to the main branch."
   }

    def respond(self):
          
     responses = [
    "How can I help with GitHub?",
    "Need Git help?",
    "Ask me about GitHub.",
    "GitHub assistance ready.",
    "You can ask me about repositories.",
    "How can I assist?"
    ]
     return random.choice(responses)
    

users = {
    "aryan" : "aryan123",
    "sarah" : "sarah456",
}    
  
obj = assistant("MyAI")

print("MyAI: Hey there! I'm MyAI, your GitHub assistant.")

while True:

    print("Please login to access MyAI")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username] == password:

        while True:

            user = input("You: ").lower().strip().replace("?", "")

            if user in obj.user_response:
                print(f"MyAI: {obj.respond()}")

            elif user in obj.github_dataset:
                print(f"MyAI: {obj.github_dataset[user]}")

            elif user == "logout":
                print("You have been logged out.")
                break  

            elif user in obj.exit_response:
                print("MyAI: Goodbye!")
                exit()

            else:
                print("MyAI: I don't understand that. Try a GitHub question.")

    else:
     print("Invalid username or password. Access denied.")