import {
    Routes,
    Route,
} from "react-router-dom";

import DashboardLayout
from "../layouts/DashboardLayout";

import roleRoutes
from "../roles/roleRoutes";

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

                {roleRoutes}

                {moduleRoutes}

            </Route>

        </Routes>
    );
};

export default DashboardRoutes;