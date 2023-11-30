import openai
import json
from flask import Flask, jsonify, request

openai.api_key = "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"

app = Flask(__name__)

def inputs_is_valid(num1,num2):

  # incase we have an empty input
  if num1 == None :
    num1 = 0
  if num2 == None :
    num2 = 0

  # this check if the string input is empty or not
  if type(num1)==str:
      if len(num1)==0:
         num1=0
      else:
         num1=int(num1)
  if type(num2)==str:
      if len(num2)==0:
         num2=0
      else:
         num2=int(num2)

  '''
    1-over here we need to find a way to retake inputs after
    this function ends if the inputs are invalid if necessary
    2- we also need to find a way to return empty string or empty input as 0
  '''
  return isinstance(num1, int) and isinstance(num2, int)


def chat_response(prompt):
    msg = [{"role": "user", "content": f'{prompt}'}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg,
        temperature=1,
    )
    return response.choices[0].message.content


@app.route("/add", methods=['POST'])
def addition():
  user_input = request.json
  a = user_input['num1']
  b = user_input['num2']

  inputs_is_valid(a,b)
  if not inputs_is_valid(a, b):
      return 'input is invalid, please enter valid inputs', 400

  sys_prompt = f'add {a} and {b}'
  response1 = chat_response(sys_prompt)

  try:
      x = response1.split()
      result = int(x[-1])
      return f"the addition is {result}", 200

  except ValueError:
      return f'the result could not be found', 500



if __name__ == '__main__':
  app.run(port=5099)





