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
// if the status is returned an right icon appears in green, Pending an icon with a yellow color

const mockRentals = [
  {
    cvid: 1,
    cdwithdrawdate: "2024-12-01 10:00",
    cdreturndate: "2024-12-05 10:00",
    cbreturned: 1,
    cvvalue: 25.5,
  },
  {
    cvid: 2,
    cdwithdrawdate: "2024-11-20 14:00",
    cdreturndate: "2024-11-27 14:00",
    cbreturned: 0,
    cvvalue: 30.0,
  },
];

const RentalModal = ({ open, onClose }) => {
  const [rentals, setRentals] = useState([]);

  const updateBalance = async () => {
    const url = URI + ":8001/rentals/1/";
    const resp = await get(url).catch(() => null);

    if (resp !== undefined) {
      setRentals([resp]);
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
          Rental History
        </Typography>
        <Paper>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>Withdraw Date</TableCell>
                <TableCell>Return Date</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Value</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {mockRentals.map((rental) => (
                <TableRow key={rental.cvid}>
                  <TableCell>{rental.cvid}</TableCell>
                  <TableCell>{rental.cdwithdrawdate}</TableCell>
                  <TableCell>{rental.cdreturndate}</TableCell>
                  <TableCell>
                    {rental.cbreturned === 1 ? "Returned" : "Pending"}
                  </TableCell>
                  <TableCell>${rental.cvvalue.toFixed(2)}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </Paper>
      </Box>
    </Modal>
  );
};

export default RentalModal;
