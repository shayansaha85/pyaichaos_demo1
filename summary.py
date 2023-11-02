import openai
from jproperties import Properties

properties = Properties()

with open("./pyaichaos_demo1/chaos_config.properties", 'rb') as f:
    properties.load(f, "utf-8")


perc = str(properties.get('percentage').data)
cores = str(properties.get('cores').data)
duration = str(properties.get('duration').data)

apikeyfile = open("E:\\OpenAI\\apikey.txt","r")
keyval = apikeyfile.read().strip()
apikeyfile.close()
api_key = keyval
openai.api_key = api_key


def ask_chat(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content']
your_question = f"Write HTML content of a report for a chaos experiment done on CentOS machine. We occupied {perc}% CPU for {duration}s duration. Wirte description on Chaos testing, CPU Chaos Testing, and a brief about the chaos experiment. Write it in a professional report style. In a newsletter format for sending email report"

answer = ask_chat(your_question)

file = open("report.html", "w")
file.write(answer)
file.close()
