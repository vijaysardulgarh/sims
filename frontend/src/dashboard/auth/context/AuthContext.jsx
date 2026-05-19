import {
    createContext,
    useContext,
    useState,
} from "react";

const AuthContext = createContext();

export const AuthProvider = ({
    children
}) => {

    const [user, setUser] =
        useState(null);

    const [accessToken,
        setAccessToken] =
        useState(
            localStorage.getItem(
                "access"
            )
        );

    const login = (
        data
    ) => {

        localStorage.setItem(
            "access",
            data.access
        );

        localStorage.setItem(
            "refresh",
            data.refresh
        );

        setAccessToken(
            data.access
        );

        setUser(
            data.user
        );
    };

    const logout = () => {

        localStorage.clear();

        setAccessToken(null);

        setUser(null);
    };

    return (

        <AuthContext.Provider
            value={{

                user,

                accessToken,

                login,

                logout,
            }}
        >

            {children}

        </AuthContext.Provider>
    );
};

export const useAuth = () =>
    useContext(AuthContext);