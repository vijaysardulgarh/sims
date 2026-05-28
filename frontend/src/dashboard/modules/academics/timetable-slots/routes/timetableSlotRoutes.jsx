import { Route } from "react-router-dom";

import TimetableSlotsList from "../pages/TimetableSlotsList";
import AddTimetableSlot from "../pages/AddTimetableSlot";
import EditTimetableSlot from "../pages/EditTimetableSlot";

const timetableSlotRoutes = (
  <>
    <Route
      path="academics/timetable-slots"
      element={<TimetableSlotsList />}
    />

    <Route
      path="academics/timetable-slots/add"
      element={<AddTimetableSlot />}
    />

    <Route
      path="academics/timetable-slots/edit/:id"
      element={<EditTimetableSlot />}
    />
  </>
);

export default timetableSlotRoutes;