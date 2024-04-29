import { useState } from "react";
import '../Pages_css/Url.css';
import OutPutText from "./OutPutText";


function Url() {

  
  

  const [inputValue, setInputValue] = useState("");

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = () => {
    fetch('http://127.0.0.1:8080/url', {
      method: 'POST',
      headers: {
        'Content-Type': 'text/html; charset=utf',
      },
      body: inputValue,
    });
  };

  return (
    <div className="section">


      <div>
        <input type="text" className='input_field' placeholder='Введите ссылку на источник(URL)...' onChange={handleChange} />
        <button className='search_btn' type="button" onClick={handleSubmit}>
          <img src="src\Images\search.png" alt="" />
        </button>
      </div>
      <div className='answer-url'>
        <div className='answer-url-frame'>
          {/* <OutPutText /> */}
        </div>
      </div>  
    </div>
    
  );
};

export default Url;
