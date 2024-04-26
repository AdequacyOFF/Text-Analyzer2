import { useState } from "react";
import '../Pages_css/Text.css';
import React from "react";



function Text() {

  const [inputValue, setInputValue] = useState("");

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = () => {
    fetch('http://127.0.0.1:8080/text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue }),
    });
  };

  return (
    <div className="section">

      <div>
        <textarea autosize
          className='input_field' //input_field
          placeholder='Начните писать текст...'
          onChange={handleChange}
          style={{ resize: 'none', height: '500px' }}
          
        />
        <button className='Processing_btn' type="button" onClick={handleSubmit}>
          <img src="src/Images/Processing.png" alt="Processing" />
        </button>
      </div>
      {/* <div className='answer-txt'></div> */}
    </div>
    
  );
};

export default Text
