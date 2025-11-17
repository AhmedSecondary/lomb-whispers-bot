import requests
import os
import random

token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

messages = [
    "Good morning, lomb. I hope today feels light and kind to you.",
    "Lomb, don’t forget to drink some water today.",
    "May Allah make your day peaceful, lomb.",
    "Take a deep breath, lomb. You’re doing better than you think.",
    "Lomb, I hope your morning is calm and your heart is at ease.",
    "If today gets heavy, remember Allah is with you, lomb.",
    "Lomb, make a small dua today — even one sentence counts.",
    "You deserve gentleness today, lomb.",
    "Lomb, may Allah open doors for you that you didn’t expect.",
    "I hope you smile at least once today, lomb.",
    "Lomb, take things slowly today. One step at a time.",
    "May your heart stay soft today, lomb.",
    "Lomb, remember to rest when you need it.",
    "Sending you calmness for today, lomb.",
    "Lomb, you’re stronger than the stress you feel.",
    "May your thoughts be light today, lomb.",
    "Lomb, Allah never burdens a soul beyond what it can bear.",
    "You deserve peace, lomb. Not pressure.",
    "Lomb, don’t forget to breathe and reset when needed.",
    "May Allah protect your mind and heart today, lomb.",
    "A quiet reminder for you, lomb: you matter.",
    "Lomb, I hope your day has a soft moment for you.",
    "May today bring you something tiny but good, lomb.",
    "Lomb, trust Allah with what you can’t control.",
    "You have a gentle strength, lomb.",
    "Lomb, remember to be kind to yourself today.",
    "May your plans go smoothly today, lomb.",
    "Lomb, if things get overwhelming, take a short pause.",
    "You are doing your best, lomb — and that’s enough.",
    "Lomb, may Allah lighten your worries today.",
    "Sending you a quiet prayer for ease today, lomb.",
    "Lomb, your effort means something — even if you don’t see it.",
    "I hope you find a small moment of joy today, lomb.",
    "Lomb, one calm breath can change a moment.",
    "May your evening be soft and restful, lomb.",
    "Lomb, you deserve peace in your mind today.",
    "Don’t rush yourself today, lomb. Move gently.",
    "Lomb, I hope someone is kind to you today — even a stranger.",
    "May Allah give you clarity in your thoughts, lomb.",
    "Lomb, if your day is hard, remember ease comes after difficulty.",
    "Sending you a bit of calm energy for today, lomb.",
    "Lomb, trust that better days are always on the way.",
    "I hope your night comes with rest, lomb.",
    "Lomb, close your eyes for a moment and reset your heart.",
    "May Allah protect your emotions today, lomb.",
    "Lomb, don’t forget to take care of your body and mind.",
    "You have a quiet kindness, lomb — keep it.",
    "Lomb, whatever you face today, you won’t face it alone.",
    "Wishing you a peaceful day, lomb — truly."
]




url = f"https://api.telegram.org/bot{token}/sendMessage"

payload = {
    "chat_id": chat_id,
    "text": random.choice(messages)
}

response = requests.post(url, data=payload)