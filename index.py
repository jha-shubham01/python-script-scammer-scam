import random
from datetime import datetime, timedelta
import multiprocessing
import requests

def parallel_function(func, num_processes):
    processes = []

    for _ in range(num_processes):
        p = multiprocessing.Process(target=func)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


def generate_name():
    adjectives = [
        'Happy',
        'Silly',
        'Clever',
        'Funny',
        'Brave',
        'Kind',
        'Energetic',
        'Wise',
        'Creative',
        'Generous',
        'Honest',
        'Sincere',
        'Charming',
        'Gracious',
        'Playful',
        'Reliable',
        'Patient',
        'Calm',
        'Curious',
        'Gentle',
        'Loyal',
        'Polite',
        'Confident',
        'Adventurous',
        'Ambitious',
        'Thoughtful',
        'Determined',
        'Witty',
        'Optimistic',
        'Talented',
        'Modest',
        'Romantic',
        'Sensible',
        'Sociable',
        'Humble',
        'Intelligent',
        'Passionate',
        'Resourceful',
        'Resilient',
        'Empathetic',
        'Diligent',
        'Flexible',
        'Sincere',
        'Trustworthy',
        'Vibrant',
        'Enthusiastic',
        'Innovative',
        'Caring',
        'Tenacious',
        'Friendly'
    ]
    nouns = [
        'Cat',
        'Dog',
        'Bird',
        'Fish',
        'Elephant',
        'Lion',
        'Tiger',
        'Monkey',
        'Giraffe',
        'Kangaroo',
        'Zebra',
        'Horse',
        'Rabbit',
        'Mouse',
        'Bear',
        'Dolphin',
        'Shark',
        'Whale',
        'Penguin',
        'Owl',
        'Butterfly',
        'Ant',
        'Snail',
        'Turtle',
        'Dragonfly',
        'Spider',
        'Bee',
        'Flamingo',
        'Peacock',
        'Octopus',
        'Starfish',
        'Lobster',
        'Crab',
        'Duck',
        'Swan',
        'Squirrel',
        'Koala',
        'Gorilla',
        'Panda',
        'Pig',
        'Sheep',
        'Cow',
        'Rooster',
        'Deer',
        'Wolf',
        'Fox',
        'Raccoon',
        'Hedgehog',
        'Otter',
        'Seagull',
        'Pelican',
        'Hummingbird'
    ]
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    return f"{adjective} {noun}"


def generate_phone_number():
    return ''.join(random.choice('0123456789') for _ in range(10))


def generate_random_date():
    start_date = datetime(2001, 1, 1)
    end_date = datetime.now()
    
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.strftime("%d-%m-%Y")


def call_scammer():
    # Code for your function
    print("call_scammer called")
    url = "https://onlinecustomercare.site/wp-admin/admin-ajax.php"
    form_data = {
        "name-1": generate_name(),
        "phone-1": generate_phone_number(),
        "phone-2": generate_random_date(),
        "select-1": "one",
        "referer_url": "",
        "forminator_nonce": "f347ae9c0a",
        "_wp_http_referer": "/sbi-credit-card/",
        "form_id": "49",
        "page_id": "6",
        "form_type": "default",
        "current_url": "https://onlinecustomercare.site/sbi-credit-card/",
        "render_id": "0",
        "action": "forminator_submit_form_custom-forms",
    }
    response = requests.post(url, form_data)
    print(f"Response of the request is: {response.ok}")



parallel_function(call_scammer, 100)