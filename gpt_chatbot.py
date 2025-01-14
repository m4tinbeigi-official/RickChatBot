from transformers import pipeline

# استفاده از مدل GPT-2
chatbot = pipeline("text-generation", model="gpt2")

print("چت‌بات: سلام! سوالی دارید؟")
while True:
    user_input = input("شما: ")
    if user_input.lower() == "خداحافظ":
        print("چت‌بات: خداحافظ!")
        break
    response = chatbot(user_input, max_length=50)[0]['generated_text']
    print(f"چت‌بات: {response}")