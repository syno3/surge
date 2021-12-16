import { useEffect, useState, createContext, useContext } from "react";
import app from '../utils/firebase'
import {createUserWithEmailAndPassword} from 'firebase/auth'


export const AuthContext = createContext({
    currentUser: null,
    register: ()=>Promise,
});

export const useAuth = () => useContext(AuthContext)

export default function AuthContextprovider({children}){
    /* we need to change the current user details */

    const [currentUser, setCurrentUser] = useState(null)

    /* function to register user to firebase */
    function register(email, password){
        return createUserWithEmailAndPassword(app, email, password)
    }

    const value={
        currentUser,
        register
    }

    return <AuthContext.Provider value={value}>
        {children}
    </AuthContext.Provider>
}

