import React, { useState } from "react";
import { Dialog, DialogActions, DialogContent, DialogTitle, Button, TextField, Select, MenuItem } from "@mui/material";

const LoginModal = ({ isVisible, onClose, onLogin }) => {
  const [userType, setUserType] = useState("customer");
  const [username, setEmail] = useState("a61491@alunos.ipb.pt");
  const [password, setPassword] = useState("senha");

  const handleLogin = () => {
    onLogin({ userType, password, username });
    onClose();
  };

  return (
    <Dialog open={isVisible} onClose={onClose}>
      <DialogTitle>Login</DialogTitle>
      <DialogContent>
        <Select
          value={userType}
          onChange={(e) => setUserType(e.target.value)}
          fullWidth
          sx={{ marginBottom: 2 }}
        >
          <MenuItem value="customer">Customer</MenuItem>
          <MenuItem value="staff">Staff</MenuItem>
        </Select>
        <TextField
          label="Email"
          type="email"
          value={username}
          onChange={(e) => setEmail(e.target.value)}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          fullWidth
          margin="normal"
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={handleLogin} variant="contained" color="primary">
          Login
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default LoginModal;
