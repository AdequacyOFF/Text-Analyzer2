
import '../Pages_css/Header.css';

function Header() {

  return (
    <div className='Head'>
      <img src="src/Images/Logo.png" alt="" className='Logo'/>
        <p className=' navigation txt anable'>ТЕКСТ</p>
        <p className=' navigation doc anable'>ЗАГРУЗИТЬ ДОКУМЕНТ</p>
        <p className=' navigation url anable'>URL</p>
    </div>
  )
}

export default Header
