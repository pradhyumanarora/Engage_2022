import Cookies from "js-cookie";
// import { useRouter } from "next/router";
import axios from "axios";
import { useEffect, useState } from "react";
// import Loader from "./loader.jsx";
// import Navbar from "./navbar.jsx";
// import Telegram from "./telegram.jsx";
const withAuth = (WrappedComponent) => {
  return (props) => {
    // const Router = useRouter();
    const [verified, setVerified] = useState(false);
    const [loader, setloader] = useState(true);
    useEffect(() =>
    async () => {
      var config = {
        method: "get",
        url: "http://localhost:8000/is-authenticated",
        withCredentials: true,
      };
      axios(config)
        .then(function (response) {
          if (response.data.isAuthenticated) {
            setVerified(true);
          } else {
            // Router.replace("http://localhost:3000");
            console.log("not authenticated");
          }
          setloader(false);
        })
        .catch(function (error) {});
    }, []);

    if (loader) {
      return <>Loaded</>;
    } else {
      if (verified) {
        return (
          <>
            You Are Verified
          </>
        );
      } else {
        return null;
      }
    }
  };
};

export default withAuth;
