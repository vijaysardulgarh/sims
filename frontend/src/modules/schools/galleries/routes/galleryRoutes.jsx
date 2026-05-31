import { Route } from "react-router-dom";

import GalleriesListPage from "../pages/GalleriesListPage";
import AddGalleryPage from "../pages/AddGalleryPage";
import EditGalleryPage from "../pages/EditGalleryPage";

const galleryRoutes = (

    <Route path="galleries">

        <Route
            index
            element={<GalleriesListPage />}
        />

        <Route
            path="add"
            element={<AddGalleryPage />}
        />

        <Route
            path="edit/:id"
            element={<EditGalleryPage />}
        />

    </Route>
);

export default galleryRoutes;