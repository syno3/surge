import React, { Component, useState, useEffect} from 'react';
import app from './utils/firebase'
import {useAuth} from './context/auth'
import { getFirestore, collection, getDocs, query, where, onSnapshot } from 'firebase/firestore';


const LoadData = () => {
    const [User, setUser] = useState([]);
    const [Loading, setLoading] = useState(false);
    const {currentUser} = useAuth();

    const db = getFirestore(app);
    const userCollection = collection(db, "User");
    const q = query(userCollection, where("userID", "==", currentUser))
    
    getDocs(q).then((snapshot)=>{
        snapshot.docs.forEach((doc)=>{
            setUser({...doc.data(), id: doc.id})
        })
        console.log(User);
    }).catch(err =>{
        console.log(err)
    })

    return (
    <div>
        <h1>we load data </h1>
        <p>{User.userName}</p>
        <p>{User.userEmail}</p>
    </div>
    );
}

export default LoadData;

