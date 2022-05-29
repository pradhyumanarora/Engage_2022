import Navbar from "./Navbar/Navbar";
import {WebcamCapture} from "./Webcam/Webcam";
import MusicPlayer from "./Music-Player/MusicPlayer";
import ReactPlayer from 'react-player';
import './homepage.css';
// import Player from "./Player";
// import withAuth from "./withAuth";
// import Sidebar from "./Sidebar/Sidebar";

function Homepage(){
    const {link,render} = WebcamCapture();
    return(
        <>
            {/* <Sidebar/> */}
            <Navbar/>
            {/* <WebcamCapture/> */}
            {render}
            {/* <MusicPlayer/> */}
            {/* <Player/> */}
            {/* <withAuth/> */}
            <div className="R-Player">
                <div className="playlist">YOUR PLAYLIST</div> 
                <div className="player-container">
                    <ReactPlayer controls url = {link}/>
                    {/* <ReactPlayer className = "R-Componet" controls url = "https://www.youtube.com/watch?v=M_Fmvs5CiDo"/> */}
                </div>
            </div>

        </>
    );
}

export default Homepage;