import React, { useState } from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

const RadioQuestion = (props) => {
  const question = props.question;
  const choices = props.choices;
  const index = props.index;
  const [value, setValue] = useState("");

  const handleChange = (event) => {
    setValue(event.target.value);
    let items = [...props.answers];
    items[index] = event.target.value;
    props.setAnswers(items);
  };

  return (
    <div style={{padding: 10}}>
      <FormControl>
        <FormLabel id="radio-buttons-group">{question}</FormLabel>
        <RadioGroup
          aria-labelledby="radio-buttons-group"
          value={value}
          onChange={handleChange}
        >
          {choices.map((choice, index) => (
            <FormControlLabel key={index} value={index} control={<Radio />} label={choice} />
          ))}
        </RadioGroup>
      </FormControl>
    </div>
  );
};

export default RadioQuestion;
