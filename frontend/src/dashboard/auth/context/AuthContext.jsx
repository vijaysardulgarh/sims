import {

    createContext,

    useContext,

    useEffect,

    useState,

} from "react";

import api from "../../../services/api";


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
        // UPDATE STATE
        // =============================

        setAccessToken(
            data.access
        );

        setUser(
            data.user || null
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

            // =========================
            // GET TOKEN
            // =========================

            const token =
                localStorage.getItem(
                    "access"
                );

            console.log(
                "LOAD TOKEN:",
                token
            );

            // =========================
            // NO TOKEN
            // =========================

            if (!token) {

                setLoading(false);

                return;
            }

            try {

                // =====================
                // GET CURRENT USER
                // =====================

                const response =
                    await api.get(

                        "/users/me/"
                    );

                console.log(
                    "ME RESPONSE:",
                    response.data
                );

                // =====================
                // SAVE USER
                // =====================

                setUser(
                    response.data
                );

                // =====================
                // KEEP TOKEN
                // =====================

                setAccessToken(
                    token
                );

            } catch (error) {

                console.log(
                    "ME API ERROR:",
                    error
                );

            } finally {

                // =====================
                // STOP LOADING
                // =====================

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