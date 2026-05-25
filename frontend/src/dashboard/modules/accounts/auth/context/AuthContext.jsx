import {

    createContext,

    useContext,

    useEffect,

    useState,

} from "react";

import { jwtDecode } from "jwt-decode";

import api from "../../../../../services/api";


// =====================================
// CONTEXT
// =====================================

export const AuthContext =
    createContext();


// =====================================
// PROVIDER
// =====================================

export const AuthProvider = ({
    children
}) => {

    // =====================================
    // GET STORED TOKEN
    // =====================================

    const getStoredToken = () => {

        return localStorage.getItem(
            "access"
        );
    };


    // =====================================
    // STATE
    // =====================================

    const [accessToken,
        setAccessToken] =
        useState(
            getStoredToken()
        );

    const [user,
        setUser] =
        useState(null);

    const [loading,
        setLoading] =
        useState(true);


    // =====================================
    // LOGIN
    // =====================================

    const login = (
        data
    ) => {

        // =============================
        // SAVE TOKENS
        // =============================

        localStorage.setItem(

            "access",

            data.access
        );

        localStorage.setItem(

            "refresh",

            data.refresh
        );

        // =============================
        // DECODE USER
        // =============================

        const decodedUser =

            jwtDecode(
                data.access
            );

        console.log(
            "DECODED USER:",
            decodedUser
        );

        // =============================
        // UPDATE STATE
        // =============================

        setAccessToken(
            data.access
        );

        setUser(
            decodedUser
        );
    };


    // =====================================
    // LOGOUT
    // =====================================

    const logout = () => {

        localStorage.removeItem(
            "access"
        );

        localStorage.removeItem(
            "refresh"
        );

        setAccessToken(null);

        setUser(null);
    };


    // =====================================
    // LOAD CURRENT USER
    // =====================================

    useEffect(() => {

        const loadUser =
            async () => {

            const token =
                localStorage.getItem(
                    "access"
                );

            if (!token) {

                setLoading(false);

                return;
            }

            try {

                // =====================
                // DECODE TOKEN
                // =====================

                const decodedUser =

                    jwtDecode(token);

                console.log(
                    "LOADED USER:",
                    decodedUser
                );

                setUser(
                    decodedUser
                );

                setAccessToken(
                    token
                );

            } catch (error) {

                console.log(
                    "AUTH ERROR:",
                    error
                );

                logout();

            } finally {

                setLoading(false);
            }
        };

        loadUser();

    }, []);


    // =====================================
    // LOADING SCREEN
    // =====================================

    if (loading) {

        return (

            <div
                className="
                    flex
                    items-center
                    justify-center
                    h-screen
                    text-xl
                "
            >

                Loading...

            </div>
        );
    }


    // =====================================
    // PROVIDER
    // =====================================

    return (

        <AuthContext.Provider

            value={{

                user,

                accessToken,

                loading,

                login,

                logout,
            }}
        >

            {children}

        </AuthContext.Provider>
    );
};


// =====================================
// CUSTOM HOOK
// =====================================

export const useAuth = () => {

    return useContext(
        AuthContext
    );
};