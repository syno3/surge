import { useEffect, useState, createContext, useContext } from "react";
import app from '../utils/firebase'
import { getAuth, onAuthStateChanged, signOut, GoogleAuthProvider, signInWithPopup } from "firebase/auth";


export const AuthContext = createContext({
    currentUser: null,
});

export const useAuth = () => useContext(AuthContext)

export default function AuthContextprovider({children}){
    /* we need to change the current user details */

    const [currentUser, setCurrentUser] = useState(null)
    const auth = getAuth();

    /* updating the display name (currentUser) */
    useEffect(() => {
        onAuthStateChanged(auth, (user) => {
            setCurrentUser(user ? user.uid : "empty")
        });
        }, []);

    /* logout user */
    function Logout(){
        return signOut(auth)
    }
    /* signin with google account */
    function signInWithGoogle() {
        const provider = new GoogleAuthProvider()
        return signInWithPopup(auth, provider)
    }    

    const value={
        currentUser,
        Logout,
        signInWithGoogle
    }

    return <AuthContext.Provider value={value}>
        {children}
    </AuthContext.Provider>
}

