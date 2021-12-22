import React, { useState } from 'react';
import avatar from '../resources/avatar.png';
import {useAuth} from '../../../context/auth';
import app from '../../../utils/firebase';
import { getFirestore, collection, getDocs, query, where } from 'firebase/firestore';



const TopBar = ({page}) => {
    const {currentUser} = useAuth();
    const [User, setUser] = useState([]);
    const [Loading, setLoading] = useState(false);

    const db = getFirestore(app);
    const userCollection = collection(db, "User");
    const q = query(userCollection, where("userID", "==", currentUser))

    getDocs(q).then((snapshot)=>{
        setLoading(true);
        snapshot.docs.forEach((doc)=>{
            setUser({...doc.data(), id: doc.id})
        })
        console.log(User);
    }).catch(err =>{
        console.log(err)
    }).finally(() => setLoading(false))

    return (
        <div className='topbar'>

            <div className='topbar-text'>
                <h1>{page}</h1>
            </div>

            <div className='topbar-icons'>

                <div className='topbar-name-avatar'>
                    <h1 className='topbar-name'>{User.userName}</h1>
                    <img src={avatar}/>
                </div>

            </div>
        </div>
        );
}
export default TopBar;

