import {
    createContext,
    useContext,
    useEffect,
    useState,
} from "react";

import api from "../../../services/api";

import {
    setupInterceptors
} from "../../../services/api/interceptors";


// =====================================
// CONTEXT
// =====================================

const AuthContext =
    createContext();


// =====================================
// PROVIDER
// =====================================

export const AuthProvider = ({
    children
}) => {

    // =====================================
    // STATE
    // =====================================

    const [user,
        setUser] =
        useState(null);

    const [loading,
        setLoading] =
        useState(true);

    const [accessToken,
        setAccessToken] =
        useState(

            localStorage.getItem(
                "access"
            )
        );


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
            data.user
        );
    };


    // =====================================
    // LOGOUT
    // =====================================

    const logout = () => {

        // =============================
        // REMOVE TOKENS
        // =============================

        localStorage.removeItem(
            "access"
        );

        localStorage.removeItem(
            "refresh"
        );

        // =============================
        // CLEAR STATE
        // =============================

        setAccessToken(null);

        setUser(null);
    };


    // =====================================
    // AUTO LOAD USER
    // =====================================

    useEffect(() => {

        const initialize =
            async () => {

            // =========================
            // CHECK TOKEN
            // =========================

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
                // GET CURRENT USER
                // =====================

                const response =
                    await api.get(

                        "/users/me/"
                    );

                // =====================
                // SET USER
                // =====================

                setUser(
                    response.data
                );

            } catch (error) {

                console.error(
                    error
                );

                logout();
            }

            setLoading(false);
        };

        initialize();

    }, []);


    // =====================================
    // AXIOS INTERCEPTORS
    // =====================================

    useEffect(() => {

        setupInterceptors(
            logout
        );

    }, []);


    // =====================================
    // CONTEXT VALUE
    // =====================================

    return (

        <AuthContext.Provider

            value={{

                user,

                loading,

                accessToken,

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

export const useAuth = () =>

    useContext(
        AuthContext
    );