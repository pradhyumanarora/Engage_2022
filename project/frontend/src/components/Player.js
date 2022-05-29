import React, { Component } from "react";
// import {
//   Grid,
//   Typography,
//   Card,
//   IconButton,
//   LinearProgress,
// } from "@material-ui/core";
// import PlayArrowIcon from "@material-ui/icons/PlayArrow";
// import PauseIcon from "@material-ui/icons/Pause";
// import SkipNextIcon from "@material-ui/icons/SkipNext";

export default function Player() {


    // fetch("/spotify/current-song")
    //   .then((response) => {
    //     if (!response.ok) {
    //       return {};
    //     } else {
    //       return response.json();
    //     }
    //   })
    //   .then((data) => {
    //     this.setState({ song: data });
    //     console.log(data);
    //   });

      fetch('http://localhost:8000/spotify/current-song')
      .then((response) => response.json())
        // if (!response.ok) {
        //       return {};
        //     } else {
        //       return response.json();
        //     }
        //   return response.json();})
      .then((data) => {
          console.log(data);
        });
    // const songProgress = (data.time / data.duration) * 100;

    // return (
    //   <Card>
    //     <Grid container alignItems="center">
    //       <Grid item align="center" xs={4}>
    //         <img src={data.image_url} height="100%" width="100%" />
    //       </Grid>
    //       <Grid item align="center" xs={8}>
    //         <Typography component="h5" variant="h5">
    //           {data.title}
    //         </Typography>
    //         <Typography color="textSecondary" variant="subtitle1">
    //           {data.artist}
    //         </Typography>
    //         <div>
    //           <IconButton>
    //             {data.is_playing ? <PauseIcon /> : <PlayArrowIcon />}
    //           </IconButton>
    //           <IconButton>
    //             <SkipNextIcon />
    //           </IconButton>
    //         </div>
    //       </Grid>
    //     </Grid>
    //     <LinearProgress variant="determinate" value={songProgress} />
    //   </Card>
    // );

}

