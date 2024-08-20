import random
import string

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = [
        random.choice(string.ascii_uppercase), 
        random.choice(string.ascii_lowercase), 
        random.choice(string.digits),          
        random.choice(string.punctuation)      
    ]
    
    password += random.choices(all_characters, k=length-4)
    
    random.shuffle(password)
    
    return ''.join(password)

password = generate_password(16) 
print(f"Generated Password: {password}")
