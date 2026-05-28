import { Route } from "react-router-dom";

import StaffList from "../pages/StaffList";

import AddStaff from "../pages/AddStaff";

import EditStaff from "../pages/EditStaff";

import StaffProfile from "../pages/StaffProfile";


const staffProfileRoutes = (

    <Route path="staff-profiles">

        <Route
            index
            element={<StaffList />}
        />

        <Route
            path="add"
            element={<AddStaff />}
        />

        <Route
            path="edit/:id"
            element={<EditStaff />}
        />

        <Route
            path="profile/:id"
            element={<StaffProfile />}
        />

    </Route>

);

export default staffProfileRoutes;