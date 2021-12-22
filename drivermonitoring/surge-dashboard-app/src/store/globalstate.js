import { atom, selector } from 'recoil';


/* gloabal state for login (signin// signup form) */
export const signinState = atom({
    key: 'signinState', 
    default: true,
});

export const signinstateselector = selector({
    key: 'signinstateselector',
    get: ({get})=>{
        const value = get(signinState)
        return value
    }

})
/* gloabal state for login (signin// signup form) */


/* global state for dashboard login */
export const dashboardstate = atom({
    key: 'dashboardstate',
    default: 'overview',
})

export const dashboardselector = selector({
    key: 'dashboardselector',
    get: ({get}) =>{
        const page = get(dashboardstate)
        return page
    }
})

/* global state for dashboard login */

/* global state for username and email */
