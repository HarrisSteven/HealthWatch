from flask_restful import Resource
from flask import request

class ApiHandler(Resource):
  def get(self):
    num_questions = 17
    age = float(request.args.get('q0'))
    age_value = 0
    if age >= 80:
      age_value = 12
    elif age >= 75:
      age_value = 11
    elif age >= 70:
      age_value = 1
    elif age >= 65:
      age_value = 9
    elif age >= 60:
      age_value = 8
    elif age >= 55:
      age_value = 7
    elif age >= 50:
      age_value = 6
    elif age >= 45:
      age_value = 5
    elif age >= 40:
      age_value = 4
    elif age >= 35:
      age_value = 12
    elif age >= 30:
      age_value = 3
    elif age >= 25:
      age_value = 2
    else:
      age_value = 1

    p_health = float(request.args.get('q1'))
    m_health = float(request.args.get('q2'))
    sleep = float(request.args.get('q3'))
    bmi = float(request.args.get('q4'))
    gender = float(request.args.get('q5'))
    race = float(request.args.get('q6'))
    exercise = float(request.args.get('q7'))
    walking = float(request.args.get('q8'))
    smoking = float(request.args.get('q9'))
    drinking = float(request.args.get('q10'))
    stroke = float(request.args.get('q11'))
    diabetic = float(request.args.get('q12'))
    general_health = float(request.args.get('q13'))
    asthma = float(request.args.get('q14'))
    kidney = float(request.args.get('q15'))
    skin = float(request.args.get('q16'))

    heart_disease = 0.0116*bmi - 0.0250*smoking - 1.7683*drinking   \
    + 0.0046*m_health - 0.6474*walking + 0.3439*gender + 0.2993*age_value \
    + 0.0652*race + 0.4899*diabetic - 0.4550*p_health \
    - 0.9219*general_health - 0.0093*sleep - 0.8019*asthma \
    - 0.6515*kidney - 0.4634*skin

    has_heart_disease = "You are at risk of heart disease" if heart_disease > 0 else "You are not at risk of heart disease"

    return {
      'resultStatus': 'SUCCESS',
      'message': has_heart_disease
    }
