import { Route } from "react-router-dom";

import StreamsList from "../pages/StreamsList";
import AddStream from "../pages/AddStream";
import EditStream from "../pages/EditStream";

const streamRoutes = (
  <>
    <Route
      path="academics/streams"
      element={<StreamsList />}
    />

    <Route
      path="academics/streams/add"
      element={<AddStream />}
    />

    <Route
      path="academics/streams/edit/:id"
      element={<EditStream />}
    />
  </>
);

export default streamRoutes;