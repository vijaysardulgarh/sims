// import { Routes, Route } from "react-router-dom";

// import DashboardLayout from "../layouts/DashboardLayout";

// import AdminDashboard from "../dashboard/admin/Dashboard";
// import TeacherDashboard from "../dashboard/teacher/Dashboard";
// import StudentDashboard from "../dashboard/student/Dashboard";
// import PrincipalDashboard from "../dashboard/principal/Dashboard";

// import ProtectedRoute from "./ProtectedRoute";

// const AppRoutes = () => {
//   return (
//     <Routes>
//       <Route
//         path="/dashboard"
//         element={
//           <ProtectedRoute>
//             <DashboardLayout />
//           </ProtectedRoute>
//         }
//       >
//         <Route path="admin" element={<AdminDashboard />} />
//         <Route path="teacher" element={<TeacherDashboard />} />
//         <Route path="student" element={<StudentDashboard />} />
//         <Route path="principal" element={<PrincipalDashboard />} />
//       </Route>
//     </Routes>
//   );
// };

// export default AppRoutes;



import WebsiteRoutes from "./WebsiteRoutes";
import DashboardRoutes from "./DashboardRoutes";
import AuthRoutes from "./AuthRoutes";

const AppRoutes = () => {
  return (
    <>
      <WebsiteRoutes />
      <DashboardRoutes />
      <AuthRoutes />
    </>
  );
};

export default AppRoutes;