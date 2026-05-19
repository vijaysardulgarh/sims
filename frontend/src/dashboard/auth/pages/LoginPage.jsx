import {
    useState
} from "react";

import {
    useNavigate
} from "react-router-dom";

import authService
from "../services/authService";

import {
    useAuth
} from "../context/AuthContext";


const LoginPage = () => {

    const navigate =
        useNavigate();

    const {
        login
    } = useAuth();

    const [email,
        setEmail] =
        useState("");

    const [password,
        setPassword] =
        useState("");

    const handleSubmit =
        async (e) => {

        e.preventDefault();

        try {

            const data =
                await authService.login({

                    email,
                    password,
                });

            login(data);

            navigate(
                "/dashboard"
            );

        } catch (error) {

            console.error(error);
        }
    };

    return (

        <form
            onSubmit={
                handleSubmit
            }
        >

            <input
                type="email"
                value={email}
                onChange={(e) =>
                    setEmail(
                        e.target.value
                    )
                }
            />

            <input
                type="password"
                value={password}
                onChange={(e) =>
                    setPassword(
                        e.target.value
                    )
                }
            />

            <button type="submit">

                Login

            </button>

        </form>
    );
};

export default LoginPage;