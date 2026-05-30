import { Route } from "react-router-dom";

import UsersListPage from "../pages/UsersListPage";
import AddUserPage from "../pages/AddUserPage";
import EditUserPage from "../pages/EditUserPage";
import UserProfilePage from "../pages/UserProfilePage";

const userRoutes = (

    <Route path="users">

        <Route
            index
            element={<UsersListPage />}
        />

        <Route
            path="add"
            element={<AddUserPage />}
        />

        <Route
            path="edit/:id"
            element={<EditUserPage />}
        />

        <Route
            path="profile/:id"
            element={<UserProfilePage />}
        />

    </Route>
);

export default userRoutes;