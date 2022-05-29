import React from "react";
import Button from "@mui/material/Button";

export default function Login() {
  const authenticateSpotify = () => {
    fetch("http://localhost:8000/spotify/is-authenticated")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (!data.isAuthenticated) {
          fetch("http://localhost:8000/spotify/get-auth-url")
            .then((response) => response.json())
            .then((data) => {
              window.location.replace(data.url);
            });
        }
      });
  };
  return (
    <div>
      <h1>Hello</h1>
      <Button
        variant="contained"
        onClick={authenticateSpotify}
        // (e)=>{
        // e.preventDefault();
        // authenticateSpotify();}}
      >
        Hello World
      </Button>
    </div>
  );
}
