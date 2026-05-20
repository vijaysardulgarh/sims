import {
    Routes,
    Route
} from "react-router-dom";

import LoginPage
from "../auth/pages/LoginPage";


const AuthRoutes = () => {

    return (

        <Routes>

            <Route

                path="login"

                element={<LoginPage />}
            />

        </Routes>
    );
};

export default AuthRoutes;