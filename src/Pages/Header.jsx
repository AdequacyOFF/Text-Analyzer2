
import '../Pages_css/Header.css';

function Header() {

  return (
    <div className='Head'>
      <img src="src/Images/Logo.png" alt="" className='Logo'/>
        {/* <p className=' navigation txt anable'>ТЕКСТ</p>
        <p className=' navigation doc anable'>ЗАГРУЗИТЬ ДОКУМЕНТ</p>
        <p className=' navigation url anable'>URL</p> */}
      {/* <form action="/Text">
        <button className='navigation txt anable'>ТЕКСТ</button>
      </form>
      <form action="/Document">
        <button className='navigation doc anable'>ЗАГРУЗИТЬ ДОКУМЕНТ</button>
      </form><form action="/Url">
        <button className='navigation url anable'>URL</button>
      </form> */}
      <nav>
        <ul>
          <li className='navigation txt anable'><a href='/Text'>ТЕКСТ</a></li>
          <li className='navigation doc anable'><a href='/Document'>ЗАГРУЗИТЬ ДОКУМЕНТ</a></li>
          <li className='navigation url anable'><a href='/Url'>URL</a></li>
        </ul>
      </nav>
    </div>
  )
}

export default Header
