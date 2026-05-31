import { Route } from 'react-router-dom';

import RoomsListPage from '../pages/RoomsListPage';

import AddRoomPage from '../pages/AddRoomPage';

import EditRoomPage from '../pages/EditRoomPage';

const roomRoutes = (

    <Route path="rooms">

        <Route
            index
            element={<RoomsListPage />}
        />

        <Route
            path="add"
            element={<AddRoomPage />}
        />

        <Route
            path="edit/:id"
            element={<EditRoomPage />}
        />

    </Route>
);

export default roomRoutes;