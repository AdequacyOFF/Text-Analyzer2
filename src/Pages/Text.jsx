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
    <section>

      <div>
        <textarea autosize
          className='text_input' //input_field
          placeholder='Начните писать текст...'
          style={{ resize: 'none'}}
          onChange={handleChange}
        />
        <button className='search_btn' type="button" onClick={handleSubmit}>
          <img src="src\Images\search.png" alt="" />
        </button>
      </div>
      {/* <div className='answer-txt'></div> */}
    </section>
    
  );
};

export default Text
