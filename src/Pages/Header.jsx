import { Link } from 'react-router-dom';
import '../Pages_css/Header.css';

function Header() {

  return (
    <div className='Head'>
      <img src="src/Images/Logo.png" alt="" className='Logo'/>
      <nav>
        <ul>
          <li className='navigation txt anable'><Link to='/'>ТЕКСТ</Link></li>
          <li className='navigation doc anable'><Link to='/Document'>ЗАГРУЗИТЬ ДОКУМЕНТ</Link></li>
          <li className='navigation url anable'><Link to='/Url'>URL</Link></li>
        </ul>
      </nav>
    </div>
  )
}

export default Header
