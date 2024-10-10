import speech_recognition as sr
import openai

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)

    # Send the text to ChatGPT for generating a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=50,
        temperature=0.7
    )

    # Print the generated response
    print("ChatGPT response:", response.choices[0].text.strip())

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
