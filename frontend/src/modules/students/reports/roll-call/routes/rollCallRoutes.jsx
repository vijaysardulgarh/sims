import { Route } from "react-router-dom";

import RollCallReportPage
from "../pages/RollCallReportPage";

import RollCallPrintPage
from "../pages/RollCallPrintPage";

const rollCallRoutes = (

    <>

        <Route
            path="roll-call"
            element={
                <RollCallReportPage />
            }
        />

        <Route
            path="roll-call/print"
            element={
                <RollCallPrintPage />
            }
        />

    </>

);

export default rollCallRoutes;