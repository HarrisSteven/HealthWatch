import React from 'react';
import TextField from '@mui/material/TextField';
import FormLabel from '@mui/material/FormLabel';

const ValueQuestion = (props) => {
  const question = props.question;
  const index = props.index;
  const maxValue = props.max;
  const [value, setValue] = React.useState("");

  const handleChange = (event) => {
    let newValue = event.target.value;
    if(newValue > maxValue) {
      newValue = maxValue;
    }
    if(newValue < 0) {
      newValue = 0;
    }
    setValue(newValue);
    let items = [...props.answers];
    items[index] = newValue;
    props.setAnswers(items);
  };

  return (
    <div style={{padding: 10}}>
      <FormLabel>{question}</FormLabel>
      <br></br>
      <TextField value={value} onChange={handleChange} variant="outlined" />
    </div>
  );
};

export default ValueQuestion;
