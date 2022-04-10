import React from 'react';
import RadioQuestion from './RadioQuestion';
import ValueQuestion from './ValueQuestion';

const Questions = (props) => {
  const answers = props.answers;
  const setAnswers = props.setAnswers;

  const questions = [
    {"question": "Age", "type": "value", "max": 120},
    {"question": "How many days during the past 30 days was your physical health not good?", "type": "value", "max": 30},
    {"question": "How many days during the past 30 was your mental health not good?", "type": "value", "max": 30},
    {"question": "On average how many hours of sleep do you get?", "type": "value", "max": 24},
    {"question": "Body Mass Index (BMI)", "type": "value", "max": 50},
    {"question": "Gender", "type": "radio", "choices": ["Female", "Male", "Other"]},
    {"question": "Race", "type": "radio", "choices": ["American Indian/Alaskan Native","Asian","Black","Hispanic","White","Other"]},
    {"question": "Do you engage in regular physical exercise?", "type": "radio", "choices": ["No", "Yes"]},
    {"question": "Do you have serious difficulty walking or climbing stairs?", "type": "radio", "choices": ["No", "Yes"]},
    {"question": "Have you smoked at least 100 cigarettes in your entire life?", "type": "radio", "choices": ["No", "Yes"]},
    {"question": "Are you a heavy drinker? (more than 14 alcoholic drinks per week)", "type": "radio", "choices": ["No", "Yes"]},
    {"question": "Have you had a stroke?", "type": "radio", "choices": ["No", "Yes"]},
    {"question": "Are you diabetic?", "type": "radio", "choices": ["No", "Yes"]},
    {"question": "How would you describe your general health?", "type": "radio", "choices": ["Poor", "Fair", "Good", "Very Good", "Excellent"]},
    {"question": "Do you have asthma?", "type": "radio", "choices": ["No", "Yes"]},
    {"question": "Do you have kidney disease?", "type": "radio", "choices": ["No", "Yes"]},
    {"question": "Do you have skin cancer?", "type": "radio", "choices": ["No", "Yes"]},
  ]

  return (
    <div>
      {questions.map((q, index) => (
        q.type === "radio" ? 
          <RadioQuestion key={q.question} index={index} question={q.question} choices={q.choices} answers={answers} setAnswers={setAnswers}/>
        : <ValueQuestion key={q.question} index={index} question={q.question} max={q.max} answers={answers} setAnswers={setAnswers}/>
      ))}      
    </div>
  );
};

export default Questions;
