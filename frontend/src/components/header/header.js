import React, { useState } from "react";
import { AppBar, Toolbar, Typography, Button, Box } from "@mui/material";
import AccountModal from "../modal/account_modal";
import { Link } from "react-router-dom";

const Header = ({ onLoginClick, isLoggedIn, onLogoutClick, userType }) => {
  const [accountModalOpen, setAccountModalOpen] = useState(false);

  return (
    <AppBar position="static" color="primary">
      <Toolbar>
        <Typography
          variant="h5"
          sx={{ flexGrow: 1 }}
          component={Link}
          to="/"
          style={{ textDecoration: "none", color: "inherit" }}
        >
          NerdLend
        </Typography>
        <Box>
          {!isLoggedIn ? (
            <Button color="inherit" onClick={onLoginClick}>
              Login
            </Button>
          ) : (
            <>
              {userType === "staff" && (
                <Button
                  color="inherit"
                  component={Link}
                  to="/staff/dashboard"
                >
                  Staff Dashboard
                </Button>
              )}
              {userType === "customer" && (
                <>
                  <Button
                    color="inherit"
                    component={Link}
                    to="/customer/home"
                    sx={{ marginRight: 1 }}
                  >
                    Home
                  </Button>
                  <Button
                    color="inherit"
                    onClick={() => setAccountModalOpen(true)}
                    sx={{ marginRight: 1 }}
                  >
                    Account
                  </Button>
                </>
              )}
              <Button color="inherit" onClick={onLogoutClick}>
                Logout
              </Button>
            </>
          )}
        </Box>
      </Toolbar>
      {userType === "customer" && (
        <AccountModal
          open={accountModalOpen}
          onClose={() => setAccountModalOpen(false)}
        />
      )}
    </AppBar>
  );
};

export default Header;
