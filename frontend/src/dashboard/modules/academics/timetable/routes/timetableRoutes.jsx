import { Route } from "react-router-dom";

import TimetableList from "../pages/TimetableList";
import AddTimetable from "../pages/AddTimetable";
import EditTimetable from "../pages/EditTimetable";

const timetableRoutes = (
  <>
    <Route
      path="academics/timetable"
      element={<TimetableList />}
    />

    <Route
      path="academics/timetable/add"
      element={<AddTimetable />}
    />

    <Route
      path="academics/timetable/edit/:id"
      element={<EditTimetable />}
    />
  </>
);

export default timetableRoutes;