// =========================================
// REACT ROUTER
// =========================================

import { Route } from "react-router-dom";


// =========================================
// ACADEMICS DASHBOARD
// =========================================

import AcademicDashboard from
"./dashboard/AcademicDashboard";


// =========================================
// CLASSES
// =========================================

import ClassesList from "./classes/pages/ClassesList";
import AddClass from "./classes/pages/AddClass";
import EditClass from "./classes/pages/EditClass";


// =========================================
// STREAMS
// =========================================

import StreamsList from
"./streams/pages/StreamsList";

import AddStream from
"./streams/pages/AddStream";

import EditStream from
"./streams/pages/EditStream";


// =========================================
// SECTIONS
// =========================================

import SectionsList from
"./sections/pages/SectionsList";

import AddSection from
"./sections/pages/AddSection";

import EditSection from
"./sections/pages/EditSection";


// =========================================
// SUBJECTS
// =========================================

import SubjectsList from
"./subjects/pages/SubjectsList";

import AddSubject from
"./subjects/pages/AddSubject";

import EditSubject from
"./subjects/pages/EditSubject";


// =========================================
// CLASS SUBJECTS
// =========================================

import ClassSubjectsList from
"./class-subjects/pages/ClassSubjectsList";

import AddClassSubject from
"./class-subjects/pages/AddClassSubject";

import EditClassSubject from
"./class-subjects/pages/EditClassSubject";


// =========================================
// DAYS
// =========================================

import DaysList from
"./days/pages/DaysList";

import AddDay from
"./days/pages/AddDay";

import EditDay from
"./days/pages/EditDay";


// =========================================
// TIMETABLE SLOTS
// =========================================

import TimetableSlotsList from
"./timetable-slots/pages/TimetableSlotsList";

import AddTimetableSlot from
"./timetable-slots/pages/AddTimetableSlot";

import EditTimetableSlot from
"./timetable-slots/pages/EditTimetableSlot";


// =========================================
// TIMETABLE
// =========================================

import TimetableList from
"./timetable/pages/TimetableList";

import AddTimetable from
"./timetable/pages/AddTimetable";

import EditTimetable from
"./timetable/pages/EditTimetable";


// =========================================
// ACADEMICS ROUTES
// =========================================

const academicsRoutes = (

  <>

    {/* ===================================== */}
    {/* ACADEMICS DASHBOARD */}
    {/* ===================================== */}

    <Route
      path="academics"
      element={<AcademicDashboard />}
    />


    {/* ===================================== */}
    {/* CLASSES */}
    {/* ===================================== */}

    <Route
      path="academics/classes"
      element={<ClassesList />}
    />

    <Route
      path="academics/classes/add"
      element={<AddClass />}
    />

    <Route
      path="academics/classes/edit/:id"
      element={<EditClass />}
    />


    {/* ===================================== */}
    {/* STREAMS */}
    {/* ===================================== */}

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


    {/* ===================================== */}
    {/* SECTIONS */}
    {/* ===================================== */}

    <Route
      path="academics/sections"
      element={<SectionsList />}
    />

    <Route
      path="academics/sections/add"
      element={<AddSection />}
    />

    <Route
      path="academics/sections/edit/:id"
      element={<EditSection />}
    />


    {/* ===================================== */}
    {/* SUBJECTS */}
    {/* ===================================== */}

    <Route
      path="academics/subjects"
      element={<SubjectsList />}
    />

    <Route
      path="academics/subjects/add"
      element={<AddSubject />}
    />

    <Route
      path="academics/subjects/edit/:id"
      element={<EditSubject />}
    />


    {/* ===================================== */}
    {/* CLASS SUBJECTS */}
    {/* ===================================== */}

    <Route
      path="academics/class-subjects"
      element={<ClassSubjectsList />}
    />

    <Route
      path="academics/class-subjects/add"
      element={<AddClassSubject />}
    />

    <Route
      path="academics/class-subjects/edit/:id"
      element={<EditClassSubject />}
    />


    {/* ===================================== */}
    {/* DAYS */}
    {/* ===================================== */}

    <Route
      path="academics/days"
      element={<DaysList />}
    />

    <Route
      path="academics/days/add"
      element={<AddDay />}
    />

    <Route
      path="academics/days/edit/:id"
      element={<EditDay />}
    />


    {/* ===================================== */}
    {/* TIMETABLE SLOTS */}
    {/* ===================================== */}

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


    {/* ===================================== */}
    {/* TIMETABLE */}
    {/* ===================================== */}

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

export default academicsRoutes;