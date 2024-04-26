
import '../Pages_css/Footer.css';

function Footer() {

  return (
    <div className='Footer'>
      <div className='Cooperation'>
        <div className='Logo_footer'>
          <div className='Logo_company'>
            <img className='Logo_znania' src="src\Images\Logo_znania.png" alt="" onClick={() => window.open("https://знаниевики.рф")}/>
            <img className='Logo_AdOFF' src="src\Images\Logo_AdOFF.png" alt="" onClick={() => window.open("https://github.com/AdequacyOFF")} />
          </div>
          <div className='Logo_product'>
            <img  className='Logo_tea_footer' src="src\Images\Logo_tea_footer.png" alt="" />
          </div>
        </div>
        <div className='Cooperation_text'>
          <a href="https://знаниевики.рф">знаниевики.рф</a>
          <a href="#">adequacyoff-AO@yandex.ru</a>
          <a href="https://github.com/AdequacyOFF">github.com/AdequacyOFF</a>
          <a href="https://t.me/siferony">t.me/siferony</a>
          <a href="https://t.me/SaR1RaS">t.me/SaR1RaS</a>
          <a href="https://t.me/HedoXaker31">t.me/HedoXaker31</a>
          <a href="https://t.me/another_vize">t.me/another_vize</a>
          <a href="https://t.me/Telega_User_1">t.me/Telega_User_1</a>
        </div>
        <div className='emoji'>
          <img src="src\Images\emoji.png" alt="" />
        </div>
      </div>
      <hr className='Strip'></hr>
      <div className='contact_information'>
        <div className='Copyright'>
          <div className='icons_contact'>
            <img src="src\Images\telegram.png" alt="telegram" onClick={() => window.open("https://t.me/siferony")} />
            <img src="src\Images\GitHub.png" alt="GitHub" onClick={() => window.open("https://github.com/AdequacyOFF")}/>
            <img src="src\Images\mail.png" alt="Mail" onClick={() => window.open("https://yandex.ru")}/>
          </div>
          <p>©2024 AdequacyOFF</p>
        </div>
      </div>
    </div>
  )
}

export default Footer
