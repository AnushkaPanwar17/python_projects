# fake_news_generator.py
import random

# Sample fake news templates
fake_templates = [
    "Breaking: {} was seen doing something shocking today!",
    "Exclusive: {} has been caught in a scandal involving {}!",
    "Alert: Experts warn that {} might affect the world in unexpected ways.",
    "Latest Update: {} is trending after an unexpected event.",
    "Shocking: {} reveals a secret about {}!"
]

# Function to generate fake news
def generate_fake_news(subject, detail=""):
    template = random.choice(fake_templates)
    news = template.format(subject, detail)
    return news

# Main CLI program
def main():
    print("===== Fake News Generator =====")
    while True:
        subject = input("\nEnter the subject (or type 'exit' to quit): ")
        if subject.lower() == "exit":
            print("Exiting Fake News Generator. Stay safe!")
            break
        
        detail = input("Enter some detail (optional, press Enter to skip): ")
        
        fake_news = generate_fake_news(subject, detail)
        print("\nGenerated Fake News:")
        print(fake_news)

if __name__ == "__main__":
    main()