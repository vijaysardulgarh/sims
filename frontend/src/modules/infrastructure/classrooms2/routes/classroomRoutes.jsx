import { Route } from 'react-router-dom';

import ClassroomsListPage
from '../pages/ClassroomsListPage';

import AddClassroomPage
from '../pages/AddClassroomPage';

import EditClassroomPage
from '../pages/EditClassroomPage';

const classroomRoutes = (

    <Route path="classrooms">

        <Route
            index
            element={
                <ClassroomsListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddClassroomPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditClassroomPage />
            }
        />

    </Route>
);

export default classroomRoutes;