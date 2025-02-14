import React, { useState, useEffect } from "react";
import {
  Modal,
  Box,
  Typography,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  IconButton,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import { URI, get } from "../../webService.js";

///TODO: As soon as the conection with API are done try to better perfome with the desgin for example
// if the status is paid an right icon appears in green, unpaid a wrong icon a red

const PenaltyModal = ({ open, onClose }) => {
  const [penalties, setPenalties] = useState([]);

  const updateBalance = async () => {
    const url = URI + ":8003/penalties/1/";
    const resp = await get(url).catch(() => null);

    if (resp !== undefined) {
      setPenalties([resp]);
    }
  };

  useEffect(() => {
    if (open) {
      updateBalance();
    }
  }, [open]);

  return (
    <Modal open={open} onClose={onClose}>
      <Box
        sx={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 600,
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
          Penalty History
        </Typography>
        <Paper>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>Rental ID</TableCell>
                <TableCell>Days Delayed</TableCell>
                <TableCell>Status</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {penalties.map((penalty) => (
                <TableRow key={penalty.cvid}>
                  <TableCell>{penalty.cvid}</TableCell>
                  <TableCell>{penalty.cvlenid}</TableCell>
                  <TableCell>{penalty.cvdaysdelayed}</TableCell>
                  <TableCell>
                    {penalty.cbpayed === 1 ? "Paid" : "Unpaid"}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </Paper>
      </Box>
    </Modal>
  );
};

export default PenaltyModal;
