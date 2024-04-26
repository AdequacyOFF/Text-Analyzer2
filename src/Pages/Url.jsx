import { useState } from "react";
import '../Pages_css/Url.css';
import OutPutText from "./OutPutText";


function Url() {

  const DataText = [['Десять лет назад, в середине 2000-х годов, в машинном обучении началась революция В 2005-2006 годах группы исследователей под руководством Джеффри Хинтона (Geoffrey Hinton) в университете Торонто и Йошуа Бенджи (Yoshua Bengio) в университете Монреаля научились обучать глубокие нейронные сети ', 'neutral', 99.97, 0.01, 0.01, 0.01, 0.0, 0.01],

  ['Сегодня был ужасный день С утра я проснулась от того, что опоздала на работу ', 'sadness', 0.03, 0.05, 99.68, 0.03, 0.14, 0.07],

  ['Вы чувствуете, как по спине пробегает холодок страха Вы убегаете от кого-то или чего-то, кто преследует вас ', 'fear', 29.5, 0.8, 0.29, 0.59, 68.49, 0.33],

  ['Я засыпаю с чувством благодарности за все хорошее, что произошло в этот день Я благодарен за свою семью, друзей, здоровье и все те возможности, которые мне дарит жизнь ', 'joy', 0.03, 99.87, 0.04, 0.02, 0.01, 0.03]



]
  

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
          <OutPutText data = {DataText}/>
        </div>
      </div>
    </div>
    
  );
};

export default Url;
