import WebsiteRoutes from "../website/routes/WebsiteRoutes";
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