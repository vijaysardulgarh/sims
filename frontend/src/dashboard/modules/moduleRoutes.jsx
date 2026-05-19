// import studentsRoutes from "./students/routes/studentsRoutes";
// import academicsRoutes from "./academics/routes/academicsRoutes";
// import examsRoutes from "./exams/routes/examsRoutes";
// import financeRoutes from "./finance/routes/financeRoutes";
// import attendanceRoutes from "./attendance/routes/attendanceRoutes";

// const moduleRoutes = (
//   <>
//     {studentsRoutes}
//     {academicsRoutes}
//     {attendanceRoutes}
//     {examsRoutes}
//     {financeRoutes}
//   </>
// );

// export default moduleRoutes;

import studentsRoutes
from "./students/routes/studentsRoutes";

import accessControlRoutes
from "./access_control/routes/accessControlRoutes";


const moduleRoutes = (

  <>

    {studentsRoutes}

    {accessControlRoutes}

  </>
);

export default moduleRoutes;