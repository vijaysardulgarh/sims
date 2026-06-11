import {
    Route,
} from "react-router-dom";

import RoomAllocationListPage
    from "../pages/RoomAllocationListPage";

import RoomAllocationCreatePage
    from "../pages/RoomAllocationCreatePage";

import RoomAllocationEditPage
    from "../pages/RoomAllocationEditPage";

const roomAllocationRoutes = (

    <Route path="room-allocations">

        <Route
            index
            element={
                <RoomAllocationListPage />
            }
        />

        <Route
            path="add"
            element={
                <RoomAllocationCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <RoomAllocationEditPage />
            }
        />

    </Route>

);

export default roomAllocationRoutes;