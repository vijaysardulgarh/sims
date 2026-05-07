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



import WebsiteRoutes from "../pages/website/routes/WebsiteRoutes";
import DashboardRoutes from "../dashboard/routes/DashboardRoutes";
import AuthRoutes from "../dashboard/routes/AuthRoutes";

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