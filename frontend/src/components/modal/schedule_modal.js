import React from "react";
import {
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Button,
  TextField,
  Autocomplete,
} from "@mui/material";

const ScheduleModal = ({
  open,
  onClose,
  onSave,
  customers,
  selectedCustomer,
  setSelectedCustomer,
  scheduleData,
  setScheduleData,
}) => {
  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Schedule Product</DialogTitle>
      <DialogContent>
        <Autocomplete
          options={customers}
          getOptionLabel={(option) => option.ccname}
          value={customers.find((customer) => customer.cvid === selectedCustomer) || null}
          onChange={(e, newValue) => {
            if (newValue) {
              setSelectedCustomer(newValue.cvid);
            } else {
              setSelectedCustomer("");
            }
          }}
          renderInput={(params) => (
            <TextField {...params} label="Select a Customer" variant="outlined" fullWidth />
          )}
          isOptionEqualToValue={(option, value) => option.cvid === value.cvid}
        />
        <TextField
          label="Withdraw Date"
          type="date"
          value={scheduleData.cdwithdrawdate}
          onChange={(e) =>
            setScheduleData({
              ...scheduleData,
              cdwithdrawdate: e.target.value,
            })
          }
          fullWidth
          margin="normal"
          InputLabelProps={{ shrink: true }}
        />
        <TextField
          label="Return Date"
          type="date"
          value={scheduleData.cdreturndate}
          onChange={(e) =>
            setScheduleData({
              ...scheduleData,
              cdreturndate: e.target.value,
            })
          }
          fullWidth
          margin="normal"
          InputLabelProps={{ shrink: true }}
        />
        <TextField
          label="Value"
          type="number"
          value={scheduleData.cvvalue}
          onChange={(e) =>
            setScheduleData({ ...scheduleData, cvvalue: e.target.value })
          }
          fullWidth
          margin="normal"
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={onSave} variant="contained" color="primary">
          Save
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default ScheduleModal;
