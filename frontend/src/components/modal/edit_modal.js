import React from "react";
import {
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Button,
  TextField,
} from "@mui/material";

const EditModal = ({ open, onClose, onSave, data = {}, setData, fields }) => {
  if (!data) {
    console.error("EditModal: `data` is null or undefined");
    return null;
  }

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Edit Item</DialogTitle>
      <DialogContent>
        {fields.map((field) => (
          <TextField
            key={field.key}
            label={field.label}
            type={field.type || "text"}
            value={data[field.key] || ""}
            onChange={(e) => setData({ ...data, [field.key]: e.target.value })}
            fullWidth
            margin="normal"
          />
        ))}
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

export default EditModal