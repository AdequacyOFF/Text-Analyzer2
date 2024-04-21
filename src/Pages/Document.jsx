
import '../Pages_css/Document.css';
import DropFileInput from './DropFileInput';

function Document() {

  const onFileChange = (files) => {
    console.log(files);
}

  return (
    <div className='section'>
      <div className='answer-doc'>

      </div>
      <div className='DropFileInput'>
          <DropFileInput onFileChange={(files) => onFileChange(files)}/>
      </div>
      <form action="/">
        <button className='btn-doc-doc btn-doc-text-doc'>ТЕКСТ</button>
      </form>
      <form action="/Url">
        <button className='btn-url-doc btn-url-text-doc'>URL</button>
      </form>
    </div>
  )
}

export default Document
