// ============================================
// IMPORTS
// ============================================

import { Route } from "react-router-dom";

import AssociationMemberListPage
from "../pages/AssociationMemberListPage";

import AssociationMemberAddPage
from "../pages/AssociationMemberAddPage";

import AssociationMemberEditPage
from "../pages/AssociationMemberEditPage";

// ============================================
// ROUTES
// ============================================

const associationMemberRoutes = (

    <>y

        <Route
            path="associations/association-members"
            element={
                <AssociationMemberListPage />
            }
        />

        <Route
            path="associations/association-members/add"
            element={
                <AssociationMemberAddPage />
            }
        />

        <Route
            path="associations/association-members/edit/:id"
            element={
                <AssociationMemberEditPage />
            }
        />

    </>

);

export default associationMemberRoutes;