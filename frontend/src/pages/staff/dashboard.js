import AccountBalanceIcon from "@mui/icons-material/AccountBalance";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import ScheduleIcon from "@mui/icons-material/Event";
import {
  Box,
  Button,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
  Typography,
} from "@mui/material";
import React, { useEffect, useState } from "react";
import BalanceModal from "../../components/modal/balance_modal";
import EditModal from "../../components/modal/edit_modal";
import ScheduleModal from "../../components/modal/schedule_modal";
import productsMock from "../../mockData/productData";
import { URI, del, get, patch, post, put } from "../../webService";

const Dashboard = () => {
  const [customers, setCustomers] = useState([]);
  const [products, setProducts] = useState(productsMock);

  const [newCustomer, setNewCustomer] = useState({
    ccname: "",
    ccemail: "",
    cvbalance: "",
  });
  const [newProduct, setNewProduct] = useState({
    ccdescription: "",
    cvamount: "",
    ccproducttype: "",
  });

  const [editCustomer, setEditCustomer] = useState(null);
  const [editProduct, setEditProduct] = useState(null);

  const handleCloseCustomerModal = () => setEditCustomer(null);
  const handleCloseProductModal = () => setEditProduct(null);

  const handleAddCustomer = async () => {
    const id = customers.length + 1;

    const url = URI + "/customers/";
    const resp = await post(url, newCustomer).catch(() => null);

    if (resp !== undefined && resp === "OK") {
      setCustomers([...customers, { cvid: id, ...newCustomer }]);
      setNewCustomer({ ccname: "", ccemail: "", cvbalance: "" });
    }
  };

  const handleAddProduct = async () => {
    const id = products.length + 1;

    const url = URI + "/products";
    const resp = await post(url, newProduct).catch(() => null);

    if (resp !== undefined) {
      setProducts([...products, { cvid: id, ...newProduct }]);
      setNewProduct({ ccdescription: "", cvamount: "", ccproducttype: "" });
    }
  };

  const handleDeleteCustomer = async (customer) => {
    const url = URI + `/customers/${customer.cvid}/`;
    const resp = await del(url, newProduct).catch(() => null);

    if (resp !== undefined) {
      setCustomers(customers.filter((c) => c.cvid !== customer.cvid));
    }
  };

  const handleDeleteProduct = async (product) => {
    const url = URI + `/products/${product.cvid}/`;
    const resp = await del(url, newProduct).catch(() => null);

    if (resp !== undefined) {
      setProducts(products.filter((p) => p.cvid !== product.cvid));
    }
  };

  const handleSaveCustomer = async () => {
    if (editCustomer) {
      const url = URI + `/customers/${editCustomer.cvid}/update/`;
      const resp = await put(url, editCustomer).catch(() => null);

      if (resp !== undefined) {
        setCustomers(
          customers.map((customer) =>
            customer.cvid === editCustomer.cvid ? editCustomer : customer
          )
        );
      }

      setEditCustomer(null);
    }
  };

  const handleSaveProduct = async () => {
    if (editProduct) {
      const url = URI + `/products/${editProduct.cvid}/`;
      const resp = await put(url, editProduct).catch(() => null);

      if (resp !== undefined) {
        setProducts(
          products.map((product) =>
            product.cvid === editProduct.cvid ? editProduct : product
          )
        );
      }
      setEditProduct(null);
    }
  };

  const [scheduleModal, setScheduleModal] = useState(false);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [selectedCustomer, setSelectedCustomer] = useState("");
  const [scheduleData, setScheduleData] = useState({
    cdwithdrawdate: "",
    cdreturndate: "",
    cvvalue: "",
  });

  const handleOpenScheduleModal = (product) => {
    setSelectedProduct(product);
    setScheduleModal(true);
  };

  const handleCloseScheduleModal = () => {
    setSelectedProduct(null);
    setSelectedCustomer("");
    setScheduleData({
      cdwithdrawdate: "",
      cdreturndate: "",
      cvvalue: "",
    });
    setScheduleModal(false);
  };

  const handleSaveSchedule = () => {
    console.log("Agendamento Salvo:", {
      product: selectedProduct,
      customer: selectedCustomer,
      schedule: scheduleData,
    });
    handleCloseScheduleModal();
  };

  const handleUpdateBalance = async (customerId, amount) => {
    const url = URI + `/customers/${customerId}/update/`;
    const resp = await patch(url, { cvbalance: amount }).catch(() => null);

    if (resp !== undefined) {
      setCustomers((prevCustomers) =>
        prevCustomers.map((customer) =>
          customer.cvid === customerId
            ? { ...customer, cvbalance: Number(customer.cvbalance) + Number(amount) }
            : customer
        )
      );
    }
  };

  const fetchCustomers = async () => {
    const url = URI + "/customers/";
    const resp = await get(url).catch(() => null);

    if (resp !== undefined) {
      setCustomers(resp);
    }
  };

  const fetchProducts = async () => {
    const url = URI + "/products";
    const resp = await get(url).catch(() => null);

    if (resp !== undefined) {
      setProducts(resp);
    }
  };

  useEffect(() => {
    fetchCustomers();
    fetchProducts();
  }, []);

  return (
    <Box sx={{ padding: 4 }}>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>

      <Box sx={{ marginBottom: 4 }}>
        <Typography variant="h5" gutterBottom>
          Customers
        </Typography>
        <Box sx={{ display: "flex", gap: 2, marginBottom: 2 }}>
          <TextField
            label="Name"
            value={newCustomer.ccname}
            onChange={(e) =>
              setNewCustomer({ ...newCustomer, ccname: e.target.value })
            }
            variant="outlined"
          />
          <TextField
            label="Email"
            value={newCustomer.ccemail}
            onChange={(e) =>
              setNewCustomer({ ...newCustomer, ccemail: e.target.value })
            }
            variant="outlined"
          />
          <TextField
            label="Balance"
            type="number"
            value={newCustomer.cvbalance}
            onChange={(e) =>
              setNewCustomer({ ...newCustomer, cvbalance: e.target.value })
            }
            variant="outlined"
          />
          <Button
            variant="contained"
            color="primary"
            onClick={handleAddCustomer}
          >
            Add Customer
          </Button>
        </Box>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>Name</TableCell>
                <TableCell>Email</TableCell>
                <TableCell>Balance</TableCell>
                <TableCell>Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {customers.map((customer) => (
                <TableRow key={customer.cvid}>
                  <TableCell>{customer.cvid}</TableCell>
                  <TableCell>{customer.ccname}</TableCell>
                  <TableCell>{customer.ccemail}</TableCell>
                  <TableCell>${customer.cvbalance}</TableCell>
                  <TableCell>
                    <Box sx={{ display: "flex", gap: 1 }}>
                      <Button
                        variant="contained"
                        color="primary"
                        onClick={() => setEditCustomer({ ...customer })}
                        startIcon={<EditIcon />}
                      >
                        {" "}
                        Edit{" "}
                      </Button>
                      <Button
                        variant="contained"
                        color="success"
                        onClick={() => setSelectedCustomer(customer)}
                        startIcon={<AccountBalanceIcon />}
                      >
                        Update Balance
                      </Button>
                      <Button
                        variant="contained"
                        color="secondary"
                        onClick={() => handleDeleteCustomer(customer)}
                        startIcon={<DeleteIcon />}
                      >
                        {" "}
                        Delete{" "}
                      </Button>
                    </Box>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>

      <Box>
        <Typography variant="h5" gutterBottom>
          Products
        </Typography>
        <Box sx={{ display: "flex", gap: 2, marginBottom: 2 }}>
          <TextField
            label="Description"
            value={newProduct.ccdescription}
            onChange={(e) =>
              setNewProduct({ ...newProduct, ccdescription: e.target.value })
            }
            variant="outlined"
          />
          <TextField
            label="Amount"
            type="number"
            value={newProduct.cvamount}
            onChange={(e) =>
              setNewProduct({ ...newProduct, cvamount: e.target.value })
            }
            variant="outlined"
          />
          <TextField
            label="Product Type"
            value={newProduct.ccproducttype}
            onChange={(e) =>
              setNewProduct({ ...newProduct, ccproducttype: e.target.value })
            }
            variant="outlined"
          />
          <Button
            variant="contained"
            color="primary"
            onClick={handleAddProduct}
          >
            Add Product
          </Button>
        </Box>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>Description</TableCell>
                <TableCell>Amount</TableCell>
                <TableCell>Product Type</TableCell>
                <TableCell>Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {products.map((product) => (
                <TableRow key={product.cvid}>
                  <TableCell>{product.cvid}</TableCell>
                  <TableCell>{product.ccdescription}</TableCell>
                  <TableCell>{product.cvamount}</TableCell>
                  <TableCell>{product.ccproducttype}</TableCell>
                  <TableCell>
                    <Box sx={{ display: "flex", gap: 1 }}>
                      {" "}
                      <Button
                        variant="contained"
                        color="primary"
                        onClick={() => setEditProduct({ ...product })}
                        startIcon={<EditIcon />}
                      >
                        {" "}
                        Edit{" "}
                      </Button>
                      <Button
                        variant="contained"
                        color="success"
                        onClick={() => handleOpenScheduleModal(product)}
                        startIcon={<ScheduleIcon />}
                      >
                        Schedule
                      </Button>
                      <Button
                        variant="contained"
                        color="secondary"
                        onClick={() => handleDeleteProduct(product)}
                        startIcon={<DeleteIcon />}
                      >
                        {" "}
                        Delete{" "}
                      </Button>
                    </Box>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>

      <EditModal
        open={!!editCustomer && Object.keys(editCustomer).length > 0}
        onClose={handleCloseCustomerModal}
        onSave={handleSaveCustomer}
        data={editCustomer}
        setData={setEditCustomer}
        fields={[
          { key: "ccname", label: "Name" },
          { key: "ccemail", label: "Email" },
          { key: "cvbalance", label: "Balance", type: "number" },
        ]}
      />

      <EditModal
        open={!!editProduct && Object.keys(editProduct).length > 0}
        onClose={handleCloseProductModal}
        onSave={handleSaveProduct}
        data={editProduct}
        setData={setEditProduct}
        fields={[
          { key: "ccdescription", label: "Description" },
          { key: "cvamount", label: "Amount", type: "number" },
          { key: "ccproducttype", label: "Product Type" },
        ]}
      />
      <ScheduleModal
        open={scheduleModal}
        onClose={handleCloseScheduleModal}
        onSave={handleSaveSchedule}
        customers={customers}
        selectedCustomer={selectedCustomer}
        setSelectedCustomer={setSelectedCustomer}
        scheduleData={scheduleData}
        setScheduleData={setScheduleData}
      />

      {selectedCustomer && (
        <BalanceModal
          open={!!selectedCustomer}
          onClose={() => setSelectedCustomer(null)}
          customer={selectedCustomer}
          onSave={handleUpdateBalance}
        />
      )}
    </Box>
  );
};

export default Dashboard;
