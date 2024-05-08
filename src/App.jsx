import {Route, Routes} from "react-router-dom"
import './App.css'
import Document from './Pages/Document.jsx'
import Footer from './Pages/Footer.jsx'
import Header from './Pages/Header.jsx'
import Url from './Pages/Url.jsx'
import Text from './Pages/Text.jsx'

function App() {
  return (
  <div className='wrapper'>
    <header className='header'><Header></Header></header>
    <main className='main'>
            <Routes>
                <Route path="/" element={<Text />} />
                <Route path="/Document" element={<Document />} />
                <Route path="/Url" element={<Url />} />
            </Routes>
    </main>
    <footer className='footer'>
        <Footer>
        </Footer>
      </footer>
  </div>
  )
}

export default App
