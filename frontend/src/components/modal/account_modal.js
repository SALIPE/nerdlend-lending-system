import React, { useState, useEffect } from "react";
import { Modal, Box, Typography, Button, IconButton } from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import PenaltyModal from "./penalty_modal";
import RentalModal from "./rental_modal";
import { URI, get } from "../../webService.js";

const AccountModal = ({ open, onClose }) => {
  const [penaltiesModal, setPenaltiesModal] = useState(false);
  const [rentalsModal, setRentalsModal] = useState(false);
  const [balance, setBalance] = useState(0);

  const formattedBalance = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  }).format(balance);

  const updateBalance = async () => {
    const url = URI + ":8003/customers/1/";
    const resp = await get(url).catch(() => null);

    if (resp && resp.cvbalance !== undefined) {
      const newBalance = resp.cvbalance;

      // Only update the state if the balance has changed
      if (newBalance !== balance) {
        setBalance(newBalance);
      }
    }
  };

  useEffect(() => {
    if (open) {
      updateBalance();
    }
  }, [open]);

  return (
    <>
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
            My Account
          </Typography>
          <Typography variant="h6" gutterBottom>
            Balance: {formattedBalance}
          </Typography>
          <Button
            variant="contained"
            color="secondary"
            sx={{ marginRight: 2, marginTop: 2 }}
            onClick={() => setPenaltiesModal(true)}
          >
            View Penalty History
          </Button>
          <Button
            variant="contained"
            color="primary"
            sx={{ marginTop: 2 }}
            onClick={() => setRentalsModal(true)}
          >
            View Rental History
          </Button>
        </Box>
      </Modal>
      <PenaltyModal
        open={penaltiesModal}
        onClose={() => setPenaltiesModal(false)}
      />
      <RentalModal open={rentalsModal} onClose={() => setRentalsModal(false)} />
    </>
  );
};

export default AccountModal;
