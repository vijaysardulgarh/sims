import { Route } from 'react-router-dom';

import PlaygroundsListPage
    from '../pages/PlaygroundsListPage';

import AddPlaygroundPage
    from '../pages/AddPlaygroundPage';

import EditPlaygroundPage
    from '../pages/EditPlaygroundPage';

const playgroundRoutes = (

    <Route path="playgrounds">

        <Route
            index
            element={
                <PlaygroundsListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddPlaygroundPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditPlaygroundPage />
            }
        />

    </Route>
);

export default playgroundRoutes;