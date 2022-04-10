import React, { useState } from 'react';
import Button from '@mui/material/Button';
import Questions from './Components/Questions';
import axios from 'axios';

const App = () => {
  const [isQuizShowing, toggleQuiz] = useState(false);
  const [response, setResponse] = useState({})
  const [isSubmit, setSubmit] = useState(false);
  const [isWarningShowing, toggleWarning] = useState(false);

  let template = [];
  const numQuestions = 17;
  for(let i = 0; i < numQuestions; i++) {
    template.push(-1);
  }  
  const [answers, setAnswers] = useState(template);

  const createParams = () => {
    let params = [];
    for(let i = 0; i < answers.length; i++) {
      const param = ['q'+i, answers[i]];
      params.push(param);
    }
    return params;
  }

  // checks that all the questions have been answered
  const validateAnswers = () => {
    for(let i = 0; i < answers.length; i++) {
      if(answers[i] == -1) {
        return false;
      }
    }
    return true;
  }

  const onSubmit = async e => {
    if(!validateAnswers()) {
      toggleWarning(true);
      return;
    }
    const params = new URLSearchParams(createParams())
    axios.get('http://localhost:5000/flask/hello', { params }).then(response => {
      console.log("SUCCESS", response)
      setResponse(response)
    }).catch(error => {
      console.log(error)
    })
    setSubmit(true);
    toggleWarning(false);
  }

  const restart = () => {
    toggleQuiz(true);
    toggleWarning(false);
    setSubmit(false);
    setAnswers(template);
  }

  return (
    <div style={{margin: 50}}>
      <h1 style={{textAlign: 'center'}}>
        Welcome to Health Watch
      </h1>

      <h2 style={{padding: 50}}>
        With our help and the use of cutting edge machine learning technology, 
        we can help you determine if you are at risk of heart disease.
      </h2>

      {response.status == 200 && isSubmit ? 
      <h1>{response.data.message}</h1> : null}

      {isSubmit ? 
        <div style={{display: 'flex',  justifyContent:'center', alignItems:'center'}}>
          <Button variant='outlined' size='large' onClick={restart}>Take Quiz Again</Button>
        </div> : null}

      {!isQuizShowing && !isSubmit ? 
        <div style={{display: 'flex',  justifyContent:'center', alignItems:'center'}}>
          <Button variant='outlined' size='large' onClick={() => toggleQuiz(!isQuizShowing)}>Take our Quiz!</Button> 
        </div>: null}

      {isQuizShowing && !isSubmit ? 
        <div>
          <Questions answers={answers} setAnswers={setAnswers}/> 
          {isWarningShowing ? 
          <h3>
            make sure to fill out all the questions!
          </h3> : null}
          <Button variant='outlined' size='large' onClick={onSubmit}>Submit</Button>
        </div>
      : null}

    </div>
  );
};

export default App;
