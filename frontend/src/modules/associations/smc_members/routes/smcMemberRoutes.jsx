// ============================================
// IMPORTS
// ============================================

import { Route } from "react-router-dom";

import SMCMembersList from "../pages/SMCMembersList";
import SMCMemberCreate from "../pages/SMCMemberCreate";
import SMCMemberEdit from "../pages/SMCMemberEdit";
import SMCMemberView from "../pages/SMCMemberView";

// ============================================
// ROUTES
// ============================================

const smcMemberRoutes = (

    <>

        {/* ================================= */}
        {/* LIST */}
        {/* ================================= */}

        <Route
            path="associations/smc-members"
            element={<SMCMembersList />}
        />

        {/* ================================= */}
        {/* CREATE */}
        {/* ================================= */}

        <Route
            path="associations/smc-members/create"
            element={<SMCMemberCreate />}
        />

        {/* ================================= */}
        {/* EDIT */}
        {/* ================================= */}

        <Route
            path="associations/smc-members/edit/:id"
            element={<SMCMemberEdit />}
        />

        {/* ================================= */}
        {/* DETAIL */}
        {/* ================================= */}

        <Route
            path="associations/smc-members/:id"
            element={<SMCMemberView />}
        />

    </>

);

// ============================================
// EXPORT
// ============================================

export default smcMemberRoutes;