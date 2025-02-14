import React, { useEffect, useState } from "react";
import {
  Navigate,
  Route,
  BrowserRouter as Router,
  Routes,
} from "react-router-dom";
import Header from "./components/header/header";
import LoginModal from "./components/modal/login_modal";
import Home from "./pages/home";
import Dashboard from "./pages/staff/dashboard";
import { URI } from "./webService";

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userType, setUserType] = useState(null);
  const [isModalVisible, setIsModalVisible] = useState(false);

  useEffect(() => {
    const savedIsLoggedIn = localStorage.getItem("isLoggedIn") === "true";
    const savedUserType = localStorage.getItem("userType");
    setIsLoggedIn(savedIsLoggedIn);
    setUserType(savedUserType);
  }, []);

  const handleResponse = (response) => {
    if (response == null || !response.statusText === "OK") {
      return false;
    }

    return response.json();
  };

  const handleLogin = async ({ userType, password, username }) => {
    setUserType(userType);

    if (password === "") {
      setIsLoggedIn(false);
    } else {
      const url = URI + "/users/user-token";

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: username,
          password: password,
        }),
      };

      const resp = await fetch(url, requestOptions).catch(() => null);

      const user = await handleResponse(resp);

      if (user) {
        setIsLoggedIn(true);
        localStorage.setItem("isLoggedIn", "true");
        localStorage.setItem("userType", userType);
        sessionStorage.setItem("user", user.token);
      }
    }
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    setUserType(null);
    localStorage.removeItem("isLoggedIn");
    localStorage.removeItem("userType");
  };

  return (
    <Router>
      <Header
        onLoginClick={() => setIsModalVisible(true)}
        isLoggedIn={isLoggedIn}
        onLogoutClick={handleLogout}
        userType={userType}
      />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/staff/dashboard"
          element={
            isLoggedIn && userType === "staff" ? (
              <Dashboard />
            ) : (
              <Navigate to="/" />
            )
          }
        />
        <Route
          path="/customer/home"
          element={
            isLoggedIn && userType === "customer" ? (
              <Home />
            ) : (
              <Navigate to="/" />
            )
          }
        />
      </Routes>
      <LoginModal
        isVisible={isModalVisible}
        onClose={() => setIsModalVisible(false)}
        onLogin={handleLogin}
      />
    </Router>
  );
};

export default App;
