// =========================================
// REACT ROUTER
// =========================================

import { Route } from "react-router-dom";


// =========================================
// CLASSES
// =========================================

import ClassesList from
"./classes/ClassesList";

import AddClass from
"./classes/AddClass";

import EditClass from
"./classes/EditClass";


// =========================================
// STREAMS
// =========================================

import StreamsList from
"./streams/StreamsList";

import AddStream from
"./streams/AddStream";

import EditStream from
"./streams/EditStream";


// =========================================
// SECTIONS
// =========================================

import SectionsList from
"./sections/SectionsList";

import AddSection from
"./sections/AddSection";

import EditSection from
"./sections/EditSection";


// =========================================
// SUBJECTS
// =========================================

import SubjectsList from
"./subjects/SubjectsList";

import AddSubject from
"./subjects/AddSubject";

import EditSubject from
"./subjects/EditSubject";


// =========================================
// CLASS SUBJECTS
// =========================================

import ClassSubjectsList from
"./class-subjects/ClassSubjectsList";

import AddClassSubject from
"./class-subjects/AddClassSubject";

import EditClassSubject from
"./class-subjects/EditClassSubject";


// =========================================
// DAYS
// =========================================

import DaysList from
"./days/DaysList";

import AddDay from
"./days/AddDay";

import EditDay from
"./days/EditDay";


// =========================================
// TIMETABLE SLOTS
// =========================================

import TimetableSlotsList from
"./timetable-slots/TimetableSlotsList";

import AddTimetableSlot from
"./timetable-slots/AddTimetableSlot";

import EditTimetableSlot from
"./timetable-slots/EditTimetableSlot";


// =========================================
// TIMETABLE
// =========================================

import TimetableList from
"./timetable/TimetableList";

import AddTimetable from
"./timetable/AddTimetable";

import EditTimetable from
"./timetable/EditTimetable";


// =========================================
// ACADEMICS ROUTES
// =========================================

const academicsRoutes = (

  <>

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