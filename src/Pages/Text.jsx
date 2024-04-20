import '../Pages_css/Text.css';


function Text() {

  return (
    <div className='section'>
      <div className='input_field'>
        
      </div>
      <div className='answer-txt'>

      </div>
      <form action="/Document">
        <button className='btn-doc-txt btn-doc-text-txt'>ЗАГРУЗИТЬ ДОКУМЕНТ</button>
      </form>
      <form action="/Url">
        <button className='btn-url-txt btn-url-text-txt'>URL</button>
      </form>
    </div>
  )
}

export default Text
