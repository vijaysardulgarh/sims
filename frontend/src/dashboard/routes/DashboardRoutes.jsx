import {
    Routes,
    Route,
} from "react-router-dom";

import DashboardLayout
from "../layouts/DashboardLayout";

import moduleRoutes
from "../modules/moduleRoutes";

import ProtectedRoute
from "./ProtectedRoute";


const DashboardRoutes = () => {

    return (

        <Routes>

            <Route

                path="/dashboard/*"

                element={

                    <ProtectedRoute>

                        <DashboardLayout />

                    </ProtectedRoute>
                }
            >


                {moduleRoutes}

            </Route>

        </Routes>
    );
};

export default DashboardRoutes;