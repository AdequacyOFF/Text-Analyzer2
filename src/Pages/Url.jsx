
import '../Pages_css/Url.css';

function Url() {

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

      </div>
      
    </div>
  )
}

export default Url
