from flask_restful import Resource
from flask import request

class HelloApiHandler(Resource):
  def get(self):
    num_questions = 17
    answers = []
    for i in range(num_questions):
      answers.append(request.args.get('q'+str(i)))
    print(answers)

    return {
      'resultStatus': 'SUCCESS',
      'message': "Result of ML processing"
      }
