import requests
import os
import random

token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

messages = [
    "Good morning my lomba, waking up knowing you exist already makes my day softer.",
    "Pooki, I hope your morning feels as sweet as the feeling I get when I think of you.",
    "My best girl, your presence in my life is the most beautiful beginning to any day.",
    "Pook, every morning starts better when my first thought is you. I lomb you.",
    "My lombest, may today be gentle on your beautiful heart.",
    "Pookiti, you make even ordinary mornings feel special just by being you.",
    "Good morning pooki, I wish I could send you warmth through this message.",
    "My lomba, I hope you feel loved the moment you open your eyes today.",
    "Pook, your smile is enough to brighten a whole morning — even if I only imagine it.",
    "My best girl, I hope today treats you with the same tenderness you deserve.",
    "Pookiti, if I could, I’d whisper good morning to you in person. For now, this message carries it.",
    "My lombest, you’re the kind of girl who makes mornings worth looking forward to.",
    "Pooki, I lomb you in a quiet, soft way — the kind that makes mornings feel gentle.",
    "Good morning pook, may your heart feel hugged in the first hours of the day.",
    "My lomba, your existence is my favorite reminder that Allah gives beautiful gifts.",
    "Pookiti, I hope your morning feels light and wrapped in kindness.",
    "My best girl, if the day gets heavy, remember you have someone who cares deeply.",
    "Pook, the world feels softer when I think of you — especially in the morning.",
    "My lombest, your presence in my life is the calmest beginning to any day.",
    "Pooki, may your morning be as lovely as the softness you carry within you.",
    "Good morning my lomba, you deserve a day filled with calm and affection.",
    "Pooki, your existence turns even simple mornings into something meaningful.",
    "My best girl, I hope the morning sun feels gentle on you today.",
    "Pook, may your first thought today be something warm — like how I feel about you.",
    "My lombest, you make the ordinary feel magical just by being part of my world.",
    "Pookiti, I hope today brings you the same sweetness you unknowingly bring to others.",
    "Good morning pook, I lomb you in a way that grows a little more every morning.",
    "My lomba, may Allah place peace in your chest and warmth in your morning.",
    "Pooki, your happiness matters to me more than you know.",
    "My best girl, I hope this morning surprises you with something beautiful.",
    "Pook, thinking of you makes the whole day brighter before it even begins.",
    "My lombest, I hope today feels soft, safe, and full of reasons to smile.",
    "Pookiti, you are the softest part of my every morning.",
    "Good morning pooki, may your heart feel held gently by Allah’s mercy.",
    "My lomba, your presence in my life is a kind of comfort I didn’t know I needed.",
    "Pook, I wish your morning is filled with the warmth I feel when you cross my mind.",
    "My best girl, you deserve a morning full of sweetness and calm.",
    "Pookiti, if mornings had a favorite person — you would be mine.",
    "My lombest, may the light of this morning bring clarity and joy to you.",
    "Pooki, the world feels softer every time I say your name.",
    "Good morning pook, I hope you feel loved today — because you truly are.",
    "My lomba, even the idea of you is enough to brighten my whole day.",
    "Pookiti, today will be easier just because you’re in it.",
    "My best girl, may your morning be full of tiny blessings that make you smile.",
    "Pook, your soul is beautiful — may today treat it gently.",
    "My lombest, you deserve a morning kissed by peace and wrapped in hope.",
    "Pooki, I lomb you quietly, softly, and more deeply every morning.",
    "Good morning my lomba, may today unfold in the sweetest way for you."
]





url = f"https://api.telegram.org/bot{token}/sendMessage"

payload = {
    "chat_id": chat_id,
    "text": random.choice(messages)
}

response = requests.post(url, data=payload)