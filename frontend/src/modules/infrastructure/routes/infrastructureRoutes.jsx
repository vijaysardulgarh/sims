import { Route, Outlet } from "react-router-dom";

import buildingRoutes from "../buildings/routes/buildingRoutes";
import floorRoutes from "../floors/routes/floorRoutes";
import roomRoutes from "../rooms/routes/roomRoutes";
import classroomRoutes from "../classrooms/routes/classroomRoutes";
import laboratoryRoutes from "../laboratories/routes/laboratoryRoutes";
import libraryRoutes from "../libraries/routes/libraryRoutes";
import auditoriumRoutes from "../auditoriums/routes/auditoriumRoutes";
import playgroundRoutes from "../playgrounds/routes/playgroundRoutes";
import assetCategoryRoutes from "../asset-categories/routes/assetCategoryRoutes";
import assetRoutes from "../assets/routes/assetRoutes";
import maintenanceRecordRoutes from "../maintenance-records/routes/maintenanceRecordRoutes";
import facilityRoutes from "../facilities/routes/facilityRoutes";

const infrastructureRoutes = (
    <Route
        path="infrastructure"
        element={<Outlet />}
    >
        {buildingRoutes}
        {floorRoutes}
        {roomRoutes}
        {classroomRoutes}
        {laboratoryRoutes}
        {libraryRoutes}
        {auditoriumRoutes}
        {playgroundRoutes}
        {assetCategoryRoutes}
        {assetRoutes}
        {maintenanceRecordRoutes}
        {facilityRoutes}
    </Route>
);

export default infrastructureRoutes;