import { Route } from "react-router-dom";

import PostTypesList from "../pages/PostTypesList";

import AddPostType from "../pages/AddPostType";

import EditPostType from "../pages/EditPostType";


const postTypeRoutes = (

    <Route path="post-types">

        <Route
            index
            element={<PostTypesList />}
        />

        <Route
            path="add"
            element={<AddPostType />}
        />

        <Route
            path="edit/:id"
            element={<EditPostType />}
        />

    </Route>

);

export default postTypeRoutes;