import { Route } from 'react-router-dom';

import LibrariesListPage
from '../pages/LibrariesListPage';

import AddLibraryPage
from '../pages/AddLibraryPage';

import EditLibraryPage
from '../pages/EditLibraryPage';

const libraryRoutes = (

    <Route path="libraries">

        <Route
            index
            element={
                <LibrariesListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddLibraryPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditLibraryPage />
            }
        />

    </Route>
);

export default libraryRoutes;