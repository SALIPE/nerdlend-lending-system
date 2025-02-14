import React from "react";
import styles from "./itemCard.module.css";

const ItemCard = ({ item }) => (
  <div className={styles.card}>
    <h3>{item.ccdescription}</h3>
    <p><strong>Type:</strong> {item.ccproducttype}</p>
    <p><strong>Amount:</strong> {item.cvamount}</p>
  </div>
);

export default ItemCard;
