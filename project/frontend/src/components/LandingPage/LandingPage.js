import React from 'react'
import './landingpage.css'
import BackgroundImage from '../assets/images/bg.png'

export default function LandingPage() {

    const authenticateSpotify = () => {
        fetch("http://127.0.0.1:8081/auth")
          .then((res) => res.json())
          .then((data) => {
              console.log(data);
                  window.location.replace(data.url);
                });
        // fetch("http://127.0.0.1:8081/callback/")
        // .then((res) => res.json())
        // .then((data) => {
        //     console.log(data);
        //         // window.location.replace(data.url);
        //       });
            }
    
    return (
        <header style={ HeaderStyle }>
            <h1 className="main-title text-center">Welcome To Music Recommendation Application</h1>
            <p className="main-para text-center">join us now and feel every beat!</p>
            <div className="buttons text-center">

                    <button className="primary-button" onClick={
                        authenticateSpotify
                    }>log in</button>
                {/* <Link to="/register">
                    <button className="primary-button" id="reg_btn"><span>register </span></button>
                </Link> */}
            </div>
        </header>
    )
}

const HeaderStyle = {
    width: "100%",
    height: "100vh",
    background: `url(${BackgroundImage})`,
    backgroundPosition: "center",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover"
}