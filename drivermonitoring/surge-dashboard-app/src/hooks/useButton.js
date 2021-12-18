import {useState} from 'react';
import {signinState, signinstateselector} from '../store/globalstate'
import { useRecoilState, useRecoilValue } from 'recoil';


export function useButton(){

    const[signin, setsignin] = useRecoilState(signinState)

    function siwtchtosignup(){
        setsignin(false)
    }

    function switchtosignin(){
        setsignin(true)
    }

    return{signin, switchtosignin, siwtchtosignup}
}

/* hook to change dashboard content */

/* hook to change dashboard content */
