from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# ایجاد یک چت‌بات
chatbot = ChatBot("MyBot")

# آموزش چت‌بات با داده‌های ساده
trainer = ListTrainer(chatbot)
trainer.train([
    "سلام",
    "سلام! چطور می‌تونم کمک‌تون کنم؟",
    "چطوری می‌تونم رمز عبورم رو تغییر بدم؟",
    "به بخش تنظیمات بروید و گزینه تغییر رمز عبور را انتخاب کنید.",
    "ساعت کار شرکت چند است؟",
    "ساعت کار شرکت از ۸ صبح تا ۵ بعدازظهر است."
])

# شروع چت
print("چت‌بات: سلام! سوالی دارید؟")
while True:
    user_input = input("شما: ")
    if user_input.lower() == "خداحافظ":
        print("چت‌بات: خداحافظ!")
        break
    response = chatbot.get_response(user_input)
    print(f"چت‌بات: {response}")