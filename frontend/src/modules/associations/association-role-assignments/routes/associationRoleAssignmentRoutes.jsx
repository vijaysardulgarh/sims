// ============================================
// IMPORTS
// ============================================

import { Route } from "react-router-dom";

import AssociationRoleAssignmentListPage from "../pages/AssociationRoleAssignmentListPage";
import AssociationRoleAssignmentAddPage from "../pages/AssociationRoleAssignmentAddPage";
import AssociationRoleAssignmentEditPage from "../pages/AssociationRoleAssignmentEditPage";

// ============================================
// ROUTES
// ============================================

const associationRoleAssignmentRoutes = (

    <>

        <Route
            path="associations/association-role-assignments"
            element={
                <AssociationRoleAssignmentListPage />
            }
        />

        <Route
            path="associations/association-role-assignments/add"
            element={
                <AssociationRoleAssignmentAddPage />
            }
        />

        <Route
            path="associations/association-role-assignments/edit/:id"
            element={
                <AssociationRoleAssignmentEditPage />
            }
        />

    </>

);

export default associationRoleAssignmentRoutes;