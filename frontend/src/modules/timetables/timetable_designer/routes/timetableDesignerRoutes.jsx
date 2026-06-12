import {
    Route,
} from 'react-router-dom';

import TimetableDesignerPage
    from '../pages/TimetableDesignerPage';

import TimetableConflictPage
    from '../pages/TimetableConflictPage';    

const timetableDesignerRoutes = (

    <Route path="timetable-designer">

        <Route
            index
            element={
                <TimetableDesignerPage />
            }
        />

        <Route
            path="conflicts"
            element={
                <TimetableConflictPage />
            }
        />

    </Route>

);

export default timetableDesignerRoutes;