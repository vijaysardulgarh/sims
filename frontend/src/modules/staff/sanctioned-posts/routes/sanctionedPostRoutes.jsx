import { Route } from "react-router-dom";

import SanctionedPostsList from "../pages/SanctionedPostsList";

import AddSanctionedPost from "../pages/AddSanctionedPost";

import EditSanctionedPost from "../pages/EditSanctionedPost";


const sanctionedPostRoutes = (

    <Route path="sanctioned-posts">

        <Route
            index
            element={<SanctionedPostsList />}
        />

        <Route
            path="add"
            element={<AddSanctionedPost />}
        />

        <Route
            path="edit/:id"
            element={<EditSanctionedPost />}
        />

    </Route>

);

export default sanctionedPostRoutes;