import { Route } from "react-router-dom";

import BranchesListPage from "../pages/BranchesListPage";
import AddBranchPage from "../pages/AddBranchPage";
import EditBranchPage from "../pages/EditBranchPage";

const branchRoutes = (

    <Route path="branches">

        <Route
            index
            element={<BranchesListPage />}
        />

        <Route
            path="add"
            element={<AddBranchPage />}
        />

        <Route
            path="edit/:id"
            element={<EditBranchPage />}
        />

    </Route>
);

export default branchRoutes;