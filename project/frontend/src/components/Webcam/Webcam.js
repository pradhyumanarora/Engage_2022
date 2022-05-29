import React, { useState, useEffect } from "react";
import Webcam from "react-webcam";
import "./webcam.css";
// import GetExpression from '../GetExpression';

const WebcamComponent = () => <Webcam />;

const videoConstraints = {
  width: 870,
  height: 470,
  facingMode: "user",
};

export const WebcamCapture = () => {
  // const [image_uri, setImageUri] = useState(null);
  const [image, setImage] = useState("");
  const [link, setLink] = useState("");
  const webcamRef = React.useRef(null);

  const capture = React.useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();

    setImage(imageSrc);
    // GetExpression(imageSrc);
    fetch("http://localhost:8000/image_process/expression", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ image_uri: imageSrc }),
    })
      .then((response) => {
        return response.json();
      })
      .then((res) => {
        fetch("http://localhost:8000/image_process/get-emotion", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ mood: res.mood }),
        })
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            console.log(data);
            setLink(data.YTLINK);
          });
      });
  });

  return {
      link,
    render: (
      <div className="webcam-container">
        <div className="webcam-img">
          {image == "" ? (
            <Webcam
              audio={false}
              // height={1000}
              ref={webcamRef}
              screenshotFormat="image/jpeg"
              // width={1200}
              videoConstraints={videoConstraints}
            />
          ) : (
            <img src={image} />
          )}
        </div>
        <div className="btn-container">
          {image != "" ? (
            <button
              onClick={(e) => {
                e.preventDefault();
                setImage("");
              }}
              className="webcam-btn"
            >
              Retake Image
            </button>
          ) : (
            <button
              onClick={(e) => {
                e.preventDefault();
                // image_uri = capture();
                // setImageUri(capture());
                capture();
                // console.log(image_uri);
              }}
              className="webcam-btn"
            >
              <span className="btn-text">Capture</span>
            </button>
          )}
        </div>
      </div>
    ),
  };
};
