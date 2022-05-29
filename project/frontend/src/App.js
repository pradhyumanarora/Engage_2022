import logo from './logo.svg';
import './App.css';
import Login from './components/Login'
import Homepage from './components/Homepage'
import LandingPage from './components/LandingPage/LandingPage'
import axios from 'axios';

function App() {
  function getData() {
    
    fetch("/auth",
    {
      mode: "no-cors", 
    })
    .then(res => res.json())
    .then((data) => {
      console.log(data);
    })
    // axios({
    //   method: "GET",
    //   url:"/auth",
    //   mode: "no-cors",
    //   headers: {
    //     "Content-Type": "application/json",
    //     "Access-Control-Allow-Origin": "*",

    // }
    // })
    // .then(console.log("Hello"))
  }

  return(
    <>
    {/* getData() */}
    <LandingPage path= "/homepage" render={Homepage}/>
    </>
  )
}

export default App;
