import { TextField } from "@mui/material";
import Grid2 from "@mui/material/Grid2";
import React, { useEffect, useState } from "react";
import ItemCard from "../components/itemCard/itemCard";
import { URI, get } from "../webService";

const Home = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    const url = URI + "/products/allproducts/";
    const resp = await get(url).catch(() => null);

    if (resp !== undefined) {
      const filteredProducts = resp.filter((product) =>
        product.ccdescription.toLowerCase().includes(searchTerm.toLowerCase())
      );
      setProducts(filteredProducts);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const filteredProducts = products.filter((product) =>
    product.ccdescription.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div
      style={{
        padding: "2rem",
        backgroundColor: "#f5f5f5",
        minHeight: "100vh",
      }}
    >
      <h2 style={{ fontSize: "2rem", color: "#333" }}>Available Items</h2>

      <TextField
        label="Search Products"
        variant="outlined"
        fullWidth
        style={{ margin: "1rem 0" }}
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />

      <Grid2 container spacing={3} style={{ marginTop: "2rem" }}>
        {filteredProducts.length > 0 ? (
          filteredProducts.map((item) => (
            <Grid2 item xs={12} sm={6} md={4} lg={3} key={item.cvid}>
              <ItemCard item={item} />
            </Grid2>
          ))
        ) : (
          <p style={{ fontSize: "1.2rem", color: "#777" }}>No items found.</p>
        )}
      </Grid2>
    </div>
  );
};

export default Home;
