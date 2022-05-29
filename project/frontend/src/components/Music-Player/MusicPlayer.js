import React from "react";
import './musicplayer.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { solid } from '@fortawesome/fontawesome-svg-core/import.macro' // <-- import styles to be used

const MusicPlayer = () => {
    return (
        <>
            <div className="music-player">
                <div className="music-box">
                    <div className="music-text">
                        <h3 className="music-name">
                            Fursat
                        </h3>
                        <h4 className="music-writer">
                            Arjun Kanungo
                        </h4>

                    </div>
                    <div className="music-buttons">
                        <div className="btn-back">
                            <FontAwesomeIcon icon={solid('backward')} />
                        </div>

                        <div className="btn-play">
                            <FontAwesomeIcon icon={solid('play')} />
                        </div>
                        <div className="btn-next">
                            <FontAwesomeIcon icon={solid('forward')} />
                        </div>
                    </div>
                </div>
            </div>

        </>
    );
};

export default MusicPlayer;