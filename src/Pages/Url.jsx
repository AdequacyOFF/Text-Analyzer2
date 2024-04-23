import { useState } from "react";
import '../Pages_css/Url.css';

function Url() {

  const [inputValue, setInputValue] = useState("");

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = () => {
    fetch('http://127.0.0.1:8080/url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue }),
    });
  };

  return (

    <div className='section'>
      <div >
        <input type="text" className='input_field' placeholder='Введите ссылку на источник(URL)...'/>
        <button className='search_btn'
          type="button"
          onClick={() => {
            inputElement.addEventListener('input', (event) => {
              
              const inputValue = event.target.value;
              fetch('http://127.0.0.1:8080/url', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({ inputValue }),
              });
            });
          }}>
            <img src="src\Images\search.png" alt="" />
        </button>
      </div>
      <div className='answer-txt'>

    <div className="section">


      <div>
        <input type="text" className='input_field' placeholder='Введите ссылку на источник(URL)...' onChange={handleChange} />
        <button className='search_btn' type="button" onClick={handleSubmit}>
          <img src="src\Images\search.png" alt="" />
        </button>
      </div>
      <div className='answer-txt'></div>
    </div>
    
  );
};

export default Url;
