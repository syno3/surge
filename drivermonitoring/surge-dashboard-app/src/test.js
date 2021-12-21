import React, { Component, useState, useEffect} from 'react';
import app from './utils/firebase'
import { getFirestore, collection, getDocs, query } from 'firebase/firestore/lite';


const LoadData = () => {
    const [User, setUser] = useState([]);
    const [Loading, setLoading] = useState(true);

    const db = getFirestore(app);
    const data = collection(db, "user");

    return (
    <div>
        <h1>we load data </h1>
    </div>
    );
}

export default LoadData;

