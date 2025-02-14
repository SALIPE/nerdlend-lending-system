import React, { useState } from "react";
import {
  Modal,
  Box,
  Typography,
  TextField,
  Button,
  IconButton,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";

const BalanceModal = ({ open, onClose, customer, onSave }) => {
  const [balance, setBalance] = useState("");

  const handleSave = () => {
    onSave(customer.cvid, parseFloat(balance));
    setBalance("");
    onClose();
  };

  return (
    <Modal open={open} onClose={onClose}>
      <Box
        sx={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 400,
          bgcolor: "background.paper",
          border: "2px solid #000",
          boxShadow: 24,
          p: 4,
          borderRadius: 2,
        }}
      >
        <IconButton
          onClick={onClose}
          sx={{ position: "absolute", top: 8, right: 8 }}
        >
          <CloseIcon />
        </IconButton>

        <Typography variant="h5" gutterBottom>
          Update Balance
        </Typography>
        <Typography variant="body1" gutterBottom>
          Customer: {customer?.ccname}
        </Typography>
        <TextField
          label="Amount"
          type="number"
          fullWidth
          variant="outlined"
          value={balance}
          onChange={(e) => setBalance(e.target.value)}
          sx={{ marginBottom: 2 }}
        />
        <Button
          variant="contained"
          color="primary"
          fullWidth
          onClick={handleSave}
        >
          Update Balance
        </Button>
      </Box>
    </Modal>
  );
};

export default BalanceModal;
