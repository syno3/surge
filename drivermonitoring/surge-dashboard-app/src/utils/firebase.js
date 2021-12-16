import * as firebase from "firebase/app";
import "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyBBSwgtkSYjroM7UhvzkuNCZGrgNSsKEVE",
    authDomain: "surge-driverx.firebaseapp.com",
    projectId: "surge-driverx",
    storageBucket: "surge-driverx.appspot.com",
    messagingSenderId: "595066205210",
    appId: "1:595066205210:web:8f5f4477ba33003a224da3",
    measurementId: "G-BS0ER4JFBN"
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);
export default app;